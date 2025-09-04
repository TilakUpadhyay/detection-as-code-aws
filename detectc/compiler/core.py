from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from jinja2 import Environment

from ..models import Rule


class ConditionTranslator:
	"""Very simple translator from a pseudo-expression to target syntax.

	This is intentionally minimal; future versions can include a proper parser
	and mapping per log source and backend.
	"""

	def to_cloudwatch(self, condition: str) -> str:
		return condition.replace(" and ", " and ").replace(" or ", " or ")

	def to_athena(self, condition: str) -> str:
		return (
			condition
			.replace(" and ", " AND ")
			.replace(" or ", " OR ")
			.replace("==", "=")
		)

	def to_securityhub(self, condition: str) -> str:
		return condition


class Compiler(Protocol):
	def compile(self, rule: Rule) -> str:  # pragma: no cover - interface
		...


@dataclass
class BaseCompiler:
	env: Environment
	translator: ConditionTranslator 