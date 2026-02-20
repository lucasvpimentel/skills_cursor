---
description: "Cria scaffold (estrutura inicial) de projeto de Data Science: pastas e arquivos base (data, notebooks, scripts, src, .env, .gitignore, README) ajustados ao tipo de problema."
license: "MIT"
keywords: ["project","data-science","scaffold","structure","template","repo"]
---

# Project DS Scaffold

## Objetivo
Gerar a estrutura básica de diretórios e arquivos para um projeto de Data Science, ajustando conforme o tipo de problema (ex.: classificação, regressão, séries temporais, NLP, visão, recomendação).

## Regras obrigatórias
- Produzir **apenas**:
  1) a árvore de diretórios/arquivos (em bloco de texto),
  2) a lista de arquivos com conteúdo inicial (somente para arquivos pequenos e essenciais),
  3) os comandos PowerShell para criar tudo.
- Não implementar modelos completos.
- Não baixar dados.
- Não incluir segredos reais (somente placeholders).

## Inputs esperados (perguntar se faltar)
- Tipo de problema (classificação/regressão/séries temporais/NLP/visão/recomendação/outro)
- Fonte de dados (arquivo, db, API) e formato (csv/parquet/etc.)
- Linguagem (default: Python)
- Ferramentas (ex.: Streamlit, MLflow, DVC) se desejadas

## Estrutura base obrigatória (mínimo)
- data/
  - raw/
  - interim/
  - processed/
- notebooks/
- scripts/
- src/
  - __init__.py
  - config/
  - data/
  - features/
  - models/
  - evaluation/
  - utils/
- tests/
- reports/
- .env (com placeholders)
- .gitignore
- README.md
- requirements.txt OU pyproject.toml (escolher um)

## Ajustes por tipo de problema (obrigatório)
- Séries temporais: adicionar src/time_series/, notebooks/ts/, docs sobre split temporal
- NLP: adicionar src/nlp/, notebooks/nlp/
- Visão: adicionar src/cv/, notebooks/cv/, data/images/
- Recomendação: adicionar src/recsys/, notebooks/recsys/
- Se Streamlit: adicionar app/ com app.py e requirements

## Saída obrigatória
1) **Tree**
2) **Conteúdo inicial** (somente: .gitignore, .env, README skeleton, requirements/pyproject skeleton)
3) **Comandos PowerShell** para criar diretórios e arquivos com Set-Content
