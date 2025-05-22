from lcfs.web.api.base import BaseSchema


class FileResponseSchema(BaseSchema):
    document_id: int
    file_name: str
    file_size: int
    create_date: str | None = None
    create_user: str | None = None


class UrlResponseSchema(BaseSchema):
    url: str
