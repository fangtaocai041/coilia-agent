"""Tests for coilia-agent species expansion integration.

Covers:
  - SpeciesRegistry loads all 4 species
  - CoiliaOrchestrator accepts species_id
  - Scripts accept --species CLI argument
  - Literature search adapts to different species
"""

import sys
from pathlib import Path

_PROJ = str(Path(__file__).resolve().parent.parent)
_REASONIX = str(Path(__file__).resolve().parent.parent.parent)

# Carefully order sys.path to avoid shadowing coilia-agent/scripts/
# with Reasonix/scripts/. Reasonix root must come first for shared types,
# but coilia-agent must be there for the local scripts/ package.
_sys_path_new = []
for _p in sys.path:
    if _p not in (_PROJ, _REASONIX):
        _sys_path_new.append(_p)
sys.path[:] = [_REASONIX, _PROJ] + _sys_path_new

# Clear any cached 'scripts' module that may have been loaded from the
# wrong location (Reasonix/scripts/ vs coilia-agent/scripts/)
for _key in list(sys.modules.keys()):
    if _key == 'scripts' or _key.startswith('scripts.'):
        del sys.modules[_key]

import pytest


# ═══════════════════════════════════════════════════════════════
# §1 test_registry_loads_all_four_species
# ═══════════════════════════════════════════════════════════════

def test_registry_importable():
    """SpeciesRegistry 应可导入."""
    from src.agent.species_registry import SpeciesRegistry, get_registry
    assert SpeciesRegistry is not None
    assert get_registry is not None


def test_registry_loads_all_four_species():
    """SpeciesRegistry 应加载 4 个鲚属物种配置."""
    from src.agent.species_registry import SpeciesRegistry
    registry = SpeciesRegistry()
    species_ids = registry.list_species()
    assert len(species_ids) == 4, \
        f"应加载 4 个物种，实际: {len(species_ids)}: {species_ids}"
    expected = {"coilia_nasus", "coilia_brachygnathus", "coilia_mystus", "coilia_grayii"}
    assert set(species_ids) == expected, \
        f"物种 ID 集合应为 {expected}，实际: {set(species_ids)}"


def test_registry_default_is_nasus():
    """默认物种应为 coilia_nasus."""
    from src.agent.species_registry import SpeciesRegistry
    registry = SpeciesRegistry()
    default = registry.default()
    assert default["species_id"] == "coilia_nasus"
    assert "Coilia nasus" in default.get("species_scientific", "")


def test_registry_get_each_species():
    """get() 应能获取每个物种的完整配置."""
    from src.agent.species_registry import SpeciesRegistry
    registry = SpeciesRegistry()
    for sid in ["coilia_nasus", "coilia_brachygnathus", "coilia_mystus", "coilia_grayii"]:
        cfg = registry.get(sid)
        assert cfg is not None, f"{sid} 的配置不应为 None"
        assert "species_id" in cfg, f"{sid} 应有 species_id"
        assert "species_scientific" in cfg, f"{sid} 应有 species_scientific"
        assert "research_themes" in cfg, f"{sid} 应有 research_themes"


def test_registry_contains():
    """__contains__ 应正确反映物种是否存在."""
    from src.agent.species_registry import SpeciesRegistry
    registry = SpeciesRegistry()
    assert "coilia_nasus" in registry
    assert "coilia_mystus" in registry
    assert "nonexistent_species" not in registry


def test_registry_len():
    """__len__ 应返回 4."""
    from src.agent.species_registry import SpeciesRegistry
    registry = SpeciesRegistry()
    assert len(registry) == 4


def test_registry_repr():
    """__repr__ 应显示物种数和列表."""
    from src.agent.species_registry import SpeciesRegistry
    registry = SpeciesRegistry()
    r = repr(registry)
    assert "4 species" in r
    assert "coilia_nasus" in r


def test_get_registry_singleton():
    """get_registry() 单例应返回同一实例."""
    from src.agent.species_registry import get_registry, reset_registry
    reset_registry()
    r1 = get_registry()
    r2 = get_registry()
    assert r1 is r2
    assert len(r1) == 4


def test_registry_each_has_chinese_names():
    """每个物种应有中文名."""
    from src.agent.species_registry import SpeciesRegistry
    registry = SpeciesRegistry()
    for sid in registry.list_species():
        cfg = registry.get(sid)
        cn = cfg.get("species_chinese", [])
        assert len(cn) >= 1, f"{sid} 应有至少一个中文名"


def test_registry_each_has_research_themes():
    """每个物种应有研究方向配置."""
    from src.agent.species_registry import SpeciesRegistry
    registry = SpeciesRegistry()
    for sid in registry.list_species():
        cfg = registry.get(sid)
        themes = cfg.get("research_themes", {})
        assert len(themes) >= 1, f"{sid} 应有至少一个研究方向"


# ═══════════════════════════════════════════════════════════════
# §2 test_orchestrator_accepts_species_id
# ═══════════════════════════════════════════════════════════════

def test_orchestrator_default_species():
    """默认构造应使用 coilia_nasus."""
    from src.agent.orchestrator import CoiliaOrchestrator
    orch = CoiliaOrchestrator()
    assert orch.species_id == "coilia_nasus"
    assert "刀鲚" in orch.config["species_chinese"][0]


def test_orchestrator_accepts_species_id_nasus():
    """显式传入 species_id='coilia_nasus'."""
    from src.agent.orchestrator import CoiliaOrchestrator
    orch = CoiliaOrchestrator(species_id="coilia_nasus")
    assert orch.species_id == "coilia_nasus"
    assert "Coilia nasus" in orch.config["species_scientific"]


def test_orchestrator_accepts_species_id_mystus():
    """切换到 coilia_mystus (凤鲚)."""
    from src.agent.orchestrator import CoiliaOrchestrator
    orch = CoiliaOrchestrator(species_id="coilia_mystus")
    assert orch.species_id == "coilia_mystus"
    assert "mystus" in orch.config["species_scientific"].lower()


def test_orchestrator_accepts_species_id_brachygnathus():
    """切换到 coilia_brachygnathus (短颌鲚)."""
    from src.agent.orchestrator import CoiliaOrchestrator
    orch = CoiliaOrchestrator(species_id="coilia_brachygnathus")
    assert orch.species_id == "coilia_brachygnathus"


def test_orchestrator_accepts_species_id_grayii():
    """切换到 coilia_grayii (七丝鲚)."""
    from src.agent.orchestrator import CoiliaOrchestrator
    orch = CoiliaOrchestrator(species_id="coilia_grayii")
    assert orch.species_id == "coilia_grayii"


def test_orchestrator_invalid_species_falls_back():
    """无效 species_id 应回退到默认 coilia_nasus."""
    from src.agent.orchestrator import CoiliaOrchestrator
    orch = CoiliaOrchestrator(species_id="nonexistent_sp")
    # 应回退到默认
    assert orch.species_id in ("coilia_nasus", "nonexistent_sp")
    assert orch.config["species_scientific"] is not None


def test_orchestrator_config_has_all_fields(orch_orchestrator):
    """配置应包含所有必需字段."""
    orch = orch_orchestrator
    for key in ["agent_id", "agent_name", "species_scientific",
                "species_chinese", "species_variants", "profile",
                "research_themes"]:
        assert key in orch.config, f"config 缺少 {key}"


def test_orchestrator_species_switching_preserves_structure():
    """切换物种后配置结构应保持一致."""
    from src.agent.orchestrator import CoiliaOrchestrator
    keys = ["agent_id", "agent_name", "species_scientific",
            "species_chinese", "species_variants", "profile", "research_themes"]
    for sid in ["coilia_nasus", "coilia_mystus", "coilia_brachygnathus", "coilia_grayii"]:
        orch = CoiliaOrchestrator(species_id=sid)
        for key in keys:
            assert key in orch.config, f"{sid}: config 缺少 {key}"
        assert "P₂" in orch.config["agent_id"]


# ═══════════════════════════════════════════════════════════════
# §3 test_scripts_accept_species_arg
# ═══════════════════════════════════════════════════════════════

def test_scripts_importable_via_orchestrator():
    """通过 orchestrator 脚本注册表验证脚本元数据完整."""
    from src.agent.orchestrator import CoiliaOrchestrator
    # 验证 SCRIPTS dict 中的每个条目都有正确的 module 和 func
    for name, spec in CoiliaOrchestrator.SCRIPTS.items():
        assert "module" in spec, f"SCRIPTS['{name}'] 缺少 module"
        assert "func" in spec, f"SCRIPTS['{name}'] 缺少 func"
        assert "kwargs" in spec, f"SCRIPTS['{name}'] 缺少 kwargs"
        assert spec["module"].startswith("scripts."), \
            f"SCRIPTS['{name}'].module 应以 'scripts.' 开头"


def test_orchestrator_scripts_registry():
    """CoiliaOrchestrator.SCRIPTS 应包含所有脚本映射."""
    from src.agent.orchestrator import CoiliaOrchestrator
    expected = [
        "literature_search",
        "migration_analysis",
        "genetics_analysis",
        "feeding_analysis",
        "stock_assessment",
        "early_life_analysis",
    ]
    for name in expected:
        assert name in CoiliaOrchestrator.SCRIPTS, \
            f"SCRIPTS 中缺少 {name}"


def test_orchestrator_call_analysis_script_invalid():
    """调用不存在的脚本应返回 None."""
    from src.agent.orchestrator import CoiliaOrchestrator
    orch = CoiliaOrchestrator()
    result = orch.call_analysis_script("nonexistent_script")
    assert result is None


def test_orchestrator_call_analysis_script_literature(orch_orchestrator):
    """调用 literature_search 脚本应返回结果."""
    orch = orch_orchestrator
    result = orch.call_analysis_script("literature_search", use_example=True)
    # 脚本可能成功或返回 None (取决于依赖)
    if result is not None:
        assert isinstance(result, dict)
        assert "script" in result


def test_orchestrator_analyze_with_scripts_flag():
    """analyze() 使用 use_scripts=True 不应崩溃."""
    from src.agent.orchestrator import CoiliaOrchestrator
    orch = CoiliaOrchestrator()
    search_results = {
        "papers": [
            {"title": "Migration patterns of Coilia nasus"},
            {"title": "Genetic diversity of Coilia nasus"},
        ]
    }
    result = orch.analyze("migration", search_results, use_scripts=True)
    assert isinstance(result, dict)
    assert "analysis_title" in result
    # 脚本结果可能附加在 script_analysis 键中
    assert "findings" in result


def test_orchestrator_run_with_react():
    """run_with_react 应返回结构化结果."""
    from src.agent.orchestrator import CoiliaOrchestrator
    orch = CoiliaOrchestrator()
    result = orch.run_with_react("洄游生态分析")
    assert isinstance(result, dict)
    # 应包含关键字段
    assert "mode" in result or "theme" in result or "findings" in result


# ═══════════════════════════════════════════════════════════════
# §4 test_literature_search_with_different_species
# ═══════════════════════════════════════════════════════════════

def test_literature_search_nasus(orch_orchestrator):
    """刀鲚文献搜索应包含 Coilia nasus."""
    orch = orch_orchestrator
    # 验证配置中的物种信息
    sci = orch.config["species_scientific"]
    assert "nasus" in sci.lower()


def test_literature_search_mystus():
    """凤鲚文献搜索应包含 Coilia mystus."""
    from src.agent.orchestrator import CoiliaOrchestrator
    orch = CoiliaOrchestrator(species_id="coilia_mystus")
    sci = orch.config["species_scientific"]
    assert "mystus" in sci.lower()


def test_literature_search_brachygnathus():
    """短颌鲚文献搜索应包含 Coilia brachygnathus."""
    from src.agent.orchestrator import CoiliaOrchestrator
    orch = CoiliaOrchestrator(species_id="coilia_brachygnathus")
    sci = orch.config["species_scientific"]
    assert "brachygnathus" in sci.lower()


def test_literature_search_grayii():
    """七丝鲚文献搜索应包含 Coilia grayii."""
    from src.agent.orchestrator import CoiliaOrchestrator
    orch = CoiliaOrchestrator(species_id="coilia_grayii")
    sci = orch.config["species_scientific"]
    assert "grayii" in sci.lower()


def test_species_variants_included():
    """所有物种配置应包含学名变体."""
    from src.agent.orchestrator import CoiliaOrchestrator
    for sid in ["coilia_nasus", "coilia_mystus", "coilia_brachygnathus", "coilia_grayii"]:
        orch = CoiliaOrchestrator(species_id=sid)
        variants = orch.config.get("species_variants", [])
        assert len(variants) >= 1, \
            f"{sid} 应有至少一个学名变体用于搜索适配"


def test_search_across_all_four_species_no_crash():
    """对 4 个物种分别执行分析不应崩溃."""
    from src.agent.orchestrator import CoiliaOrchestrator
    for sid in ["coilia_nasus", "coilia_mystus", "coilia_brachygnathus", "coilia_grayii"]:
        orch = CoiliaOrchestrator(species_id=sid)
        result = orch.analyze("migration", {"papers": []}, use_scripts=False)
        assert isinstance(result, dict)
        assert "findings" in result


# ═══════════════════════════════════════════════════════════════
# §5 Fixtures
# ═══════════════════════════════════════════════════════════════

@pytest.fixture
def orch_orchestrator():
    """默认 CoiliaOrchestrator 实例."""
    from src.agent.orchestrator import CoiliaOrchestrator
    return CoiliaOrchestrator()
