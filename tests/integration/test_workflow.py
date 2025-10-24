# ruff: noqa: D103
"""Integration-style checks for the agentic workflow."""

from agentic_py.core.agent_registry import AgentRegistry
from agentic_py.models.agent_profile import AgentProfile
from agentic_py.services.orchestrator import AgentOrchestrator


def test_end_to_end_assignment_flow() -> None:
    registry = AgentRegistry()
    agent = AgentProfile(identifier="agent-42", display_name="Agent 42")
    registry.register(agent)

    orchestrator = AgentOrchestrator(registry=registry)
    orchestrator.assign_task(agent.identifier, "Answer life questions")
    assert "Answer life questions" in set(orchestrator.active_assignments())

    completed = orchestrator.complete_task(agent.identifier)
    assert completed == "Answer life questions"
