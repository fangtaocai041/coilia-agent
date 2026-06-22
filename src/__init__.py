"""coilia-agent — 刀鲚专研智能体 (P₂/V3)"""

import sys as _sys
from pathlib import Path as _Path
_PROJECT_ROOT = str(_Path(__file__).resolve().parent.parent)
if _PROJECT_ROOT not in _sys.path:
    _sys.path.insert(0, _PROJECT_ROOT)
__version__ = "1.2.0"
