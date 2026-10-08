from pydantic import BaseModel


class Finding(BaseModel):
    finding_type: str
    column: str | None = None
    description: str
    severity: str