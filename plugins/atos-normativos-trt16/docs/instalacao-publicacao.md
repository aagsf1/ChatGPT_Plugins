# Instalação e preparação para publicação

## Estado da entrega

Pacote de arquivos versão 1.0.0, sem instalação na conta e sem publicação em diretório. Contém manifesto portátil `plugin.json`, manifesto de compatibilidade `.codex-plugin/plugin.json`, cinco skills e referências compartilhadas. Não requer API própria, chave, autenticação ou servidor MCP. Python só é necessário para a conferência opcional dos arquivos; não para o conteúdo das skills.

## Importação do pacote

1. Extraia o ZIP em pasta estável, preservando diretórios e arquivos iniciados por ponto.
2. A raiz do plugin é a pasta que contém `plugin.json`, `.codex-plugin/`, `skills/`, `references/` e `knowledge/`. Não importe apenas uma skill, pois ela depende do núcleo compartilhado.
3. Na superfície que disponibilizar importação de plugin por arquivo/pasta, selecione o ZIP ou essa raiz conforme solicitado. A disponibilidade do fluxo depende do aplicativo e das permissões da conta; não foi testada nesta entrega.
4. Confira nome, versão e cinco skills. Abra nova conversa e execute os casos de aceitação. Não considere a simples leitura do manifesto como comprovação de funcionamento.

## Catálogo pessoal no Codex

Se usar catálogo pessoal, copie a pasta do plugin para uma localização estável e adicione uma entrada ao catálogo pessoal existente em `~/.agents/plugins/marketplace.json`, preservando as demais entradas. Não substitua o arquivo completo por um exemplo. A configuração deve apontar para o caminho real e seguir a documentação da versão instalada. O pacote não altera esse arquivo nem registra catálogo na conta.

Exemplo para a convenção `~/plugins/atos-normativos-trt16` do criador local (o caminho da entrada é relativo à raiz pessoal):

```json
{
  "name": "atos-normativos-trt16",
  "source": {"source": "local", "path": "./plugins/atos-normativos-trt16"},
  "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
  "category": "Productivity"
}
```

O exemplo é uma entrada, não um catálogo completo. `ON_INSTALL` é metadado do catálogo, não uma integração de autenticação adicionada ao plugin. Se o ambiente adotar outra pasta, ajuste o caminho e confirme a resolução antes de instalar. Atualize/reinicie o aplicativo, abra o diretório de plugins, selecione a origem pessoal e instale. Para o catálogo pessoal padrão, não é necessário cadastrar outra origem por comando. Estas instruções são de preparação; a instalação real não foi executada.

## Publicação

O manifesto portátil segue o formato documentado pela OpenAI; o manifesto de compatibilidade é mantido para Codex. O campo `extensions.com.openai.interface` espelha a apresentação da versão de compatibilidade. Mantenha nome e versão iguais nos dois arquivos.

Antes de submeter, o responsável deve definir identificação do publicador, licença de distribuição e eventuais metadados exigidos pelo canal; verificar autorização de uso do nome e de documentos que venha a incorporar; completar as fontes necessárias; e testar na superfície de destino. O nome é provisório e não indica chancela do TRT-16. Não foram inventados publicador institucional, domínio, política de privacidade ou contatos. Requisitos adicionais do diretório e aprovação não são supridos pelo ZIP.

Não há promessa de importação universal nem de aceitação automática. Siga o procedimento atual do canal escolhido. Não crie servidor MCP apenas para distribuir instruções.

## Referências técnicas consultadas em 18 de setembro de 2026

- [Empacotamento de plugins — documentação oficial](https://developers.openai.com/plugins/build/plugins): estrutura portátil, compatibilidade e catálogos.
- Skills locais `plugin-creator` e `skill-creator`: scaffold e validação utilizados nesta entrega.

A entrega não depende da afirmação, na conversa anterior, sobre descontinuação de GPTs personalizados; essa afirmação não foi adotada como premissa necessária nem revalidada aqui.
