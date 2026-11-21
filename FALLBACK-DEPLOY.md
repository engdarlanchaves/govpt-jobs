# Fallback deploy Cloudflare (conta engdarlanchaves)

Repo de desencargo - Nao e source de verdade do codigo SERVO.
Fonte de verdade: `Darlanchavess/Gov.pt` (branch `restore-21d98db`).

## Quando usar
- Workers Builds na Cloudflare falham de forma repetida.
- GitHub Actions na conta Darlanchavess indisponivel/limitado.

NAO usar no dia a dia.

## Prerequisitos
1. Secrets Actions neste repo (ou num mirror Gov.pt-deploy):
   - CLOUDFLARE_API_TOKEN
   - CLIOUDFLARE_ACCOUNT_ID = a59d977592818b2f30fd7ff211152be3
2. Codigo do worker disponivel (mirror do monorepo ou patch pontual).
3. Workflow com `workflow_dispatch` + `dry_run`.

## Passos rapidos
1. Mirror ou push da branch de trabalho para um repo nesta conta.
2. Run workflow com dry_run=true.
3. Se OK, run com dry_run=false sono para o worker certo.

## Regras
Sempre gravar chaves novas no Selo (UNIVERSAL_*).
Tools MCP github2_* soo com pedido explicito do dono.
