---
description: "Checklist de segurança para MCP: secrets, permissões, PII, logging sensível e superfície de ataque de tools."
license: "MIT"
keywords: ["mcp","security","secrets","pii","permissions","risk"]
---

# Auxiliar - MCP Security Check

## Objetivo
Reduzir riscos ao expor ferramentas externas via MCP.

## Regras de saída
Gerar somente:
1) checklist de segurança (bullets)
2) riscos e mitigação (tabela curta)
3) recomendações de configuração (env, permissões)

## Cobertura mínima
- secrets fora do código (env)
- PII: minimização e mascaramento
- permissões mínimas (principle of least privilege)
- logs sem dados sensíveis
- validação de inputs nas tools
