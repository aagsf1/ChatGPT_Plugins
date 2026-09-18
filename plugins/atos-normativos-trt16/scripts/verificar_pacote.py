"""Verifica integridade estrutural local; não certifica conteúdo jurídico."""
from pathlib import Path
import json
import re
import sys


def verify(root):
    errors = []
    expected = {'analise', 'criacao', 'revisao', 'consolidacao', 'colegiados'}
    try:
        portable = json.loads((root / 'plugin.json').read_text(encoding='utf-8'))
        compat = json.loads((root / '.codex-plugin/plugin.json').read_text(encoding='utf-8'))
        sources = json.loads((root / 'knowledge/fontes.json').read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        return [str(exc)]
    for key in ('name', 'version', 'description'):
        if portable.get(key) != compat.get(key):
            errors.append(f'Manifestos divergem: {key}')
    if root.name != compat.get('name'):
        errors.append('Nome da pasta difere do identificador.')
    if portable.get('extensions', {}).get('com.openai', {}).get('interface') != compat.get('interface'):
        errors.append('Apresentação dos manifestos diverge.')
    actual = {p.parent.name for p in (root / 'skills').glob('*/SKILL.md')}
    if actual != expected:
        errors.append(f'Skills inesperadas ou ausentes: {actual ^ expected}')
    for name in expected:
        path = root / 'skills' / name / 'SKILL.md'
        if not path.exists():
            continue
        content = path.read_text(encoding='utf-8')
        if not content.startswith(f'---\nname: {name}\ndescription: '):
            errors.append(f'Identificação inválida: {name}')
        if '../../references/nucleo-comum.md' not in content:
            errors.append(f'Núcleo não referenciado: {name}')
    for path in root.rglob('*.md'):
        content = path.read_text(encoding='utf-8')
        for link in re.findall(r'\]\(([^)]+)\)', content):
            if '://' in link or link.startswith('#'):
                continue
            target = (path.parent / link.split('#')[0]).resolve()
            if not target.is_relative_to(root.resolve()):
                errors.append(f'Referência fora do pacote: {path.name} -> {link}')
            elif not target.exists():
                errors.append(f'Referência ausente: {path.name} -> {link}')
    ids = [source['id'] for source in sources['fontes']]
    if len(ids) != 7 or len(ids) != len(set(ids)):
        errors.append('Catálogo deve conter sete identificadores únicos.')
    for source in sources['fontes']:
        if source['integra_incorporada']:
            file = source.get('arquivo')
            if not file or not (root / file).is_file():
                errors.append(f'Íntegra declarada sem arquivo: {source["id"]}')
    for unwanted in ('.mcp.json', 'mcp.json', '.app.json', 'hooks.json'):
        if (root / unwanted).exists():
            errors.append(f'Integração não prevista: {unwanted}')
    return errors


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    failures = verify(root)
    if failures:
        print('\n'.join(f'ERRO: {item}' for item in failures))
        sys.exit(1)
    print('OK: manifestos coerentes, cinco skills, referências internas e sete fontes verificadas estruturalmente.')
