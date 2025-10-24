"""Core registry functionality for managing agents."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, Optional

from agentic_py.config import get_config
from agentic_py.exceptions import AgentAlreadyRegisteredError, AgentNotFoundError
from agentic_py.models.agent_profile import AgentProfile


@dataclass
class AgentRegistry:
    """Maintain a registry of known agents."""

    _agents: Dict[str, AgentProfile] = field(default_factory=dict)

    def register(self, profile: AgentProfile) -> None:
        """Register an agent profile, enforcing uniqueness and capacity limits."""
        config = get_config()
        if len(self._agents) >= config.registry_capacity:
            raise AgentAlreadyRegisteredError(
                "Registry capacity reached; cannot register additional agents",
            )

        if profile.identifier in self._agents:
            raise AgentAlreadyRegisteredError(
                f"Agent '{profile.identifier}' is already registered.",
            )

        self._agents[profile.identifier] = profile

    def get(self, identifier: str) -> AgentProfile:
        """Return an agent profile by identifier."""
        try:
            return self._agents[identifier]
        except KeyError as exc:
            raise AgentNotFoundError(
                f"Agent '{identifier}' does not exist in the registry.",
            ) from exc

    def list(self) -> Iterable[AgentProfile]:
        """Return all registered agent profiles."""
        return self._agents.values()

    def update_status(self, identifier: str, status: str) -> AgentProfile:
        """Update and return the agent profile with a new status."""
        profile = self.get(identifier)
        updated_profile = profile.model_copy(update={"status": status})
        self._agents[identifier] = updated_profile
        return updated_profile

    def deregister(self, identifier: str) -> Optional[AgentProfile]:
        """Remove and return an agent profile if present."""
        return self._agents.pop(identifier, None)
