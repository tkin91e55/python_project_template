# pylint: disable=C0413
"""Business logic around coordinating agent tasks."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable

from agentic_py.exceptions import AgentNotFoundError, InvalidTaskError
from agentic_py.models.agent_profile import AgentProfile
from agentic_py.utils.logging import configure_logging


@dataclass
class AgentOrchestrator:
    """Coordinate work assignments for registered agents."""

    registry: "AgentRegistry"
    _active_tasks: Dict[str, str] = field(default_factory=dict)

    def assign_task(self, agent_id: str, task_description: str) -> None:
        """Assign a task to an agent, logging the operation."""
        if not task_description.strip():
            raise InvalidTaskError("Task description must be a non-empty string.")

        profile = self._get_agent(agent_id)
        logger = configure_logging("agentic_py.services.orchestrator")
        logger.info("Assigning task '%s' to %s", task_description, profile.display_name)
        self._active_tasks[agent_id] = task_description

    def complete_task(self, agent_id: str) -> str:
        """Mark the task as complete and return its description."""
        task = self._active_tasks.pop(agent_id, None)
        if task is None:
            raise InvalidTaskError(f"Agent '{agent_id}' does not have an active task.")

        logger = configure_logging("agentic_py.services.orchestrator")
        logger.info("Agent '%s' completed task '%s'", agent_id, task)
        return task

    def active_assignments(self) -> Iterable[str]:
        """Return the current active task descriptions."""
        return self._active_tasks.values()

    def _get_agent(self, agent_id: str) -> AgentProfile:
        try:
            return self.registry.get(agent_id)
        except AgentNotFoundError as exc:
            raise AgentNotFoundError(
                f"Cannot assign task; agent '{agent_id}' is not registered.",
            ) from exc


# Local import to avoid circular dependency during type checking.
from agentic_py.core.agent_registry import (
    AgentRegistry,  # noqa: E402  pylint: disable=C0413
)
