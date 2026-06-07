#!/usr/bin/env python3
"""Coilia Agent CLI — 刀鲚专研入口"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from src.agent.orchestrator import CoiliaOrchestrator


def main():
    import argparse
    parser = argparse.ArgumentParser(prog="coilia", description="Coilia Agent — 刀鲚专研 (P₂)")
    sub = parser.add_subparsers(dest="command")

    p_run = sub.add_parser("run", help="执行刀鲚研究查询")
    p_run.add_argument("--query", "-q", required=True)

    args = parser.parse_args()
    if args.command == "run":
        orch = CoiliaOrchestrator()
        result = orch.run(args.query)
        print(f"\n{'='*60}")
        print(f"  {result['agent']}")
        print(f"  Species: {result['species']}")
        print(f"  Phase:   {result['phase']}")
        print(f"  Skill:   {result['skill']}")
        print(f"  Status:  {result['status']}")
        print(f"{'='*60}\n")
        print(result['delegate_message'])
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
