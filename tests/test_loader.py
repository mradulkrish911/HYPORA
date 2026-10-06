from hypora.ingestion.loader import load_csv


def test_load_csv():
    df = load_csv("data/raw/sample.csv")

    assert not df.empty
    assert df.shape == (4, 3)
    assert list(df.columns) == ["name", "age", "score"]