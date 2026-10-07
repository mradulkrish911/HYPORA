from pathlib import Path

import pandas as pd
import pytest

from hypora.ingestion.loader import DatasetLoader


def test_load_csv(tmp_path: Path):
    csv_file = tmp_path / "sample.csv"

    csv_file.write_text(
        "name,age\nAlice,21\nBob,25\n"
    )

    loader = DatasetLoader()

    result = loader.load_csv(csv_file)

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2
    assert list(result.columns) == ["name", "age"]

def test_load_csv_file_not_found(tmp_path: Path):
    loader = DatasetLoader()

    with pytest.raises(FileNotFoundError):
        loader.load_csv(Path("does_not_exist.csv"))

def test_load_csv_rejects_non_csv(tmp_path: Path):
    txt_file = tmp_path / "sample.txt"
    txt_file.write_text("hello")

    loader = DatasetLoader()

    with pytest.raises(ValueError):
        loader.load_csv(txt_file)