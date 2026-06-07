"""
Coilia Agent Orchestrator — 刀鲚专研管线协调器 (P₂)

轻量级——核心协调由 meso-cosmos-agent (T) 负责，
本 orchestrator 只处理刀鲚领域特定逻辑。
"""

from dataclasses import dataclass, field
from enum import Enum


class ResearchPhase(str, Enum):
    LITERATURE = "literature_review"
    MIGRATION = "migration_analysis"
    GENETICS = "genetics_analysis"
    STOCK = "stock_assessment"
    REPORT = "report_generation"


@dataclass
class ResearchContext:
    question: str
    phase: ResearchPhase = ResearchPhase.LITERATURE


class CoiliaOrchestrator:
    """刀鲚专研轻量级编排器——领域路由 + 委托执行"""

    PHASE_ORDER = [
        ResearchPhase.LITERATURE,
        ResearchPhase.MIGRATION,
        ResearchPhase.GENETICS,
        ResearchPhase.STOCK,
        ResearchPhase.REPORT,
    ]

    def __init__(self):
        self.context: ResearchContext | None = None

    def run(self, question: str) -> dict:
        """入口: 问题 → 路由 → 委托执行"""
        q_lower = question.lower()

        # Phase routing via keyword matching
        if any(kw in q_lower for kw in ["洄游", "migration", "耳石", "otolith", "sr/ca", "微化学"]):
            phase = ResearchPhase.MIGRATION
        elif any(kw in q_lower for kw in ["遗传", "genetic", "dna", "微卫星", "snp", " phylogeny"]):
            phase = ResearchPhase.GENETICS
        elif any(kw in q_lower for kw in ["资源", "stock", "cpue", "评估", "msy", "种群", "abundance"]):
            phase = ResearchPhase.STOCK
        elif any(kw in q_lower for kw in ["报告", "report", "综述", "总结"]):
            phase = ResearchPhase.REPORT
        else:
            phase = ResearchPhase.LITERATURE

        self.context = ResearchContext(question=question, phase=phase)

        return {
            "agent": "Coilia Agent (P₂)",
            "species": "Coilia nasus (刀鲚)",
            "phase": phase.value,
            "skill": self._phase_to_skill(phase),
            "status": "delegated",
            "delegate_message": (
                f"DELEGATE to coilia-agent:\n"
                f"  species: Coilia nasus\n"
                f"  phase: {phase.value}\n"
                f"  question: {question}\n"
                f"  research_group: 淡水渔业研究中心 刘凯研究员课题组"
            ),
        }

    def _phase_to_skill(self, phase: ResearchPhase) -> str:
        mapping = {
            ResearchPhase.LITERATURE: "search-literature",
            ResearchPhase.MIGRATION: "analyze-migration",
            ResearchPhase.GENETICS: "analyze-genetics",
            ResearchPhase.STOCK: "assess-stock",
            ResearchPhase.REPORT: "generate-report",
        }
        return mapping.get(phase, "search-literature")
