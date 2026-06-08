"""
Coilia Agent Orchestrator — 刀鲚专研管线协调器 (P₂)

双模式运行:
  独立模式 (standalone): 作为独立 Agent 运行，内置物种知识 + 搜索策略建议
  集成模式 (integrated):   由 meso-cosmos-agent (T) 调度，返回 DELEGATE 协议消息
"""

from dataclasses import dataclass
from enum import Enum
import os


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
    """刀鲚专研轻量级编排器 — 双模式: 独立/集成"""

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
        """入口: 问题 → 路由 → 执行 (独立/集成双模式)

        独立模式: coilia-agent 作为独立 Agent 运行，内置基础搜索建议
        集成模式: 由 meso-cosmos-agent (T) 调度，返回 DELEGATE 协议消息
        """
        q_lower = question.lower()

        # Detect operating mode
        base = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        meso_available = os.path.isdir(os.path.join(base, "meso-cosmos-agent"))
        mode = "integrated" if meso_available else "standalone"

        # Phase routing
        if any(kw in q_lower for kw in ["洄游", "migration", "耳石", "otolith", "sr/ca", "微化学"]):
            phase = ResearchPhase.MIGRATION
        elif any(kw in q_lower for kw in ["遗传", "genetic", "dna", "微卫星", "snp"]):
            phase = ResearchPhase.GENETICS
        elif any(kw in q_lower for kw in ["资源", "stock", "cpue", "评估", "msy", "种群"]):
            phase = ResearchPhase.STOCK
        elif any(kw in q_lower for kw in ["报告", "report", "综述", "总结"]):
            phase = ResearchPhase.REPORT
        else:
            phase = ResearchPhase.LITERATURE

        self.context = ResearchContext(question=question, phase=phase)

        if mode == "standalone":
            return self._standalone_response(question, phase)
        else:
            return self._integrated_response(question, phase)

    def _standalone_response(self, question: str, phase: ResearchPhase) -> dict:
        """独立模式: 返回内置分析 + 搜索建议。"""
        return {
            "agent": "Coilia Agent (P₂) — Standalone",
            "species": "Coilia nasus (刀鲚/长江刀鱼)",
            "phase": phase.value,
            "skill": self._phase_to_skill(phase),
            "mode": "standalone",
            "status": "analyzed",
            "knowledge": {
                "profile": "溯河洄游鱼类, 长江三鲜之首, 资源量仅为历史峰值(1973年3750t)的1-3%",
                "key_themes": [
                    "耳石微化学 Sr/Ca 洄游履历重建",
                    "群体遗传学 微卫星/线粒体/SNP",
                    "资源评估 CPUE标准化 MSY估算",
                ],
                "suggested_queries": [
                    '"Coilia nasus" migration otolith',
                    '刀鲚 洄游 耳石 微化学',
                    '"Coilia nasus" stock assessment',
                ],
                "research_group": "淡水渔业研究中心 刘凯研究员课题组",
            },
            "note": "Standalone — provides species knowledge + search strategy. Install meso-cosmos-agent for integrated S-T-V-P execution.",
        }

    def _integrated_response(self, question: str, phase: ResearchPhase) -> dict:
        """集成模式: DELEGATE 协议消息。"""
        return {
            "agent": "Coilia Agent (P₂)",
            "species": "Coilia nasus (刀鲚)",
            "phase": phase.value,
            "skill": self._phase_to_skill(phase),
            "mode": "integrated",
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
