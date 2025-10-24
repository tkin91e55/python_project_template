# ruff: noqa: D103
"""Unit tests for the AgentRegistry."""

from agentic_py.core.agent_registry import AgentRegistry
from agentic_py.exceptions import AgentAlreadyRegisteredError, AgentNotFoundError
from agentic_py.models.agent_profile import AgentProfile


def test_register_and_retrieve_agent() -> None:
    registry = AgentRegistry()
    profile = AgentProfile(identifier="agent-1", display_name="Agent One")

    registry.register(profile)

    retrieved = registry.get("agent-1")
    assert retrieved.identifier == "agent-1"
    assert retrieved.display_name == "Agent One"


def test_register_duplicate_agent_raises() -> None:
    registry = AgentRegistry()
    profile = AgentProfile(identifier="agent-dup", display_name="Duplicate Agent")
    registry.register(profile)

    try:
        registry.register(profile)
    except AgentAlreadyRegisteredError:
        assert True
    else:
        raise AssertionError("Expected AgentAlreadyRegisteredError to be raised.")


def test_deregister_agent_removes_profile() -> None:
    registry = AgentRegistry()
    profile = AgentProfile(identifier="agent-remove", display_name="Agent Remove")
    registry.register(profile)

    removed_profile = registry.deregister("agent-remove")
    assert removed_profile is not None
    assert removed_profile.identifier == "agent-remove"

    try:
        registry.get("agent-remove")
    except AgentNotFoundError:
        assert True
    else:
        raise AssertionError("Expected AgentNotFoundError to be raised.")
