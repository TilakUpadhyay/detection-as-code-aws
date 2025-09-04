from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Any

import yaml

from .models import Rule


class RuleParser:
	@staticmethod
	def load_rule(path: str | Path) -> Rule:
		p = Path(path)
		if not p.exists():
			raise FileNotFoundError(f"Rule file not found: {p}")

		text = p.read_text(encoding="utf-8")
		if p.suffix.lower() in {".yml", ".yaml"}:
			data: Dict[str, Any] = yaml.safe_load(text)
		elif p.suffix.lower() == ".json":
			data = json.loads(text)
		else:
			raise ValueError("Unsupported rule file format. Use .yaml/.yml or .json")

		return Rule.from_dict(data) 