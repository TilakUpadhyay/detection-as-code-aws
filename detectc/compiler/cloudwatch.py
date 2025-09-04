from __future__ import annotations

from .core import BaseCompiler
from ..models import Rule


class CloudWatchCompiler(BaseCompiler):
	def compile(self, rule: Rule) -> str:
		template = self.env.get_template("cloudwatch/insights.j2")
		condition = self.translator.to_cloudwatch(rule.detection.condition)
		return template.render(rule=rule, condition=condition) 