from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class OutputTargets:
	cloudwatch: bool = False
	athena: bool = False
	securityhub: bool = False


@dataclass
class DetectionLogic:
	condition: str


@dataclass
class Rule:
	title: str
	id: str
	description: str
	logsource: str
	detection: DetectionLogic
	output: OutputTargets
	tags: Dict[str, Any] = field(default_factory=dict)

	@staticmethod
	def from_dict(data: Dict[str, Any]) -> "Rule":
		title = data.get("title")
		id_ = data.get("id")
		description = data.get("description", "")
		logsource = data.get("logsource")
		detection_block = data.get("detection", {})
		output_block = data.get("output", {})

		if not title or not id_ or not logsource or "condition" not in detection_block:
			raise ValueError("Rule must include title, id, logsource, and detection.condition")

		detection = DetectionLogic(condition=str(detection_block["condition"]))
		output = OutputTargets(
			cloudwatch=bool(output_block.get("cloudwatch", False)),
			athena=bool(output_block.get("athena", False)),
			securityhub=bool(output_block.get("securityhub", False)),
		)

		return Rule(
			title=title,
			id=id_,
			description=description,
			logsource=logsource,
			detection=detection,
			output=output,
			tags=data.get("tags", {}),
		) 