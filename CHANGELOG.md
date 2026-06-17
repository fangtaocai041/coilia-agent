# Changelog — coilia-agent

> 版本变更记录。参见 ROADMAP.md 了解技术改进路线图。

## v1.4.0 — 2026-06-27

### 🗂️ SpeciesRegistry 4 物种扩展 + --species CLI

- 🗂️ **SpeciesRegistry**: `src/agent/species_registry.py` — 统一管理 4 个 Coilia 属物种 (nasus/brachygnathus/mystus/grayii)
- 🏷️ **--species CLI**: 所有脚本 (`literature_search.py`/`migration_analysis.py`/`feeding_analysis.py`/`early_life_analysis.py`/`stock_assessment.py`) 支持 `--species` 参数
- 🧪 新增 `test_species_expansion.py` — SpeciesRegistry 多物种加载验证

---

## v1.3.0 — 2026-06-20
- 🔗 KB-First 搜索集成
- cross-project 协议更新

## v1.0.0 — 2026-06-06
- 初始发布 — 5 Skills · DirectLoader 认知搜索
