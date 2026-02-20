---
description: "Revisor de SQL: corretude, determinismo, performance, custo, legibilidade e armadilhas comuns em joins/aggregations."
license: "MIT"
keywords: ["sql","performance","cost","joins","cte","determinism","review"]
---

# SQL Reviewer

## Objetivo
Melhorar queries sem mudar significado (a menos que apontado como bug).

## Procedimento
1. Corretude:
   - chaves de join
   - duplicação por join (fanout)
   - filtros no lugar correto (before/after join)
2. Performance/custo:
   - evitar full scans quando possível
   - reduzir colunas e linhas cedo (pushdown)
   - agregações e janelas com parcimônia
3. Determinismo:
   - ORDER BY em funções de janela
   - LIMIT sem ORDER BY (evitar)
4. Legibilidade:
   - CTEs nomeadas
   - aliases claros
   - comentários sobre decisões

## Saída obrigatória
### Problemas encontrados (com trechos)
### Correções sugeridas (com query revisada)
### Riscos de mudança semântica
### Dicas de custo/performance
