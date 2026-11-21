# -*- coding: utf-8 -*-
from pathlib import Path
import base64, runpy, sys
here = Path(__file__).resolve().parent
parts = sorted(here.glob("_pl_c*.b64"))
if not parts:
    raise SystemExit("Faltam _pl_c*.b64 em scripts/")
raw = b"".join(base64.b64decode(p.read_text().strip() for p in parts)
target = here / "_pl_body.py"
target.write_bytes(raw)
sys.argv[0] = str(target)
runpy.run_path(str(target), run_name="__main__")
