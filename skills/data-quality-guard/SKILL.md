---
description: "Guardião de qualidade de dados: regras, validações, contratos de schema e checagens de consistência."
license: "MIT"
keywords: ["data","quality","validation","schema","contracts","checks"]
---

# Data Quality Guard

## Objetivo
Evitar que dados ruins entrem no pipeline e quebrar cedo com mensagens claras.

## Procedimento
1. Definir contrato mínimo:
   - colunas obrigatórias
   - tipos esperados
   - chaves únicas
2. Aplicar checks:
   - null checks (obrigatórias)
   - range checks (ex.: idade 0..120)
   - domínio (ex.: UF ∈ {AC..TO})
   - duplicidade em chaves
   - integridade referencial (quando existir dimensão)
3. Definir severidade:
   - ERROR: bloqueia pipeline
   - WARN: alerta e segue (com log)
4. Produzir relatório de qualidade com contagens e exemplos.

## Saída obrigatória
### Contratos (tabela)
### Checks aplicados (pass/fail)
### Registros exemplares (amostras)
### Recomendações de correção (upstream/downstream)
