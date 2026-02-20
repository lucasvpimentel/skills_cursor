---
description: "Arquitetura de pipeline de dados: camadas (bronze/silver/gold), idempotência, orquestração, observabilidade e custos."
license: "MIT"
keywords: ["data","pipeline","architecture","etl","elt","orchestration","observability"]
---

# Data Pipeline Architect

## Objetivo
Desenhar pipeline robusto e escalável, com governança e observabilidade.

## Procedimento
1. Contexto:
   - fonte(s), frequência, SLA, volume, latência, custo
2. Modelagem de camadas:
   - Bronze: raw + audit columns
   - Silver: limpeza + padronização + dedupe
   - Gold: agregações e modelos analíticos
3. Requisitos não-funcionais:
   - idempotência
   - reprocessamento
   - versionamento de schema
   - lineage básico
4. Operação:
   - orquestração (DAG), retries, backfills
   - métricas (linhas, tempo, custo)
   - alertas (falha, atraso, anomalia)

## Saída obrigatória
### Diagrama lógico (camadas)
### Contratos por camada
### Estratégia de reprocessamento
### Observabilidade e alertas
### Checklist de produção
