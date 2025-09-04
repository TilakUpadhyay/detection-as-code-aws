from pathlib import Path

from detectc.parser import RuleParser
from detectc.cli import _templates_env
from detectc.compiler.core import ConditionTranslator
from detectc.compiler.cloudwatch import CloudWatchCompiler
from detectc.compiler.athena import AthenaCompiler
from detectc.compiler.securityhub import SecurityHubCompiler


def test_parse_rule_yaml(tmp_path: Path):
	src = Path(__file__).parents[1] / "detections" / "s3_access_anomaly.yaml"
	rule = RuleParser.load_rule(src)
	assert rule.id == "s3_access_anomaly"
	assert rule.output.cloudwatch and rule.output.athena and rule.output.securityhub


def test_compile_all_targets(tmp_path: Path):
	src = Path(__file__).parents[1] / "detections" / "s3_access_anomaly.yaml"
	rule = RuleParser.load_rule(src)
	env = _templates_env()
	translator = ConditionTranslator()

	cw = CloudWatchCompiler(env, translator).compile(rule)
	ath = AthenaCompiler(env, translator).compile(rule)
	sh = SecurityHubCompiler(env, translator).compile(rule)

	assert "filter" in cw
	assert "SELECT" in ath
	assert "Filters" in sh 