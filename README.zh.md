<div align="center">

```
╔══════════════════════════════════════════════════════════════╗
║   🐟  COILIA AGENT  ·  P₂ 刀鲚专研  ·  v1.4.0                ║
║  ─────────────────────────────────────────────────────────  ║
║    耳石微化学 · 洄游生态 · 资源评估 · 种群遗传学                ║
║        刀鲚 · Coilia nasus · 4 种鲚属                          ║
╚══════════════════════════════════════════════════════════════╝
```

<p align="center">
  🇬🇧 <a href="README.md">English</a>  ·  🇨🇳 <a href="README.zh.md">中文</a>
</p>

[![Python 3.10+](https://img.shields.io/badge/Python%203.10%2B-3776AB?style=flat-square)]()
[![v1.4.0](https://img.shields.io/badge/v1.4.0-8A4FCE?style=flat-square)]()
[![4 species](https://img.shields.io/badge/4%20species-007EC6?style=flat-square)]()
[![144 tests](https://img.shields.io/badge/144%20tests-D73A4A?style=flat-square)]()
[![ReAct](https://img.shields.io/badge/ReAct%20Loop-0EA5E9?style=flat-square)]()
[![Triangle](https://img.shields.io/badge/Triangle%20Powered-EC4899?style=flat-square)]()

<p align="center">
  <a href="https://github.com/fangtaocai041/coilia-agent/stargazers"><img src="https://img.shields.io/github/stars/fangtaocai041/coilia-agent?style=social" alt="Stars"></a>
  <a href="https://github.com/fangtaocai041/coilia-agent/network/members"><img src="https://img.shields.io/github/forks/fangtaocai041/coilia-agent?style=social" alt="Forks"></a>
</p>

<div align="center"><h3>🌊 万物皆流。</h3></div>

</div>

---

## 📑 目录

- [🧠 核心哲学](#-核心哲学)
- [🧩 项目定位](#-项目定位)
- [🔺 三角核心 + 衍生角色](#-三角核心--衍生角色)
- [🚀 快速开始](#-快速开始)
- [🏗️ 内部架构](#-内部架构)
- [✨ 核心特性](#-核心特性)
- [📊 分析脚本](#-分析脚本)
- [📜 版本历史](#-版本历史)
- [🪞 自我评价](#-自我评价)

---

## 🧠 核心哲学

> 🌍 世界是动态的，📖 知识是暂时的，🌟 涌现是常态。

### 📜 三大信条

**🌍 世界是动态的** — 刀鲚的洄游路线随气候变化而调整。今天的产卵场可能不是明天的。耳石 Sr/Ca 比值记录的是特定年份的环境条件。

**📖 知识是暂时的** — 资源评估模型需要每年用最新 CPUE 数据重新校准。昨天的资源量估算不能用于今天的管理决策。

**🌟 涌现是常态** — 当耳石微化学数据、捕捞日志、环境 DNA 三个独立来源指向同一洄游模式变化时，系统标记为涌现信号。

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

## 🧩 项目定位

**Coilia Agent** 是三生万物生态体系中 P₂ 衍生项目。作为刀鲚领域的专属智能体，专精于耳石微化学分析（Sr/Ca）、洄游生态重建和资源评估。

覆盖 4 种鲚属鱼类，8 个分析脚本，144 测试全覆盖。

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

## 🔺 三角核心 + 衍生角色

| 项目 | 层级 | 角色 |
|------|:----:|------|
| fish-ecology-assistant | 三角 S/V0 | 知识供给 |
| cognitive-search-engine | 三角 V/V1 | 搜索验证 |
| eon-core | Coord | 协调中枢 |
| porpoise-agent | 衍生 P₁ | 江豚专研 |
| **coilia-agent** | **衍生 P₂** | **刀鲚专研** |
| culter-agent | 衍生 P₃ | 鲌类专研 |
| conflict-arbiter | 衍生 C | 冲突仲裁 |

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

## 🚀 快速开始

```bash
git clone https://github.com/fangtaocai041/coilia-agent.git
cd coilia-agent
pip install -e .
```

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

## 🏗️ 内部架构

| 模块 | 功能 |
|------|------|
| `otolith/` | 耳石 Sr/Ca 微化学分析 |
| `migration/` | 洄游生态重建模型 |
| `stock/` | CPUE 资源评估 |
| `scripts/` | 8 个可执行分析脚本 |

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

## ✨ 核心特性

<details open><summary><b>📋 特性列表</b></summary>

| 特性 | 状态 | 说明 |
|------|:----:|------|
| 🔬 耳石微化学 | ✅ | Sr/Ca 比值 LA-ICP-MS 数据分析 |
| 🐟 洄游生态 | ✅ | 淡水-河口-海洋生活史重建 |
| 📊 资源评估 | ✅ | CPUE 标准化 + 种群动态模型 |
| 🌐 多物种 | ✅ | 4 种鲚属（*C. nasus*、*C. mystus*、*C. grayii*、*C. brachygnathus*） |
| 🧪 测试 | ✅ | 144 测试全覆盖 |

</details>

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

## 📊 分析脚本

| 脚本 | 功能 |
|------|------|
| `otolith_analysis.py` | 耳石 Sr/Ca 剖面分析 |
| `migration_reconstruct.py` | 洄游路线重建 |
| `cpue_standardize.py` | CPUE 标准化 |
| `stock_assessment.py` | 资源评估模型 |
| `habitat_suitability.py` | 栖息地适宜性建模 |
| `data_pipeline.py` | 数据预处理管线 |
| `cross_validation.py` | 跨项目验证 |
| `report_generator.py` | 报告生成 |

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

## 📜 版本历史

| 版本 | 日期 | 主题 |
|------|------|------|
| **v1.4.0** | 2026-06-18 | 4 物种 + 144 测试 + 跨项目验证 |
| **v1.3.0** | 2026-06-12 | 栖息地适宜性建模 |
| **v1.2.0** | 2026-06-07 | 三角核心集成 + ReAct 循环 |
| **v1.0.0** | 2026-06-05 | 初始发布 · 耳石微化学分析 |

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

## 🪞 自我评价

**优势**：耳石微化学分析国内最早开源实现之一；4 物种并行分析；144 测试全通过。

**局限**：依赖 LA-ICP-MS 实验数据（非实时）；洄游模型需现场验证数据校准。

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

---

> **"不要搜索字符串，要重建所指。"**
> Don't search for strings — reconstruct the signified.

---

## 🌱 万物皆变 · Panta Rhei

> 赫拉克利特说：人不能两次踏进同一条河流。
>
> 我们说：知识会老去，但人类对世界的追问永不落幕。昨日之真理为今日之基石，今日之未知为明日之征途。我们的目光，从不囿于已知的疆界；我们的脚步，终将踏上那片星光璀璨的浩瀚征途。

这个项目不是一套固定的工具集——它是一个**活的系统**。


> 🔧 Agent 约束: [AGENTS.md](../AGENTS.md) · [core-constitution.md](../.reasonix/core-constitution.md) · [research-first](../skills/research-first.md) · [retro-session](../skills/retro-session.md)

*最后更新: 2026-06-18 | Reasonix Code · DeepSeek 驱动*

---

<div align="center">

### 🏷️ 技术标签

`刀鲚` `耳石微化学` `洄游生态` `资源评估` `稳定同位素` `遗传学` `ReAct循环` `物种注册` `长江` `渔业` `Reasonix` `MCP`

<br>

<sub>🐟 属于 **三生万物** 生态体系 · P₂ 衍生专研 · 由 [eon-core](https://github.com/fangtaocai041/eon-core) 统一协调</sub>

</div>
