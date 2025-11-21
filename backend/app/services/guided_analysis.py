"""Placeholder guided analysis steps module."""

from typing import Any


DEFAULT_STEPS = [
    "Collect case overview",
    "Identify parties and relationships",
    "Timeline and procedural posture",
    "Jurisdiction and venue",
    "Key legal issues",
    "Fact strengths and weaknesses",
    "Evidence and exhibits",
    "Legal authority",
    "Arguments and counterarguments",
    "Remedies and outcomes",
    "Forms and filings",
    "Deadlines and rules",
    "Reminders and scheduling",
    "Support resources",
    "Document comparison",
]


def guided_analysis_plan(document_id: str) -> dict[str, Any]:
    return {
        "document_id": document_id,
        "steps": DEFAULT_STEPS,
        "notes": "Guided analysis workflow placeholder.",
    }
