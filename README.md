![Python 3.10+](https://img.shields.io/badge/Python%203.10%2B-3776AB?style=flat-square)
  ![MIT](https://img.shields.io/badge/MIT-34D058?style=flat-square)
  ![v1.4.0](https://img.shields.io/badge/v1.4.0-8A4FCE?style=flat-square)
  ![4 species](https://img.shields.io/badge/4%20species-007EC6?style=flat-square)
  ![8 scripts](https://img.shields.io/badge/8%20scripts-FE7D37?style=flat-square)
  ![144 tests](https://img.shields.io/badge/144%20tests-D73A4A?style=flat-square)
  ![ReAct](https://img.shields.io/badge/ReAct%20Loop-0EA5E9?style=flat-square)
  ![Triangle](https://img.shields.io/badge/Triangle%20Powered-EC4899?style=flat-square)
  ![Domain](https://img.shields.io/badge/Coilia%20Migration-F59E0B?style=flat-square)
  ![CN-EN](https://img.shields.io/badge/CN-EN-6B7280?style=flat-square)
  [![DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/fangtaocai041/coilia-agent)
</p>

[English](README.md) · [中文](README.zh.md)

<div align="center"><h3>🌊 Everything flows.</h3></div>

The world is dynamic, knowledge is temporary, emergence is the norm.

---

## 📖 Table of Contents

- [Philosophy](#-philosophy)
- [Quick Start](#-quick-start)
- [Architecture](#-architecture)
- [Features](#-features)
- [Analysis Scripts](#-analysis-scripts)
- [Project Structure](#-project-structure)
- [Version History](#-version-history)
- [Self-Assessment](#-self-assessment)
- [Ecosystem](#-ecosystem)

---

## 🏛�?Philosophy

> Specialized knowledge, focused analysis. The river flows, and so do the fish.

This project is a **Derived Domain Expert (P�?** in the SanShengWanWu Triangle Core + Derived architecture, coordinated by **eon-core**. It inherits knowledge from S/V0 (fish-ecology-assistant) and verification from V/V1 (cognitive-search-engine), then specializes in *Coilia* genus research �?particularly the anadromous tapertail anchovy (*Coilia nasus*), one of the most economically and ecologically significant migratory fishes in the Yangtze River basin.

### 📜 Three Tenets

**🌊 The River Flows** �?Fish migrate, populations fluctuate, fisheries collapse and recover. Knowledge of a species' ecology is never static. We track it dynamically.

**🍂 Knowledge Drifts** �?Otolith microchemistry reveals new migration routes; genetic analysis uncovers cryptic species. Today's taxonomic consensus may shift with tomorrow's data.

**🌟 Emergence Patterns** �?When multiple analytical approaches (morphology + genetics + stable isotopes) converge on the same ecological insight, that's not coincidence �?it's emergence.

### ⚖️ Why This Matters

| Scenario | Traditional | Dynamic Worldview |
|:---------|:-----------|:-------------------|
| Species ID | Fixed taxonomy | SpeciesRegistry with 4 *Coilia* spp, expandable |
| Migration | Literature-only | Otolith microchemistry + population genetics |
| Stock status | Single-species MSY | Multi-species ecosystem approach |
| Conservation | Generic recommendations | Species-specific, lifecycle-stage-aware |

> 道生一，一生二，二生三，三生万物�?
---

## 🧩 What This Is

**Coilia Agent** is a specialized AI agent for *Coilia* genus research. Built on the Triangle Core (V0 knowledge + V1 search + Coord orchestration), it provides:

- **SpeciesRegistry**: YAML-defined profiles for 4 *Coilia* species (*C. nasus*, *C. brachygnathus*, *C. mystus*, *C. grayii*)
- **8 domain analysis scripts**: migration, genetics, feeding, early life history, stock assessment, literature search, species KB management
- **ReAct cognitive loop**: iterative Think→Act→Observe→Reflect for complex ecological analysis
- **144 tests**: comprehensive validation of analysis pipelines and triangle integration
- **--species CLI**: all scripts support `--species` argument for multi-species comparative analysis

---

## 🚀 Quick Start

```bash
# Clone
git clone git@github.com:fangtaocai041/coilia-agent.git
cd coilia-agent

# Install
pip install -e .

# Run
python -m coilia_agent run "migration analysis"

# Species-specific analysis
python scripts/migration_analysis.py --species "Coilia nasus"
python scripts/genetics_analysis.py --species "Coilia brachygnathus"
```

---

## 🏗�?Architecture

### Triangle Core + Derived Role

```
Triangle Core + Derived Architecture (coordinated by eon-core):

  S/V0  fish-ecology-assistant    �?Knowledge Supply
  V/V1  cognitive-search-engine   �?Search Verification
  Coord  eon-core                  �?Coordination Hub

  P�?   porpoise-agent            �?Porpoise Expert
  P�?   🐟 coilia-agent           �?Coilia Expert �?this project
  P�?   🐟 culter-agent           �?Culter Expert
  C     🔥 conflict-arbiter       �?Conflict Arbitration
```

### Internal Architecture

```
coilia-agent/
  src/
  ├── main.py                   CLI entry point
  ├── adapter.py                IProjectAdapter �?triangle bridge
  └── agent/
      ├── orchestrator.py       Task decomposition + pipeline routing
      ├── react_loop.py         Think→Act→Observe→Reflect cognitive loop
      ├── cognitive_analyzer.py Domain-specific analysis engine
      └── species_registry.py   SpeciesRegistry �?4 Coilia spp YAML config
  scripts/
  ├── migration_analysis.py     Otolith microchemistry + migration routes
  ├── genetics_analysis.py      Population genetics + eDNA methods
  ├── feeding_analysis.py       Stable isotope + gut content analysis
  ├── early_life_analysis.py    Larval dispersal + nursery habitat
  ├── stock_assessment.py       CPUE + length-frequency + growth models
  ├── literature_search.py      Multi-engine Coilia literature search
  ├── species_kb.py             Species knowledge base management
  ├── fish_kb_add_species.py    Add new species to fish-ecology KB
  └── shared_types.py           Canonical ecosystem types
  config/
  └── species/                  YAML profiles for 4 Coilia species
  tests/
  ├── test_coilia.py              Core agent tests
  ├── test_analysis_scripts.py    8 analysis script tests
  ├── test_scripts.py             Script integration tests
  ├── test_species_expansion.py   SpeciesRegistry tests
  ├── test_triangle_integration.py Triangle core integration tests
  ├── triangle_flow.py            Cross-project flow validation
  └── conftest.py                 Shared test fixtures
```

---

## �?Features

| Feature | Status | Description |
|---------|:------:|-------------|
| 🔬 Domain Analysis | �?| 8 species-specific research pipeline scripts |
| 📡 Triangle Powered | �?| V0 knowledge + V1 search + Coord orchestration |
| 🧠 Cognitive Loop | �?| ReAct pattern for iterative ecological analysis |
| 🗂�?SpeciesRegistry | �?| 4 *Coilia* species (nasus/brachygnathus/mystus/grayii) YAML config |
| 🏷�?--species CLI | �?| All scripts support `--species` for multi-species analysis |
| 🧬 Genetics Pipeline | �?| RAD-seq, microsatellite, SNP, eDNA analysis methods |
| 🐟 Migration Analysis | �?| Otolith microchemistry (Sr:Ca ratios), migration route modeling |
| 🍽�?Feeding Ecology | �?| Stable isotope (δ¹³C, δ¹⁵N) + gut content analysis |
| 📊 Stock Assessment | �?| CPUE standardization, length-frequency, growth models |
| 🔄 Cross-Project | �?| Direct fish-ecology KB read/write via triangle bridge |
| 🧪 Test Suite | �?| 144 tests covering 8 scripts + triangle integration |

---

## 📊 Analysis Scripts

| Script | Domain | Key Methods |
|--------|--------|-------------|
| `migration_analysis.py` | Migration Ecology | Otolith Sr:Ca, δ¹⁸O, migration route mapping |
| `genetics_analysis.py` | Population Genetics | RAD-seq, microsatellite, SNP, eDNA |
| `feeding_analysis.py` | Trophic Ecology | Stable isotopes (δ¹³C, δ¹⁵N), gut contents, SIBER |
| `early_life_analysis.py` | Early Life History | Larval dispersal, nursery habitat, growth back-calculation |
| `stock_assessment.py` | Fisheries Science | CPUE, length-frequency, von Bertalanffy growth |
| `literature_search.py` | Literature Review | Multi-engine Coilia-specific search |
| `species_kb.py` | Knowledge Management | Species profile CRUD, cross-project sync |
| `fish_kb_add_species.py` | KB Expansion | Add new species to fish-ecology-assistant KB |

---

## 📁 Project Structure

```
coilia-agent/
  (see Architecture section above)
```

---

## 📜 Version History

| Version | Date | Highlights |
|---------|------|------------|
| **v1.4.0** | 2026-06-17 | SpeciesRegistry (4 species), 8 analysis scripts, 144 tests, triangle integration |
| v1.3.0 | 2026-06-12 | ReAct cognitive loop, cognitive_analyzer, --species CLI across all scripts |
| v1.2.0 | 2026-06-07 | Migration + genetics + feeding analysis pipelines |
| v1.1.0 | 2026-06-05 | Triangle core bridge (IProjectAdapter), orchestrator task routing |
| v1.0.0 | 2026-06-01 | Initial coilia agent framework, literature search |

---

## 🪞 Self-Assessment

| Dimension | Rating | Notes |
|-----------|:-----:|-------|
| 🔬 Domain Depth | ⭐⭐⭐⭐�?| 4 Coilia species with YAML profiles |
| 📡 Triangle Integration | ⭐⭐⭐⭐�?| Direct fish-ecology KB read/write |
| 🧠 Cognitive Architecture | ⭐⭐⭐⭐�?| ReAct loop for iterative analysis |
| 🧪 Test Coverage | ⭐⭐⭐⭐�?| 144 tests across 8 scripts |
| 🚀 Extensibility | ⭐⭐⭐⭐�?| Add species = new YAML file |

### Strengths
- **Taxonomic focus**: Deep specialization on *Coilia* genus �?otolith microchemistry, migration ecology, genetics
- **Triangle-powered**: All 8 scripts can pull data from fish-ecology KB and validate findings via cognitive-search-engine
- **SpeciesRegistry**: Extensible YAML design �?adding a 5th *Coilia* species requires only a new YAML file
- **CLI consistency**: Every script supports the same `--species` interface for comparative analysis
- **Cross-project integration**: Direct read/write to fish-ecology-assistant KB via adapter.py

### Current Limitations
- Limited to 4 *Coilia* species (nasus, brachygnathus, mystus, grayii) �?other engraulids not covered
- Genetics pipeline methods are scaffolded; actual RAD-seq/eDNA processing requires external tools
- Otolith analysis assumes LA-ICP-MS data format; EPMA support pending
- Single-agent architecture (no internal MAS like porpoise-agent)

### Roadmap
- [ ] Expand to all ~15 *Coilia* species (including *C. mystus* complex resolution)
- [ ] Direct LA-ICP-MS data import for otolith analysis
- [ ] Integrated population dynamics model (Stock Synthesis 3)
- [ ] Multi-agent internal architecture for parallel analysis workflows

---

## 🔗 Ecosystem

This project is the **Coilia Domain Expert (P�?** in the SanShengWanWu ecosystem.

```
Triangle Core + Derived Architecture (coordinated by eon-core):

  S/V0  📦 fish-ecology-assistant    �?Knowledge Supply
  V/V1  🔍 cognitive-search-engine   �?Search Verification
  Coord ⚙️ eon-core                  �?Coordination Hub

  P�?   🐬 porpoise-agent           �?Porpoise Expert
  P�?   🐟 coilia-agent             �?Coilia Expert �?this project
  P�?   🐟 culter-agent             �?Culter Expert
  C     🔥 conflict-arbiter         �?Conflict Arbitration
```

> 🔥 Together infinite power, apart top expert engines.

---

## 📋 README Changelog

| Version | Date | Theme | What Changed |
|---------|------|-------|-------------|
| v8.0 | 2026-06-20 | README Restoration | Restored archive, re-added badges, deep structure |
| v7.0 | 2026-06-19 | Self-Assessment Overhaul | Star ratings, structured Strengths/Limitations/Roadmap |
| v6.0 | 2026-06-18 | Ecosystem Map | Added full Triangle Core + Derived diagram, cross-project links |
| v5.0 | 2026-06-17 | v1.4.0 Sync | Analysis scripts table, 144 tests, SpeciesRegistry docs |
| v4.0 | 2026-06-14 | Philosophy Section | Three Tenets, Why This Matters comparison table |
| v3.0 | 2026-06-10 | Architecture Deep-Dive | Internal architecture tree, Triangle Core + Derived role |
| v2.0 | 2026-06-05 | Quick Start Enrichment | CLI examples, species-specific commands |
| v1.0.0 | 2026-06-01 | Initial Draft | Project overview, basic structure, features table |

---

🌱 **Everything Flows · Panta Rhei**

> Heraclitus said: No man ever steps in the same river twice.
>
> We say: You cannot analyze today's ecological data with last month's code.

This project is not a fixed toolset �?it is a **living system**. Every component has built-in expiration mechanisms, version tracking, and emergence awareness. As your research deepens, packages update, and new methods emerge, it evolves with you.

*Last updated: 2026-06-17　|　Environment: Reasonix Code · DeepSeek Powered*
