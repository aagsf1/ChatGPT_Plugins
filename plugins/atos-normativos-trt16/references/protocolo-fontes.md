# Protocolo documental

1. Fixe objeto, versão recebida e data de corte solicitada. Sem data indicada, explicite a data adotada e sua razão. Inventarie documentos, anexos, atos modificadores, publicações e decisões que afetem eficácia.
2. Consulte `knowledge/fontes.json` e `knowledge/catalogo-fontes.md`. O catálogo aponta fontes; não contém, por si, a norma. “Localizada” não equivale a “lida”, “incorporada”, “vigente” ou “aplicável”.
3. Obtenha a íntegra oficial ou documento fornecido com procedência. Confirme órgão, espécie, número, data, publicação, anexos, retificações e alterações pertinentes. Se só houver excerto, limite conclusões ao excerto. Texto de pesquisa e ementa não bastam para reconstruir dispositivos.
4. Para fonte incorporada, registre identificador, título, órgão, data do ato e publicação, URL efetivamente aberta, consulta, arquivo relativo, versão/corte, páginas, integridade e hash SHA-256 se disponível. Guarde original e extração separados; verifique OCR em números, negações, remissões e quadros.
5. Confira alteração e revogação posteriores. Não deduza inexistência de alterações só porque o PDF não as menciona. Distingua versão histórica, consolidada oficial e reconstrução de trabalho.
6. Faça matriz de evidências: afirmação, fonte, dispositivo/página, trecho suficiente, situação documental, incidência e limitação. Não use uma citação para sustentar afirmação que o trecho não demonstra.
7. Divergências entre fontes exigem exame de autenticidade, competência, cronologia, publicação e alcance. Não escolha automaticamente o arquivo mais recente ou o texto mais conveniente. Mantenha cenário alternativo quando necessário.
8. Fonte indisponível: faça análise condicional, solicite apenas o documento indispensável e continue partes autônomas. Não afirme irregularidade ou regularidade integral sem suporte.

## Atualização do conhecimento

Inclua arquivos oficiais em `knowledge/documentos/` quando efetivamente recebidos ou obtidos. Atualize o catálogo e o registro JSON; não substitua silenciosamente versões antigas relevantes. Para cada atualização, registre origem, alteração e data no histórico. Não inclua dados pessoais desnecessários nem documentos de processo sigiloso em pacote destinado a distribuição pública. Não há sincronização automática nem integração externa neste plugin.

## Classes de evidência

- Confirmada: demonstrada pela fonte consultada, dentro do alcance e da data examinados.
- Parcial: só parte da afirmação foi demonstrada.
- Controvertida: fontes ou interpretações relevantes divergem.
- Não confirmada: sem evidência suficiente, sem presumir falsidade.
- Desatualizada: versão superada demonstrada documentalmente.
- Insuficiente: a lacuna impede o ponto específico da conclusão.
