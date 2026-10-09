from pydantic import BaseModel, Field


class Finding(BaseModel):
    finding_type: str
    column: str | None = None
    description: str
    severity: str


class ColumnProfile(BaseModel):
    name: str
    dtype: str
    missing_count: int = Field(ge=0)
    unique_count: int = Field(ge=0)

class DatasetProfile(BaseModel):
    dataset_name: str
    row_count: int = Field(ge=0)
    column_count: int = Field(ge=0)
    columns: list[ColumnProfile]
    missing_values: int = Field(ge=0)
    duplicate_rows: int = Field(ge=0)
