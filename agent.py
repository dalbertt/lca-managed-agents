# agent.py
#
# Your design studio's agent. Each lab adds to this file: look for the TODOs.
from managed_deepagents import define_deep_agent

from middleware.brand_lint import brand_lint
from tools.brand import get_brand
from tools.slack_tools import publish_design

# TODO (Lab 2): import get_weekly_metrics from tools/data.py.
# TODO (Lab 3): import choose_concept from tools/slack_tools.py.

agent = define_deep_agent(
    name="design-studio",
    model="openai:gpt-5.5",
    tools=[get_brand, publish_design],
    interrupt_on={"publish_design": True},
    middleware=[brand_lint],
    # TODO (Lab 1): add the critic subagent.
)
