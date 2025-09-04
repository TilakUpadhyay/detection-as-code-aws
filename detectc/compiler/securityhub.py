from __future__ import annotations

import json

from .core import BaseCompiler
from ..models import Rule


class SecurityHubCompiler(BaseCompiler):
	def compile(self, rule: Rule) -> str:
		template = self.env.get_template("securityhub/insight.j2")
		condition = self.translator.to_securityhub(rule.detection.condition)
		payload = template.render(rule=rule, condition=condition)
		# Ensure valid JSON output formatting
		obj = json.loads(payload)
		return json.dumps(obj, indent=2) 