"""CoiliaAdapter — coilia-agent (V3 / P₂ 同级项目).

Wraps CoiliaOrchestrator for cross-project consumption.
Provides otolith microchemistry + resource assessment as standard interface.

P₁(porpoise-agent) 与 P₂(coilia-agent) 为同级平行项目，
分别对应 eon-core 四象顶点 V2 和 V3。
"""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict

logger = logging.getLogger(__name__)


class CoiliaAdapter:
    """Adapter for coilia-agent (V3 — 刀鲚领域, P₂ 同级项目)."""

    project_name = "coilia-agent"

    def __init__(self) -> None:
        self._orchestrator: Any = None
        self._init_orchestrator()

    def _init_orchestrator(self) -> None:
        base = Path(__file__).resolve().parent.parent
        orch_file = base / "src" / "agent" / "orchestrator.py"
        if not orch_file.is_file():
            logger.warning(f"Coilia orchestrator not found at {orch_file}")
            return
        proj_str = str(base)
        if proj_str not in sys.path:
            sys.path.insert(0, proj_str)
        try:
            import importlib, importlib.util
            # Clear cached 'src' to avoid cross-project conflict
            for key in list(sys.modules.keys()):
                if key == "src" or key.startswith("src."):
                    del sys.modules[key]
            spec = importlib.util.spec_from_file_location(
                f"coilia.orchestrator.{id(self)}", str(orch_file))
            if spec and spec.loader:
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                cls = getattr(mod, "CoiliaOrchestrator", None)
                if cls:
                    self._orchestrator = cls()
        except Exception as exc:
            logger.warning(f"Coilia orchestrator init failed: {exc}")

    def search(self, query: str, **kwargs) -> Dict[str, Any]:
        if self._orchestrator:
            try:
                result = self._orchestrator.run(query)
                return {"status": "ok", "result": result}
            except Exception as exc:
                return {"status": "error", "error": str(exc)}
        return {"status": "unavailable", "query": query,
                "note": "Coilia orchestrator not loaded"}

    def health(self) -> Dict[str, Any]:
        return {"project": self.project_name,
                "status": "HEALTHY" if self._orchestrator else "DEGRADED"}

    def info(self) -> Dict[str, Any]:
        return {
            "project": self.project_name,
            "role": "V3_DomainVertexP2 (P₂ 同级项目)",
            "symbol": "🌦️ 少阳",
            "wuxing": "水 (WATER)",
            "capabilities": ["otolith_microchemistry", "migration_path",
                           "resource_assessment", "conservation_recommendations"],
        }


def get_adapter() -> CoiliaAdapter:
    return CoiliaAdapter()
