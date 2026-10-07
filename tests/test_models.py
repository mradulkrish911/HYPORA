import pytest
from pydantic import ValidationError

from hypora.profiling.models import ColumnProfile, DatasetProfile


def test_column_profile():
    profile = ColumnProfile(
        name="age",
        dtype="int64",
        missing_count=2,
        unique_count=50,
    )

    assert profile.name == "age"
    assert profile.missing_count == 2


def test_dataset_profile():
    profile = DatasetProfile(
        dataset_name="customers.csv",
        row_count=1000,
        column_count=1,
        columns=[
            ColumnProfile(
                name="age",
                dtype="int64",
                missing_count=2,
                unique_count=50,
            )
        ],
        missing_values=2,
        duplicate_rows=3,
    )

    assert profile.row_count == 1000
    assert len(profile.columns) == 1

def test_column_profile_rejects_invalid_data():
    with pytest.raises(ValidationError):
        ColumnProfile(
            name="age",
            dtype="int64",
            missing_count="not a number",
            unique_count=50,
        )

