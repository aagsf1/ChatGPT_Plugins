# Relatório de validação

Versão 1.0.0 — 18 de setembro de 2026.

## Verificações executadas

- Manifesto de compatibilidade: aprovado pelo `validate_plugin.py` da skill local `plugin-creator`.
- Cinco skills: aprovadas individualmente pelo `quick_validate.py` da skill local `skill-creator`.
- Conferência adicional: nomes e versões dos dois manifestos coerentes; apresentação espelhada; cinco skills esperadas; referências Markdown locais existentes e contidas na raiz; sete fontes com identificadores únicos; ausência de integrações não previstas.
- Revisão editorial dos fluxos: distinção formal/material, precedência normativa, lacunas documentais, encadeamento das alterações e categorias de colegiados explicitados.
- ZIP: inclusão recursiva de todos os arquivos, inclusive `.codex-plugin/plugin.json`, com conferência de conteúdo e CRC após empacotamento. Resumo SHA-256 entregue ao lado do ZIP.

## Limites

O manifesto portátil foi comparado ao formato da documentação oficial; não foi submetido a um serviço de importação nem a validação remota de esquema. Os validadores locais não certificam raciocínio jurídico nem comportamento de execução. Os casos funcionais de `casos-aceitacao.md` foram preparados para teste após instalação; não são apresentados como testes executados em conta real. Não houve instalação, publicação ou validação integral das fontes normativas.

A dependência PyYAML foi usada somente no ambiente temporário de validação. O plugin distribuído não depende dela nem contém a biblioteca. A conferência estrutural adicional pode ser repetida com Python 3.9 ou superior:

```text
python scripts/verificar_pacote.py
```

O resultado positivo significa integridade estrutural no escopo descrito; não significa homologação institucional ou aptidão para decidir um caso sem suas fontes.
