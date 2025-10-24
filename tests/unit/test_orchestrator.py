# ruff: noqa: D103
# pylint: disable=W0621

"""Unit tests for the AgentOrchestrator service."""

import pytest

from agentic_py.core.agent_registry import AgentRegistry
from agentic_py.exceptions import AgentNotFoundError, InvalidTaskError
from agentic_py.models.agent_profile import AgentProfile
from agentic_py.services.orchestrator import AgentOrchestrator


@pytest.fixture()
def orchestrator() -> AgentOrchestrator:
    registry = AgentRegistry()
    registry.register(AgentProfile(identifier="agent-1", display_name="Agent One"))
    return AgentOrchestrator(registry=registry)


def test_assign_and_complete_task(orchestrator: AgentOrchestrator) -> None:
    orchestrator.assign_task("agent-1", "Process dataset")

    result = orchestrator.complete_task("agent-1")

    assert result == "Process dataset"
    assert not list(orchestrator.active_assignments())


def test_assign_task_to_unknown_agent_raises(orchestrator: AgentOrchestrator) -> None:
    with pytest.raises(AgentNotFoundError):
        orchestrator.assign_task("missing-agent", "Explore")


def test_assign_empty_task_raises(orchestrator: AgentOrchestrator) -> None:
    with pytest.raises(InvalidTaskError):
        orchestrator.assign_task("agent-1", "")


def test_complete_missing_task_raises(orchestrator: AgentOrchestrator) -> None:
    with pytest.raises(InvalidTaskError):
        orchestrator.complete_task("agent-1")
