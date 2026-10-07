from pydantic import BaseModel


class ColumnProfile(BaseModel):
    name: str
    dtype: str
    missing_count: int
    unique_count: int


class DatasetProfile(BaseModel):
    dataset_name: str
    row_count: int
    column_count: int
    columns: list[ColumnProfile]
    missing_values: int
    duplicate_rows: int