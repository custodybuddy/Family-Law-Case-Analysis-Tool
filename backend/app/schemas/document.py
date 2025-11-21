from pydantic import BaseModel, Field


class DocumentMetadata(BaseModel):
    title: str | None = Field(default=None, description="Optional document title")
    description: str | None = Field(default=None, description="Optional summary provided by the user")
    tags: list[str] = Field(default_factory=list, description="Labels that can be used to organize documents")


class DocumentIngestionRequest(BaseModel):
    content: str = Field(..., description="Raw text content or base64-encoded file contents")
    filename: str = Field(..., description="Original name of the uploaded file")
    metadata: DocumentMetadata | None = Field(default=None, description="Optional document metadata")


class DocumentIngestionResponse(BaseModel):
    document_id: str = Field(..., description="Temporary reference to the stored document")
    status: str = Field(..., description="Processing status for the ingestion job")


class DocumentStatusResponse(BaseModel):
    document_id: str
    status: str
    notes: str | None = None
