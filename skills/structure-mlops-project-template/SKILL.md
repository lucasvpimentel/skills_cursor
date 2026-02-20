---
description: "Gera estrutura de projeto MLOps (treino, validação, deploy, monitoramento) com pastas e arquivos padrão."
license: "MIT"
keywords: ["structure","mlops","ml","deployment","monitoring","ci-cd"]
---

# Structure - MLOps Project Template

## Regra
Gerar somente:
1) árvore de pastas/arquivos (tree)
2) descrição curta por item
3) checklist de produção
Sem código.
Sem execução.

## Cobertura mínima
- src/ (treino, inferência, features)
- data/ (somente amostras ou instruções, sem dados sensíveis)
- configs/
- notebooks/ (opcional)
- tests/
- pipelines/ (orquestração)
- docker/ (opcional)
- docs/ (runbook, ADR)
- monitoring/ (drift, métricas)
- ci/ (workflows)

## Saída obrigatória
### Estrutura (tree)
### Descrição dos componentes
### Checklist de MLOps (treino → deploy → monitoramento)
