# govpt-jobs (conta B · engdarlanchaves)

Pipeline de listagens de oportunidades. Grava no **Supabase composition**.
A app vive em `Darlanchavess/Gov.pt` e só lê a BD.

## Desenho

```
Mordomo (preferido) ──┐
                      ├──► scripts ──► composition ──► app (conta A)
Conta B (este repo) ──┘   fallback cloud 1×/dia
```

## Secrets (Actions)

- `SUPABASE_URL` — projeto composition
- `SUPABASE_SERVICE_ROLE_KEY`
- `GOVPT_SOURCE_TOKEN` — PAT conta A com leitura do repo Gov.pt (sync dos scripts)

## Até ~1 dez 2026

Conta A sem cota Actions; se esta conta B tiver billing lock, correr no **PC/Mordomo**:

```bash
cd Gov.pt
export SUPABASE_URL=...
export SUPABASE_SERVICE_ROLE_KEY=...
python -u scripts/atualizar_concursos.py
python -u scripts/ext_oportunidades_fontes.py
```

Quando o billing da B desbloquear: Actions → Run workflow.

## Não fazer

- Não meter secrets no código
- Não depender do cron da conta A para listagens
