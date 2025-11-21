from fastapi import APIRouter

from ..schemas.document import DocumentIngestionRequest, DocumentIngestionResponse, DocumentStatusResponse
from ..services.ingestion import ingestion_service

api_router = APIRouter(prefix="/api", tags=["api"])


@api_router.post("/documents/ingest", response_model=DocumentIngestionResponse)
def ingest_document(request: DocumentIngestionRequest) -> DocumentIngestionResponse:
    """Ingest a new document into the system for later processing."""

    return ingestion_service.ingest(request)


@api_router.get("/documents/{document_id}/status", response_model=DocumentStatusResponse)
def get_document_status(document_id: str) -> DocumentStatusResponse:
    """Return the current processing status for a document."""

    return ingestion_service.status(document_id)
