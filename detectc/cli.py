from __future__ import annotations

import argparse
from pathlib import Path
from typing import List

from jinja2 import Environment, FileSystemLoader

from .models import Rule
from .parser import RuleParser
from .compiler.core import ConditionTranslator
from .compiler.cloudwatch import CloudWatchCompiler
from .compiler.athena import AthenaCompiler
from .compiler.securityhub import SecurityHubCompiler


def _templates_env() -> Environment:
	base = Path(__file__).parent / "compiler" / "templates"
	return Environment(
		loader=FileSystemLoader(str(base)),
		autoescape=False,
		trim_blocks=True,
		lstrip_blocks=True,
	)


def compile_rule(rule_path: str, targets: List[str], out_dir: str) -> None:
	rule: Rule = RuleParser.load_rule(rule_path)
	env = _templates_env()
	translator = ConditionTranslator()

	out = Path(out_dir)
	out.mkdir(parents=True, exist_ok=True)

	selected = set(t.lower() for t in targets)

	if "cloudwatch" in selected or rule.output.cloudwatch:
		compiler = CloudWatchCompiler(env, translator)
		content = compiler.compile(rule)
		(out / f"{rule.id}.cloudwatch.insights").write_text(content + "\n", encoding="utf-8")

	if "athena" in selected or rule.output.athena:
		compiler = AthenaCompiler(env, translator)
		content = compiler.compile(rule)
		(out / f"{rule.id}.athena.sql").write_text(content + "\n", encoding="utf-8")

	if "securityhub" in selected or rule.output.securityhub:
		compiler = SecurityHubCompiler(env, translator)
		content = compiler.compile(rule)
		(out / f"{rule.id}.securityhub.json").write_text(content + "\n", encoding="utf-8")


def main() -> None:
	parser = argparse.ArgumentParser(prog="detectc", description="Detection-as-Code compiler for AWS")
	sub = parser.add_subparsers(dest="cmd", required=True)

	p_compile = sub.add_parser("compile", help="Compile a detection rule to target queries")
	p_compile.add_argument("rule", help="Path to YAML/JSON detection file")
	p_compile.add_argument("--targets", nargs="*", default=[], help="Targets: cloudwatch athena securityhub")
	p_compile.add_argument("--out", default="examples", help="Output directory for compiled queries")

	args = parser.parse_args()

	if args.cmd == "compile":
		compile_rule(args.rule, args.targets, args.out)
	else:
		parser.print_help()


if __name__ == "__main__":
	main() 