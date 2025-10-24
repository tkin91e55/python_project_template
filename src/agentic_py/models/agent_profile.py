"""Data models for representing agents."""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field, field_validator


class AgentProfile(BaseModel):
    """Metadata describing an AI agent participant."""

    identifier: str = Field(..., min_length=3, max_length=50)
    display_name: str = Field(..., min_length=3, max_length=100)
    skills: List[str] = Field(
        default_factory=list,
        description="Primary capabilities offered by the agent.",
    )
    status: str = Field(
        default="idle",
        description="Current lifecycle status for the agent.",
    )
    description: Optional[str] = Field(
        default=None,
        max_length=250,
        description="Short summary of the agent's responsibilities.",
    )

    @field_validator("status")
    @classmethod
    def normalize_status(cls, value: str) -> str:
        """Ensure status is lower-case for consistent comparisons."""
        return value.lower()

    def add_skill(self, skill: str) -> "AgentProfile":
        """Return a mutated copy of this profile with a new skill."""
        if skill.lower() in {existing.lower() for existing in self.skills}:
            return self
        updated_skills = [*self.skills, skill]
        return self.model_copy(update={"skills": updated_skills})
