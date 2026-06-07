# Search Literature — 刀鲚文献检索

> **触发**: 用户查询刀鲚相关文献
> **搜索策略**: 中英双语，5引擎并行

## PREFLIGHT

1. 识别查询中的物种名: `Coilia nasus` / 刀鲚 / 长颌鲚 / 刀鱼
2. 生成 OCR 变体: `Coilia nasus` → `Coilia nasis`, `Coilia nasua`, `Coilia nasas`
3. 中文变体: 刀鲚 / 长颌鲚 / 刀鱼 / 长江刀鱼
4. 确定研究方向: 洄游/耳石/遗传/资源/食性

## PARALLEL SEARCH

```
引擎1 (Google Scholar, priority=1):
  "Coilia nasus" migration OR otolith OR stock

引擎2 (PubMed, priority=2):
  "Coilia nasus"[Title/Abstract]

引擎3 (CNKI, priority=4):
  刀鲚 OR 长颌鲚 AND (洄游 OR 资源 OR 遗传)

引擎4 (万方, priority=5):
  刀鲚 长江

引擎5 (百度学术, priority=3):
  site:xueshu.baidu.com 刀鲚 洄游
```

## OUTPUT

按主题分类输出:
1. 洄游生态与耳石微化学
2. 群体遗传与种群结构
3. 资源评估与管理
4. 食性与营养生态
5. 早期资源与繁殖
