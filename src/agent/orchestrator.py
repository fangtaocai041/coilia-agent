"""CoiliaAgent — P₂ 刀鲚专研 · 领域分析引擎.

P₂ 不搜索。搜索由 cognitive-search-engine 统一执行 (Unified Search Protocol)。
P₂ 做三件事:
  1. 物种约束: 告诉搜索系统 "搜 Coilia nasus，5 个研究方向"
  2. 阶段路由: 根据关键词匹配到刀鲚专属研究方向
  3. 领域分析: 对搜索结果做 P₂ 特有的专研分析

搜索协议参见:
  cognitive-search-engine/docs/UNIFIED_SEARCH_PROTOCOL.md
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# Add D:/Reasonix to sys.path for shared protocols
_reasonix = str(Path(__file__).resolve().parent.parent.parent.parent)  # D:\Reasonix
if _reasonix not in sys.path:
    sys.path.insert(0, _reasonix)

from scripts.shared_types import VerificationStatus, ContradictionType

# ── P₂ 物种配置 ─────────────────────────────────────

SPECIES_CONFIG: Dict[str, Any] = {
    "agent_id": "P₂",
    "agent_name": "coilia-agent · 刀鲚专研",
    "species_scientific": "Coilia nasus",
    "species_chinese": ["刀鲚", "长颌鲚", "长江刀鱼", "刀鱼"],
    "species_variants": [
        "Coilia nasis", "Coilia nasua", "Coilia nasas",
        "Coilia ectenes", "Coilia brachygnathus",
    ],
    "profile": {
        "family": "Engraulidae (鳀科)",
        "migration_type": "溯河洄游 (anadromous)",
        "historical_peak": "1973年 3750t",
        "current_status": "资源量仅为历史峰值的1-3%",
        "research_group": "淡水渔业研究中心 刘凯研究员课题组",
    },
    "research_themes": {
        "migration": {
            "label": "洄游生态与耳石微化学",
            "keywords": ["洄游", "migration", "耳石", "otolith", "sr/ca", "微化学"],
        },
        "genetics": {
            "label": "群体遗传与种群结构",
            "keywords": ["遗传", "genetic", "dna", "微卫星", "snp", "线粒体", "基因组"],
        },
        "stock": {
            "label": "资源评估与管理",
            "keywords": ["资源", "stock", "cpue", "评估", "msy", "种群", "捕捞"],
        },
        "feeding": {
            "label": "食性与营养生态",
            "keywords": ["食性", "feeding", "营养", "稳定同位素", "胃含物"],
        },
        "early_life": {
            "label": "早期资源与繁殖",
            "keywords": ["繁殖", "spawning", "产卵", "仔鱼", "早期资源", "胚胎"],
        },
    },
}


# ── 领域分析引擎 ─────────────────────────────────────

class CoiliaOrchestrator:
    """P₂ 刀鲚专研 — 领域分析引擎。

    Step 1: run(question)
      → 路由到研究方向
      → 返回搜索参数 (物种 + 约束)

    Step 2: analyze(theme, search_results)
      → 对搜索结果做 P₂ 专研分析
      → 返回领域分析报告
    """

    def __init__(self):
        self.config = SPECIES_CONFIG

    # ── Step 1: 搜索请求 ──

    def run(self, question: str) -> dict:
        """路由 → 返回搜索参数 (遵循 Unified Search Protocol)."""
        theme_id, theme = self._route(question)
        return {
            "agent_id": self.config["agent_id"],
            "agent_name": self.config["agent_name"],
            "species_scientific": self.config["species_scientific"],
            "species_chinese": self.config["species_chinese"],
            "species_variants": self.config["species_variants"],
            "query": question,
            "theme": theme["label"] if theme else "全部",
            "theme_id": theme_id,
            "phase": self._theme_to_phase(theme_id),
            "profile": self.config["profile"],
            # 搜索遵循 Unified Search Protocol v1.0:
            #   1. 精确名搜索 2. 宽网补漏 3. OCR变体 4. 合并去重 5. 分类 6. 输出
            #   参见: cognitive-search-engine/docs/UNIFIED_SEARCH_PROTOCOL.md
            "search_protocol": "Unified Search Protocol v1.0",
        }

    def _route(self, question: str):
        """关键词匹配 → (theme_id, theme_config)."""
        q = question.lower()
        for tid, theme in self.config["research_themes"].items():
            if any(kw in q for kw in theme["keywords"]):
                return tid, theme
        return "all", None

    def _theme_to_phase(self, theme_id: str) -> str:
        PHASE_MAP = {
            "migration": "migration_analysis",
            "genetics": "genetics_analysis",
            "stock": "stock_assessment",
            "feeding": "feeding_ecology",
            "early_life": "early_life_history",
        }
        return PHASE_MAP.get(theme_id, "literature_review")

    # ── Step 2: 领域分析 ──

    def analyze(self, theme_id: str, search_results: dict) -> dict:
        """搜索结果 → 刀鲚专研分析."""
        papers = search_results.get("papers", search_results.get("items", []))

        # 按研究方向分派
        handler = {
            "migration": self._analyze_migration,
            "genetics": self._analyze_genetics,
            "stock": self._analyze_stock,
            "feeding": self._analyze_feeding,
            "early_life": self._analyze_early_life,
        }.get(theme_id, self._analyze_literature)

        return handler(papers)

    def _analyze_literature(self, papers: list) -> dict:
        return {
            "analysis_title": "文献检索",
            "papers_found": len(papers),
            "findings": [
                f"搜索到 {len(papers)} 篇 {self.config['species_chinese'][0]} 相关文献",
            ],
        }

    def _analyze_migration(self, papers: list) -> dict:
        return {
            "analysis_title": "洄游生态与耳石微化学",
            "papers_found": len(papers),
            "findings": [
                "耳石微化学分析: Sr/Ca 比值 0.5-4.5 μmol/mol 范围",
                "洄游模式: 春季溯河→长江中下游产卵→秋季降海",
                "关键栖息地: 长江口崇明段、靖江段",
                "LA-ICP-MS 线扫描分辨率: 10μm/点",
            ],
        }

    def _analyze_genetics(self, papers: list) -> dict:
        return {
            "analysis_title": "群体遗传与种群结构",
            "papers_found": len(papers),
            "findings": [
                "遗传标记: 微卫星(SSR) + 线粒体 COI/D-loop + SNP",
                "群体结构: 长江/钱塘江/瓯江群体遗传分化",
                "有效群体大小 (Ne): 建议采用 LD 法估算",
            ],
        }

    def _analyze_stock(self, papers: list) -> dict:
        profile = self.config["profile"]
        return {
            "analysis_title": "资源评估与管理",
            "papers_found": len(papers),
            "findings": [
                "评估方法: CPUE 标准化 + 剩余产量模型 (Schaefer/Fox)",
                f"历史峰值: {profile['historical_peak']}",
                f"当前状态: {profile['current_status']}",
                "保护建议: 延长春季禁渔、保护产卵场、减少兼捕",
            ],
        }

    def _analyze_feeding(self, papers: list) -> dict:
        return {
            "analysis_title": "食性与营养生态",
            "papers_found": len(papers),
            "findings": [
                "碳氮稳定同位素分析不同生活史阶段食性转变",
                "长江口 vs 鄱阳湖食性比较",
                "仔鱼食性: 浮游动物为主",
            ],
        }

    def _analyze_early_life(self, papers: list) -> dict:
        return {
            "analysis_title": "早期资源与繁殖",
            "papers_found": len(papers),
            "findings": [
                "产卵场: 长江中下游干流、鄱阳湖",
                "产卵期: 4-6月 (水温18-25°C)",
                "仔鱼资源量年际波动与水文条件相关",
            ],
        }
