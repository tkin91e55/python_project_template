"""Custom exceptions for the agentic_py package."""


class AgenticPyError(Exception):
    """Base exception for the package."""


class AgentAlreadyRegisteredError(AgenticPyError):
    """Raised when attempting to register an agent that already exists."""


class AgentNotFoundError(AgenticPyError):
    """Raised when a requested agent cannot be located."""


class InvalidTaskError(AgenticPyError):
    """Raised when orchestration receives an invalid task payload."""
