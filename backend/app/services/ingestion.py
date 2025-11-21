from __future__ import annotations

import uuid
from typing import Any

from ..schemas.document import DocumentIngestionRequest, DocumentIngestionResponse, DocumentStatusResponse


class IngestionService:
    """Placeholder ingestion service for document storage and preprocessing."""

    def __init__(self) -> None:
        self._storage: dict[str, dict[str, Any]] = {}

    def ingest(self, request: DocumentIngestionRequest) -> DocumentIngestionResponse:
        document_id = str(uuid.uuid4())
        self._storage[document_id] = {
            "filename": request.filename,
            "metadata": request.metadata.model_dump() if request.metadata else {},
            "content": request.content,
            "status": "received",
        }
        return DocumentIngestionResponse(document_id=document_id, status="received")

    def status(self, document_id: str) -> DocumentStatusResponse:
        document = self._storage.get(document_id)
        if not document:
            return DocumentStatusResponse(document_id=document_id, status="not_found", notes="Document not ingested yet")

        return DocumentStatusResponse(document_id=document_id, status=document.get("status", "unknown"))


ingestion_service = IngestionService()
