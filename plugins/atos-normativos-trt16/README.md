# Atos Normativos TRT-16

**Versão 1.0.0 — nome provisório.** Plugin de trabalho independente, sem chancela institucional presumida, para apoiar análise, criação, revisão, consolidação e exame de colegiados. Conteúdo em português do Brasil.

## Comece aqui

1. Leia [instalação e publicação](docs/instalacao-publicacao.md).
2. Consulte [uso e exemplos](docs/uso.md).
3. Verifique o [catálogo de fontes](knowledge/catalogo-fontes.md) antes de usar o plugin em caso concreto.

O pacote contém as instruções completas dos cinco fluxos. **Não contém as íntegras das sete fontes normativas indicadas.** Sua situação está registrada individualmente. Fontes localizadas não são tratadas como normas integralmente verificadas. As instruções nunca substituem o conteúdo da norma vigente.

## Arquitetura

```text
atos-normativos-trt16/
  plugin.json                       Manifesto portátil
  .codex-plugin/plugin.json         Compatibilidade Codex
  README.md
  CHANGELOG.md
  skills/
    analise/SKILL.md
    criacao/SKILL.md
    revisao/SKILL.md
    consolidacao/SKILL.md
    colegiados/SKILL.md
    (cada skill inclui agents/openai.yaml)
  references/
    nucleo-comum.md                 Instruções compartilhadas
    protocolo-fontes.md             Regras de evidência e atualização
    controle-final.md               Conferência transversal
  knowledge/
    catalogo-fontes.md              Situação das sete fontes
    fontes.json                    Registro estruturado
    documentos/LEIA-ME.md           Orientação para incorporar íntegras
  docs/
    uso.md
    instalacao-publicacao.md
    casos-aceitacao.md
    validacao.md
  scripts/
    verificar_pacote.py
```

As referências são internas ao pacote, sem dependência de outro plugin. Não há APIs, servidor MCP, aplicativos conectados, chaves ou rotinas de transmissão de documentos. O conteúdo só é carregado quando a skill é usada; catálogo não é mecanismo de atualização automática.

## Capacidades

| Skill | Produto principal |
|---|---|
| Análise | Exame jurídico e técnico, achados por dispositivo e conclusão delimitada |
| Criação | Diagnóstico prévio, minuta e pendências [PREENCHER/CONFIRMAR] |
| Revisão | Texto revisado com preservação de mérito e quadro de mudanças |
| Consolidação | Reconstrução rastreável na data de corte ou projeto identificado |
| Colegiados | Diagnóstico de governança e propostas sobre as cinco categorias |

O núcleo cobre confiabilidade, hierarquia e incidência, competência, necessidade, técnica legislativa, remissões, temporalidade, publicação, padrão TRT-16 e controle final. Mudanças materiais são destacadas; dados ausentes não são inventados.

## Validação e limites

Consulte [o relatório de validação](docs/validacao.md) para os testes efetivamente executados e [os casos de aceitação](docs/casos-aceitacao.md) para testes após instalação. O pacote não foi instalado nem publicado. Validação estrutural não equivale a homologação jurídica, confirmação de vigência ou aprovação por diretório de plugins.

O formato foi conferido na [documentação oficial de empacotamento](https://developers.openai.com/plugins/build/plugins). A decisão sobre publicação, identidade do responsável e licença deve ser tomada antes da distribuição pública; não se atribui autoria ou chancela ao Tribunal.
