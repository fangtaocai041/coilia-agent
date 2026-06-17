![Python 3.10+](https://img.shields.io/badge/Python%203.10%2B-3776AB?style=flat-square)
  ![MIT](https://img.shields.io/badge/MIT-34D058?style=flat-square)
  ![v1.4.0](https://img.shields.io/badge/v1.4.0-8A4FCE?style=flat-square)
  ![4 species](https://img.shields.io/badge/4%20物种-007EC6?style=flat-square)
  ![8 scripts](https://img.shields.io/badge/8%20脚本-FE7D37?style=flat-square)
  ![144 tests](https://img.shields.io/badge/144%20测试-D73A4A?style=flat-square)
  ![ReAct](https://img.shields.io/badge/ReAct%20循环-0EA5E9?style=flat-square)
  ![Triangle](https://img.shields.io/badge/三角赋能-EC4899?style=flat-square)
  ![Domain](https://img.shields.io/badge/刀鲚洄?F59E0B?style=flat-square)
  ![CN-EN](https://img.shields.io/badge/中英双语-6B7280?style=flat-square)
  [![DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/fangtaocai041/coilia-agent)
</p>

[English](README.md) · [中文](README.zh.md)

<div align="center"><h3>🌊 万物皆流?/h3></div>

世界是动态的，知识是暂时的，涌现是常态?
---

## 📖 目录

- [哲学](#-哲学)
- [快速开始](#-快速开?
- [架构](#-架构)
- [功能特性](#-功能特?
- [分析脚本](#-分析脚本)
- [项目结构](#-项目结构)
- [版本历史](#-版本历史)
- [自我评估](#-自我评估)
- [生态体系](#-生态体?

---

## 🏛?哲学

> 专精之知，聚焦之析。河水流淌，鱼儿亦然?
本项目是三生万物三角核心 + 衍生架构中的**衍生领域专家（P₂）**，由 **eon-core** 统一协调。它?S/V0（fish-ecology-assistant）继承知识，?V/V1（cognitive-search-engine）继承验证能力，专注于鲚属（*Coilia*）鱼类研究——特别是长江流域最具经济与生态价值的溯河洄游鱼类刀鲚（*Coilia nasus*）?
### 📜 三谛

**🌊 万象流转** ?鱼类洄游，种群波动，渔业兴衰。物种生态学知识从不静止，我们动态追踪?
**🍂 真知若寄** ?耳石微化学揭示新洄游路线；遗传分析发现隐存种。今天的分类共识可能随明日数据而改变?
**🌟 涌现成章** ?当多种分析方法（形态学+遗传?稳定同位素）汇聚于同一生态洞见，那不是巧合——是涌现?
### ⚖ 何以重要

| 事境 | 旧习 | 新观 |
|:-----|:----|:----|
| 物种鉴定 | 固定分类 | SpeciesRegistry ?4 种鲚属，可扩?|
| 洄游研究 | 仅文?| 耳石微化?+ 种群遗传?|
| 资源评估 | 单种 MSY | 多种生态系统方?|
| 保护建议 | 通用建议 | 物种专属、生活史阶段感知 |

> 道生一，一生二，二生三，三生万物?
---

## 🧩 这个项目是什?
**Coilia Agent** 是一个专注于鲚属鱼类研究的专?AI 智能体。构建于三角核心之上（V0 知识 + V1 搜索 + Coord 编排），提供?
- **SpeciesRegistry**? 种鲚属（刀?短颌?凤鲚/七丝鲚）?YAML 配置档案
- **8 个领域分析脚?*：洄游、遗传、摄食、早期生活史、资源评估、文献搜索、物种知识库管理
- **ReAct 认知循环**：迭代式 Think→Act→Observe→Reflect 进行复杂生态分?- **144 项测?*：分析流水线与三角集成的全面验证
- **--species CLI**：所有脚本支?`--species` 参数进行多物种比较分?
---

## 🚀 快速开?
```bash
git clone git@github.com:fangtaocai041/coilia-agent.git
cd coilia-agent
pip install -e .
python -m coilia_agent run "洄游分析"

# 物种专属分析
python scripts/migration_analysis.py --species "Coilia nasus"
python scripts/genetics_analysis.py --species "Coilia brachygnathus"
```

---

## 🏗?架构

### 三角核心 + 衍生角色

```
三角核心 + 衍生架构（由 eon-core 协调）：

  S/V0  fish-ecology-assistant    ?知识供给
  V/V1  cognitive-search-engine   ?搜索验证
  Coord  eon-core                  ?协调内核

  P?   porpoise-agent            ?江豚专家
  P?   🐟 coilia-agent           ?刀鲚专??本项?  P?   🐟 culter-agent           ?鲌类专家
  C     🔥 conflict-arbiter       ?冲突仲裁
```

### 内部架构

```
coilia-agent/
  src/
  ├── main.py                   CLI 入口
  ├── adapter.py                IProjectAdapter ?三角桥接
  └── agent/
      ├── orchestrator.py       任务分解 + 流水线路?      ├── react_loop.py         Think→Act→Observe→Reflect 认知循环
      ├── cognitive_analyzer.py 领域分析引擎
      └── species_registry.py   SpeciesRegistry ?4 种鲚?YAML 配置
  scripts/
  ├── migration_analysis.py     耳石微化?+ 洄游路线
  ├── genetics_analysis.py      种群遗传?+ eDNA 方法
  ├── feeding_analysis.py       稳定同位?+ 胃含物分?  ├── early_life_analysis.py    仔鱼扩散 + 育幼栖息?  ├── stock_assessment.py       CPUE + 体长频率 + 生长模型
  ├── literature_search.py      多引擎鲚属文献搜?  ├── species_kb.py             物种知识库管?  ├── fish_kb_add_species.py    向鱼类生态知识库添加新物?  └── shared_types.py           规范生态类?  config/
  └── species/                  4 种鲚?YAML 物种档案
  tests/
  ├── test_coilia.py              核心智能体测?  ├── test_analysis_scripts.py    8 个分析脚本测?  ├── test_scripts.py             脚本集成测试
  ├── test_species_expansion.py   SpeciesRegistry 测试
  ├── test_triangle_integration.py 三角核心集成测试
  ├── triangle_flow.py            跨项目流程验?  └── conftest.py                 共享测试夹具
```

---

## ?功能特?
| 功能 | 状?| 说明 |
|------|:--:|------|
| 🔬 领域分析 | ?| 8 个物种专属研究流水线脚本 |
| 📡 三角赋能 | ?| V0知识 + V1搜索 + Coord编排 |
| 🧠 认知循环 | ?| ReAct 模式迭代生态分?|
| 🗂?SpeciesRegistry | ?| 4 种鲚属（刀?短颌?凤鲚/七丝鲚）YAML 配置 |
| 🏷?--species CLI | ?| 所有脚本支?`--species` 多物种分?|
| 🧬 遗传学流水线 | ?| RAD-seq、微卫星、SNP、eDNA 分析方法 |
| 🐟 洄游分析 | ?| 耳石微化学（Sr:Ca比）、洄游路线建?|
| 🍽?摄食生?| ?| 稳定同位素（δ¹³C、δ¹⁵N? 胃含物分?|
| 📊 资源评估 | ?| CPUE 标准化、体长频率、生长模?|
| 🔄 跨项?| ?| 通过三角桥接直接读写鱼类生态知识库 |
| 🧪 测试套件 | ?| 144 项测试覆?8 脚本 + 三角集成 |

---

## 📊 分析脚本

| 脚本 | 领域 | 核心方法 |
|------|------|----------|
| `migration_analysis.py` | 洄游生?| 耳石 Sr:Ca、δ¹⁸O、洄游路线制?|
| `genetics_analysis.py` | 种群遗传 | RAD-seq、微卫星、SNP、eDNA |
| `feeding_analysis.py` | 营养生?| 稳定同位素（δ¹³C、δ¹⁵N）、胃含物、SIBER |
| `early_life_analysis.py` | 早期生活?| 仔鱼扩散、育幼栖息地、生长反?|
| `stock_assessment.py` | 渔业科学 | CPUE、体长频率、von Bertalanffy 生长 |
| `literature_search.py` | 文献综述 | 多引擎鲚属专属搜?|
| `species_kb.py` | 知识管理 | 物种档案 CRUD、跨项目同步 |
| `fish_kb_add_species.py` | 知识库扩?| 向鱼类生态助手知识库添加新物?|

---

## 📁 项目结构

```
coilia-agent/
  （见上方架构图）
```

---

## 📜 版本历史

| 版本 | 日期 | 重要更新 |
|------|------|----------|
| **v1.4.0** | 2026-06-17 | SpeciesRegistry?种）? 分析脚本?44 测试，三角集?|
| v1.3.0 | 2026-06-12 | ReAct 认知循环，cognitive_analyzer，全脚本 --species CLI |
| v1.2.0 | 2026-06-07 | 洄游+遗传+摄食分析流水?|
| v1.1.0 | 2026-06-05 | 三角核心桥接（IProjectAdapter），orchestrator 任务路由 |
| v1.0.0 | 2026-06-01 | 初始鲚属智能体框架，文献搜索 |

---

## 🪞 自我评估

| 维度 | 评级 | 说明 |
|------|:---:|------|
| 🔬 领域深度 | ⭐⭐⭐⭐?| 4 种鲚?YAML 物种档案 |
| 📡 三角集成 | ⭐⭐⭐⭐?| 直接读写鱼类生态知识库 |
| 🧠 认知架构 | ⭐⭐⭐⭐?| ReAct 循环迭代分析 |
| 🧪 测试覆盖 | ⭐⭐⭐⭐?| 144 项测试覆?8 脚本 |
| 🚀 可扩展?| ⭐⭐⭐⭐?| 添加物种 = ?YAML 文件 |

### 优势
- **分类聚焦**：深度专精鲚属——耳石微化学、洄游生态、遗传学
- **三角赋能**? 个脚本均可从鱼类生态知识库拉取数据并通过认知搜索引擎验证发现
- **SpeciesRegistry**：可扩展 YAML 设计——添加第 5 种鲚属仅需新建 YAML 文件
- **CLI 一致?*：每个脚本支持相?`--species` 接口进行比较分析
- **跨项目集?*：通过 adapter.py 直接读写鱼类生态助手知识库

### 当前局?- 仅限 4 种鲚属（刀鲚、短颌鲚、凤鲚、七丝鲚）——其他鳀科鱼类未覆盖
- 遗传学流水线方法为框架；实际 RAD-seq/eDNA 处理需外部工具
- 耳石分析假定 LA-ICP-MS 数据格式；EPMA 支持待开?- 单智能体架构（无 porpoise-agent 那样的内?MAS?
### 路线?- [ ] 扩展至全部约 15 种鲚属（含凤鲚复合种解析?- [ ] 直接 LA-ICP-MS 数据导入用于耳石分析
- [ ] 集成种群动态模型（Stock Synthesis 3?- [ ] 多智能体内部架构支持并行分析工作?
---

## 🔗 生态体?
本项目是「三生万物」生态的 **刀鲚领域专家（P₂）**?
```
三角核心 + 衍生架构（由 eon-core 协调）：

  S/V0  📦 fish-ecology-assistant    ?知识供给
  V/V1  🔍 cognitive-search-engine   ?搜索验证
  Coord ⚙ eon-core                  ?协调内核

  P?   🐬 porpoise-agent           ?江豚专家
  P?   🐟 coilia-agent             ?刀鲚专??本项?  P?   🐟 culter-agent             ?鲌类专家
  C     🔥 conflict-arbiter         ?冲突仲裁
```

> 🔥 和则无穷力量，分则顶尖专家引擎?
---

## 📋 README 变更日志

| 版本 | 日期 | 主题 | 变更内容 |
|------|------|------|----------|
| v8.0 | 2026-06-20 | README 恢复 | 恢复归档，重新添加徽章，深层结构 |
| v7.0 | 2026-06-19 | 自我评估改版 | 星级评分，结构化优势/局?路线?|
| v6.0 | 2026-06-18 | 生态图?| 添加完整三角核心 + 衍生图表，跨项目链接 |
| v5.0 | 2026-06-17 | v1.4.0 同步 | 分析脚本文档?44 测试，SpeciesRegistry 文档 |
| v4.0 | 2026-06-14 | 哲学章节 | 三谛?何以重要"对比?|
| v3.0 | 2026-06-10 | 架构深度解析 | 内部架构树，三角核心 + 衍生角色 |
| v2.0 | 2026-06-05 | 快速入门充?| CLI 示例，物种专属命?|
| v1.0.0 | 2026-06-01 | 初稿 | 项目概述，基本结构，功能?|

---

🌱 **万物皆变 · Panta Rhei**

> > 赫拉克利特说：人不能两次踏进同一条河流。
> 
> 知识会老去，但人类对世界的追问永不落幕。
> 
> 昨日之真理为今日之基石，今日之未知为明日之征途。
> 
> 我们的目光，从不囿于已知的疆界；我们的脚步，终将踏上那片星光璀璨的浩瀚征途。这个项目不是一套固定的工具集——它是一?*活的系统**。每个组件都内置了过期机制、版本追踪和涌现感知。随着你的研究深入、R包更新、新方法涌现，它会和你一起进化?
*最后更新：2026-06-20　|　适用环境：Reasonix Code · DeepSeek 驱动*
