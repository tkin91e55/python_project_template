"""
Agentic Python tooling playground package.

This package offers a lightweight but structured example project that showcases
type-safe service orchestration, configuration management, and documentation
tooling intended for agent-based workflows.
"""

from .config import AppConfig, get_config
from .core.agent_registry import AgentRegistry
from .services.orchestrator import AgentOrchestrator

__all__ = [
    "AgentRegistry",
    "AgentOrchestrator",
    "AppConfig",
    "get_config",
]
