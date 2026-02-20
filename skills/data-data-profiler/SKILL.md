---
description: "Perfilamento de dados: schema, tipos, missing, cardinalidade, outliers, distribuição e achados iniciais."
license: "MIT"
keywords: ["data","profiling","schema","missing","outliers","eda"]
---

# Data Profiler

## Objetivo
Gerar um perfil confiável do dataset antes de qualquer decisão.

## Procedimento
1. Identificar fonte(s), período, granularidade e chaves candidatas.
2. Levantar schema: colunas, tipos, valores especiais, padrões.
3. Calcular:
   - % missing e padrões de ausência
   - cardinalidade por coluna
   - duplicidades em chaves
   - estatísticas (min/max/mean/std/quantis) para numéricas
   - top valores para categóricas
4. Detectar outliers (IQR/z-score) e inconsistências (domínios inválidos).
5. Produzir resumo executivo + lista de riscos.

## Saída obrigatória
### Resumo executivo (5–10 linhas)
### Tabela de qualidade (missing, cardinalidade, duplicidade)
### Outliers e anomalias prováveis
### Próximas ações recomendadas
