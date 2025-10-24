"""Logging helpers for the agentic_py package."""

from __future__ import annotations

import logging
from typing import Optional

from agentic_py.config import get_config


def configure_logging(logger_name: Optional[str] = None) -> logging.Logger:
    """Configure and return a namespaced logger."""
    config = get_config()
    logger = logging.getLogger(logger_name or "agentic_py")

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.setLevel(config.log_level)
    return logger
