---
description: "Engenharia de features: evitar leakage, alinhar tempo, codificações, escalas, janelas e justificativa estatística."
license: "MIT"
keywords: ["ml","features","leakage","encoding","scaling","time-series"]
---

# Feature Engineering

## Objetivo
Criar features úteis e seguras, com foco em generalização.

## Procedimento
1. Definir alvo e momento de previsão (T0).
2. Leakage check:
   - qualquer informação do futuro em relação a T0 é proibida
3. Estratégias:
   - numéricas: scaling quando necessário
   - categóricas: one-hot/target encoding com cuidado
   - temporais: lags, rolling windows, sazonalidade
4. Documentar:
   - fórmula/SQL da feature
   - motivação
   - riscos e validação

## Saída obrigatória
### Lista de features (com fórmula)
### Verificação de leakage
### Requisitos de dados por feature
### Plano de validação
