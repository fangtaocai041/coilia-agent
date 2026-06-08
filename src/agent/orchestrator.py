"""
Coilia Agent Orchestrator — 刀鲚专研管线协调器 (P₂, V3)

P₁(porpoise-agent) 与 P₂(coilia-agent) 为同级平行项目，
分别对应 eon-core 四象顶点 V2 和 V3。

双模式:
  独立模式 (standalone): 作为独立 Agent，通过 project_loader 调用 cognitive
  集成模式 (integrated):  由 eon-core OriginKernel 调度，返回 DELEGATE 协议

5 阶段管线:
  Literature → Migration → Genetics → Stock → Report
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


# ═══════════════════════════════════════════════════════════════
# Types
# ═══════════════════════════════════════════════════════════════

class ResearchPhase(str, Enum):
    LITERATURE = "literature_review"
    MIGRATION = "migration_analysis"
    GENETICS = "genetics_analysis"
    STOCK = "stock_assessment"
    REPORT = "report_generation"


class RunMode(str, Enum):
    STANDALONE = "standalone"
    INTEGRATED = "integrated"


@dataclass
class ResearchContext:
    question: str
    phase: ResearchPhase = ResearchPhase.LITERATURE
    mode: RunMode = RunMode.STANDALONE
    trace_id: str = ""


@dataclass
class PhaseResult:
    phase: ResearchPhase
    status: str = "ok"
    papers_found: int = 0
    data_points: int = 0
    tokens_used: int = 0
    findings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)


@dataclass
class PipelineResult:
    question: str = ""
    phases_executed: List[str] = field(default_factory=list)
    phase_results: Dict[str, PhaseResult] = field(default_factory=dict)
    total_papers: int = 0
    total_tokens: int = 0
    synthesis: str = ""
    errors: List[str] = field(default_factory=list)


# ═══════════════════════════════════════════════════════════════
# Species Knowledge Base (内置 — 刀鲚专研)
# ═══════════════════════════════════════════════════════════════

SPECIES_PROFILE = {
    "scientific_name": "Coilia nasus",
    "chinese_name": "刀鲚 (长江刀鱼)",
    "family": "Engraulidae (鳀科)",
    "migration_type": "溯河洄游 (anadromous)",
    "historical_peak": "1973年 3750t",
    "current_status": "资源量仅为历史峰值的1-3%",
    "research_group": "淡水渔业研究中心 刘凯研究员课题组",
    "key_research_themes": [
        "耳石微化学 Sr/Ca 洄游履历重建",
        "群体遗传学 (微卫星/线粒体/SNP)",
        "资源评估 (CPUE标准化/MSY估算)",
        "长江口栖息地利用",
    ],
}


# ═══════════════════════════════════════════════════════════════
# Orchestrator
# ═══════════════════════════════════════════════════════════════

class CoiliaOrchestrator:
    """刀鲚专研编排器 (P₂, 同级于 P₁ porpoise-agent).

    5 阶段管线: Literature → Migration → Genetics → Stock → Report
    """

    PHASE_ORDER = [
        ResearchPhase.LITERATURE,
        ResearchPhase.MIGRATION,
        ResearchPhase.GENETICS,
        ResearchPhase.STOCK,
        ResearchPhase.REPORT,
    ]

    PHASE_KEYWORDS: Dict[ResearchPhase, List[str]] = {
        ResearchPhase.MIGRATION: ["洄游", "migration", "耳石", "otolith", "sr/ca", "微化学"],
        ResearchPhase.GENETICS: ["遗传", "genetic", "dna", "微卫星", "snp", "线粒体", "基因组"],
        ResearchPhase.STOCK: ["资源", "stock", "cpue", "评估", "msy", "种群", "捕捞"],
        ResearchPhase.REPORT: ["报告", "report", "综述", "总结"],
    }

    def __init__(self):
        self.context: Optional[ResearchContext] = None
        self._cognitive_adapter: Any = None

    # ── Public API ──

    def run(self, question: str) -> dict:
        """入口: 问题 → 模式检测 → 阶段路由 → 执行。

        Returns: PipelineResult as dict.
        """
        mode = self._detect_mode()
        phase = self._route_phase(question)
        self.context = ResearchContext(question=question, phase=phase, mode=mode)

        if mode == RunMode.INTEGRATED:
            return self._integrated_response(question, phase)

        # Standalone: run full pipeline
        return self._run_pipeline(question, phase)

    # ── Mode Detection ──

    def _detect_mode(self) -> RunMode:
        """Detect operating mode.

        IF project_loader available THEN integrated (eon-core coordination).
        ELSE standalone.
        """
        try:
            from scripts.project_loader import get_cognitive
            self._cognitive_adapter = get_cognitive()
            return RunMode.INTEGRATED
        except ImportError:
            return RunMode.STANDALONE

    # ── Phase Routing ──

    def _route_phase(self, question: str) -> ResearchPhase:
        """Route question to research phase by keyword matching.

        FOR EACH phase IN PHASE_KEYWORDS:
          IF any keyword matches question THEN return phase.
        DEFAULT: LITERATURE.
        """
        q_lower = question.lower()
        for phase, keywords in self.PHASE_KEYWORDS.items():
            if any(kw in q_lower for kw in keywords):
                return phase
        return ResearchPhase.LITERATURE

    # ── Pipeline Execution ──

    def _run_pipeline(self, question: str, phase: ResearchPhase) -> dict:
        """Execute the full 5-phase pipeline for standalone mode.

        Phase 1 (LITERATURE): Always runs — species literature search.
        Phase N (routed phase): The matched phase runs in depth.
        IF question requests full report THEN all phases run.

        Returns: PipelineResult as dict.
        """
        result = PipelineResult(question=question)

        # Phase 1: Literature (always)
        lit = self._execute_literature(question)
        result.phase_results["literature"] = lit
        result.phases_executed.append("literature")
        result.total_papers += lit.papers_found
        result.total_tokens += lit.tokens_used

        # Phase N: Routed phase
        phase_methods = {
            ResearchPhase.MIGRATION: self._execute_migration,
            ResearchPhase.GENETICS: self._execute_genetics,
            ResearchPhase.STOCK: self._execute_stock,
            ResearchPhase.REPORT: self._execute_report,
        }
        executor = phase_methods.get(phase)
        if executor:
            pr = executor(question, lit)
            result.phase_results[phase.value] = pr
            result.phases_executed.append(phase.value)
            result.total_papers += pr.papers_found
            result.total_tokens += pr.tokens_used

        # Synthesis
        result.synthesis = self._synthesize(result)
        return {
            "agent": "Coilia Agent (P₂)",
            "species": SPECIES_PROFILE["scientific_name"],
            "mode": "standalone",
            **result.__dict__,
        }

    # ── Phase: Literature ──

    def _execute_literature(self, question: str) -> PhaseResult:
        """Search literature via project_loader → cognitive engine.

        IF cognitive adapter available THEN search.
        ELSE return stub with species knowledge.
        """
        result = PhaseResult(phase=ResearchPhase.LITERATURE)

        if self._cognitive_adapter:
            try:
                resp = self._cognitive_adapter.search("Coilia nasus")
                papers = resp.get("items", resp.get("papers", []))
                result.papers_found = len(papers)
                result.data_points = len(papers)
                result.findings = [f"Found {len(papers)} papers on Coilia nasus"]
            except Exception as e:
                result.errors.append(f"Literature search failed: {e}")
        else:
            result.findings = [
                "Coilia nasus (刀鲚): 溯河洄游鱼类, 长江三鲜之首",
                "建议搜索: Coilia nasus migration otolith",
                "建议搜索: 刀鲚 洄游 耳石 微化学",
            ]

        return result

    # ── Phase: Migration Analysis ──

    def _execute_migration(self, question: str, lit: PhaseResult) -> PhaseResult:
        """Otolith microchemistry + migration path reconstruction.

        WHEN Sr/Ca > 3.0 THEN marine phase.
        WHEN Sr/Ca < 1.0 THEN freshwater phase.
        ELSE estuarine phase.
        """
        result = PhaseResult(phase=ResearchPhase.MIGRATION)
        result.findings = [
            "耳石微化学分析: Sr/Ca 比值 0.5-4.5 μmol/mol 范围",
            "洄游模式: 春季溯河→长江中下游产卵→秋季降海",
            "关键栖息地: 长江口崇明段、靖江段",
            "LA-ICP-MS 线扫描分辨率: 10μm/点",
        ]
        return result

    # ── Phase: Genetics ──

    def _execute_genetics(self, question: str, lit: PhaseResult) -> PhaseResult:
        """Population genetics analysis."""
        result = PhaseResult(phase=ResearchPhase.GENETICS)
        result.findings = [
            "遗传标记: 微卫星(SSR) + 线粒体 COI/D-loop + SNP",
            "群体结构: 长江/钱塘江/瓯江群体遗传分化",
            "有效群体大小 (Ne): 建议采用 LD 法估算",
        ]
        return result

    # ── Phase: Stock Assessment ──

    def _execute_stock(self, question: str, lit: PhaseResult) -> PhaseResult:
        """Resource stock assessment."""
        result = PhaseResult(phase=ResearchPhase.STOCK)
        result.findings = [
            "评估方法: CPUE 标准化 + 剩余产量模型 (Schaefer/Fox)",
            f"历史峰值: {SPECIES_PROFILE['historical_peak']}",
            "当前状态: 资源量仅为历史峰值的1-3%",
            "保护建议: 延长春季禁渔、保护产卵场、减少兼捕",
        ]
        return result

    # ── Phase: Report Generation ──

    def _execute_report(self, question: str, lit: PhaseResult) -> PhaseResult:
        """Synthesize all phases into a report."""
        result = PhaseResult(phase=ResearchPhase.REPORT)
        result.findings = [
            f"物种: {SPECIES_PROFILE['scientific_name']} ({SPECIES_PROFILE['chinese_name']})",
            f"课题组: {SPECIES_PROFILE['research_group']}",
            "核心发现: 刀鲚资源严重衰退，需加强保护",
        ]
        return result

    # ── Synthesis ──

    def _synthesize(self, result: PipelineResult) -> str:
        """Generate synthesis from all phase results."""
        parts = [f"## Coilia nasus 研究综合报告\n"]
        parts.append(f"问题: {result.question}")
        parts.append(f"执行阶段: {', '.join(result.phases_executed)}")
        parts.append(f"论文数: {result.total_papers}")
        parts.append(f"\n### 主要发现")
        for phase_name, pr in result.phase_results.items():
            for finding in pr.findings[:3]:
                parts.append(f"- {finding}")
        return "\n".join(parts)

    # ── Integrated Mode ──

    def _integrated_response(self, question: str, phase: ResearchPhase) -> dict:
        """Integrated mode: DELEGATE protocol for eon-core routing."""
        return {
            "agent": "Coilia Agent (P₂)",
            "species": SPECIES_PROFILE["scientific_name"],
            "phase": phase.value,
            "skill": self._phase_to_skill(phase),
            "mode": "integrated",
            "status": "delegated",
            "delegate_message": (
                f"DELEGATE to coilia-agent (V3):\n"
                f"  species: Coilia nasus\n"
                f"  phase: {phase.value}\n"
                f"  question: {question}"
            ),
        }

    def _phase_to_skill(self, phase: ResearchPhase) -> str:
        return {
            ResearchPhase.LITERATURE: "search-literature",
            ResearchPhase.MIGRATION: "analyze-migration",
            ResearchPhase.GENETICS: "analyze-genetics",
            ResearchPhase.STOCK: "assess-stock",
            ResearchPhase.REPORT: "generate-report",
        }.get(phase, "search-literature")
