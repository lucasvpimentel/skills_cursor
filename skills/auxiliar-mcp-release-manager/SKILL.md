---
description: "Gerencia releases de MCP server: versionamento, changelog, smoke tests, compatibilidade e plano de rollback para uso no Cursor."
license: "MIT"
keywords: ["mcp","release","versioning","changelog","smoke-test","rollback","cursor"]
---

# Auxiliar - MCP Release Manager

## Objetivo
Padronizar releases de MCP servers para evitar que o Cursor perca conexão ou tools quebrem após atualizações.

## Regras de saída
Gerar somente:
1) passo a passo numerado (release checklist)
2) template de changelog
3) plano de smoke test (mínimo)
4) plano de rollback
5) checklist de compatibilidade

Sem código (exceto nomes de arquivos e comandos PowerShell).
Sem execução.

## Versionamento (padrão sugerido)
- Usar SemVer: MAJOR.MINOR.PATCH
- MAJOR: quebra de compatibilidade de tool schema/outputs
- MINOR: tool nova ou feature compatível
- PATCH: correções internas sem alterar contratos

## Changelog (formato)
- Added
- Changed
- Fixed
- Deprecated
- Removed
- Security

## Smoke tests mínimos (obrigatório)
- Server sobe via command
- Cursor conecta e lista tools
- Tool crítica responde com input válido
- Tool crítica retorna erro padrão com input inválido
- Logs não expõem secrets

## Compatibilidade
- Mudanças em nomes de tools: evitar (ou manter alias temporário)
- Mudanças em schema de input/output: documentar e versionar MAJOR
- Timeouts e payload: documentar limites

## Rollback
- Manter última versão funcional disponível
- Instruções para alternar command/args para a versão anterior
- Critérios de rollback (ex.: tool não lista, erros críticos, regressão)

## Saída obrigatória (formato)
### Release Checklist (1..N)
### CHANGELOG.md (template)
### Smoke Test Plan
### Compatibilidade e Migração
### Rollback Plan
