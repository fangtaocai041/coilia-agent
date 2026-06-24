"""Smoke test for coilia-agent imports and adapter."""
import sys
from pathlib import Path

_root = str(Path(__file__).resolve().parent.parent)
if _root not in sys.path:
    sys.path.insert(0, _root)


def test_imports():
    from src import __version__
    from src.adapter import CoiliaAdapter, get_adapter
    from src.agent.orchestrator import CoiliaOrchestrator
    from src.agent.species_registry import get_registry
    from src.agent.cognitive_analyzer import CognitiveAnalyzer, CognitiveState
    from src.rcca_core import SelfModelEngine, EmotionEngine
    print(f"[OK] coilia-agent v{__version__} imports OK")
    print(f"     CognitiveState values: {[s.value for s in CognitiveState]}")


def test_adapter():
    from src.adapter import CoiliaAdapter
    adapter = CoiliaAdapter()
    info = adapter.info()
    assert info["project"] == "coilia-agent"
    health = adapter.health()
    assert health["status"] in ("HEALTHY", "DEGRADED")
    print(f"[OK] adapter health: {health['status']}")


if __name__ == "__main__":
    for name, fn in [("imports", test_imports), ("adapter", test_adapter)]:
        try:
            fn()
        except Exception as e:
            print(f"[FAIL] {name}: {e}")
            sys.exit(1)
    print(f"\n2/2 passed")
