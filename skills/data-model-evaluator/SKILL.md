---
description: "Avaliação de modelos: métricas corretas, overfitting, calibração, análise de erro, robustez e explicabilidade básica."
license: "MIT"
keywords: ["ml","evaluation","metrics","calibration","overfitting","error-analysis"]
---

# Model Evaluator

## Objetivo
Evitar aprovação de modelo por métrica errada ou avaliação fraca.

## Procedimento
1. Confirmar split (train/val/test) e vazamento.
2. Escolher métricas alinhadas ao objetivo:
   - classificação: precision/recall/F1/AUC-PR
   - regressão: MAE/RMSE/MAPE (com cuidado)
3. Diagnósticos:
   - overfitting (gap train vs val)
   - calibração (se probabilidade importa)
   - análise de erro (fatias por grupo)
4. Resultado:
   - recomendação de go/no-go
   - próximos experimentos

## Saída obrigatória
### Métricas e interpretação
### Diagnóstico de overfitting
### Análise de erro (slices)
### Recomendação e próximos passos
