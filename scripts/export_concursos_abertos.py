"""Exporta concursos abertos para public/data/concursos-abertos.json (snapshot CDN)."""
from __future__ import annotations

import datetime as dt
import json
import os
from pathlib import Path
from typing import Any, Dict, List

from supabase import create_client

SUPABASE_URL = (os.environ.get("SUPABASE_URL") or "").strip()
SUPABASE_KEY = (os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or "").strip()
TABLE = "01_MN_OPO_PUB_concursos_brutos"
PAGE = 1000
OUT = Path(__file__).resolve().parent.parent / "public" / "data" / "concursos-abertos.json"

COLUNAS = (
    "n_anuncio,data_publicacao,designacao/entidade,descricao_anuncio,url_pdf,"
    "tipos_contrato,preco_base,data_limite_propostas,cpvs,modelo_anuncio,lotes,"
    "distrito,concelho,lcoal_execucao,plataforma,enquadramento,pecas_procedimento,"
    "trabalhos_contrato,estado_prazo,data_limite_original"
}

