---
description: "Gera e revisa configuração de MCP servers para Cursor (mcpServers) com command/args/env e checklist de validação. Saída em PowerShell + JSON."
license: "MIT"
keywords: ["mcp","cursor","mcpServers","configuration","json","env"]
---

# Auxiliar - MCP Configurator

## Objetivo
Produzir configuração MCP no formato esperado pelo Cursor, incluindo:
- command, args
- env (quando necessário)
- instruções PowerShell para testar localmente

## Regras
- Responder com:
  1) snippet JSON { ""mcpServers"": { ... } }
  2) comandos PowerShell para testar a execução do servidor
  3) checklist de diagnóstico (se não conectar)
- Não inventar campos fora do padrão.
- Se o usuário não informar o runtime, assumir Node (stdio).

## Checklist final
- [ ] command executa no PowerShell
- [ ] args corretos
- [ ] env configurado (se necessário)
- [ ] Cursor reconhece o server e expõe as tools
