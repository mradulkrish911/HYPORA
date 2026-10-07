import pandas as pd

from hypora.profiling.profiler import DatasetProfiler


def test_profile_dataset():
    df = pd.DataFrame(
        {
            "age": [21, 25, 30, 25],
            "city": ["Delhi", "Noida", "Delhi", "Noida"],
            "salary": [40000, 55000, None, 55000],
        }
    )

    profiler = DatasetProfiler()

    profile = profiler.profile(df, "employees.csv")

    assert profile.dataset_name == "employees.csv"
    assert profile.row_count == 4
    assert profile.column_count == 3


def test_profile_column_information():
    df = pd.DataFrame(
        {
            "age": [21, 25, 30, 25],
            "city": ["Delhi", "Noida", "Delhi", "Noida"],
        }
    )

    profiler = DatasetProfiler()

    profile = profiler.profile(df, "employees.csv")

    age_profile = profile.columns[0]

    assert age_profile.name == "age"
    assert age_profile.dtype == "int64"
    assert age_profile.missing_count == 0
    assert age_profile.unique_count == 3


def test_profile_missing_values():
    df = pd.DataFrame(
        {
            "age": [21, None, 30],
            "salary": [40000, 50000, None],
        }
    )

    profiler = DatasetProfiler()

    profile = profiler.profile(df, "employees.csv")

    assert profile.missing_values == 2
    assert profile.columns[0].missing_count == 1
    assert profile.columns[1].missing_count == 1


def test_profile_duplicate_rows():
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Alice"],
            "age": [21, 25, 21],
        }
    )

    profiler = DatasetProfiler()

    profile = profiler.profile(df, "employees.csv")

    assert profile.duplicate_rows == 1