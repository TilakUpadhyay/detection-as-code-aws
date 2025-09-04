from __future__ import annotations

from .core import BaseCompiler
from ..models import Rule


class AthenaCompiler(BaseCompiler):
	def compile(self, rule: Rule) -> str:
		template = self.env.get_template("athena/query.j2")
		condition = self.translator.to_athena(rule.detection.condition)
		return template.render(rule=rule, condition=condition) 