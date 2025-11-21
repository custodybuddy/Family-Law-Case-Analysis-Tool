"""Placeholder legal aid service matching module."""

from typing import Any


def match_legal_aid_services(document_id: str) -> dict[str, Any]:
    return {
        "document_id": document_id,
        "providers": [],
        "notes": "Legal aid matching not yet implemented.",
    }
