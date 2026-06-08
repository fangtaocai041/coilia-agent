# 🐟 Coilia Agent — 刀鲚专研 (P₂)

> **物种**: 刀鲚 (*Coilia nasus*) — 长江三鲜之首，溯河洄游鱼类
> **课题组**: 淡水渔业研究中心 刘凯研究员
> **角色**: P₂ — S-T-V-P₁-P₂ 五体架构中的刀鲚专研层
> **同级**: porpoise-agent (P₁, 长江江豚) | **协调**: meso-cosmos-agent (T)
> **版本**: v1.2.0 | **状态**: ✅ 运行中

## 研究背景

刀鲚（长江刀鱼）是长江流域最重要的经济鱼类之一，也是"长江三鲜"之首。
由于过度捕捞、水利工程阻断洄游通道、栖息地退化，刀鲚资源量急剧下降。
2019年起农业农村部停止发放刀鲚专项捕捞许可证，2021年长江十年禁捕全面实施。

## 🔗 生态系统

| 项目 | 角色 | 说明 |
|------|:--:|------|
| [meso-cosmos-agent](https://github.com/fangtaocai041/meso-cosmos-agent) | **T** | 执行中枢 — 路由刀鲚查询到本 Agent |
| [porpoise-agent](https://github.com/fangtaocai041/porpoise-agent) | **P₁** | 姊妹 Agent — 长江江豚专研 (同课题组) |
| [fish-ecology-assistant](https://github.com/fangtaocai041/fish-ecology-assistant) | **S** | 知识供给 — 长江 443 种鱼类数据库 |
| [cognitive-search-engine](https://github.com/fangtaocai041/cognitive-search-engine) | **V** | 验证引擎 — 文献搜索 + 三角验证 |

## 核心研究方向

| 方向 | 说明 |
|------|------|
| 🧬 群体遗传学 | 刀鲚洄游群体遗传结构、地理种群分化 |
| 🏷️ 耳石微化学 | Sr/Ca比分析洄游履历、生境履历重建 |
| 📐 形态学 | 刀鲚与近缘种(短颌鲚、凤鲚)的形态鉴别 |
| 🌊 洄游生态 | 溯河洄游路线、时间节律、环境驱动因子 |
| 📊 资源评估 | 禁捕后资源恢复监测、种群动态模型 |
| 🍽️ 食性分析 | 刀鲚摄食生态、营养级位置 |

## 📊 自我评价

| 维度 | 评分 | 说明 |
|------|:--:|------|
| 🐟 领域深度 | ⭐⭐⭐⭐⭐ | 刀鲚完整知识库：生物学、洄游特性、耳石微化学、资源评估 |
| 🔬 研究方法 | ⭐⭐⭐⭐☆ | 3 个核心 Skill 定义完整 (文献检索/洄游分析/资源评估) |
| 🔗 生态位整合 | ⭐⭐⭐⭐⭐ | P₂ 角色，与 P₁(江豚) 平级，统一由 meso-cosmos (T) 调度 |
| 📡 可执行性 | ⭐⭐⭐☆☆ | 当前为 delegation stub 架构，实际搜索需通过 Reasonix Skills 执行 |
| 🚀 可扩展性 | ⭐⭐⭐⭐⭐ | 与 porpoise-agent 共享 P 层模板，3 步复制出新物种 Agent |

> **核心优势**: 长江刀鲚（三鲜之首）专属研究 Agent。与 P₁ 江豚 Agent 共享刘凯研究员课题组方向，形成长江水生生物"豚-鱼"双专研体系。
> **待改进**: Skills 从 delegation stub 升级为可执行搜索逻辑。

## 快速开始

```bash
cd coilia-agent
pip install -e .
coilia run --query "刀鲚洄游路线 长江"
```
