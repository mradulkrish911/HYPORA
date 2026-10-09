import pytest

from hypora.eda.finder import FindingDetector
from hypora.profiling.models import ColumnProfile, DatasetProfile


def test_detects_high_missingness():
    profile = DatasetProfile(
        dataset_name="employees.csv",
        row_count=100,
        column_count=1,
        columns=[
            ColumnProfile(
                name="salary",
                dtype="float64",
                missing_count=40,
                unique_count=60,
            )
        ],
        missing_values=40,
        duplicate_rows=0,
    )

    detector = FindingDetector()

    findings = detector.detect(profile)

    assert len(findings) == 1
    assert findings[0].finding_type == "high_missingness"
    assert findings[0].column == "salary"
    assert findings[0].severity == "high"


def test_detects_moderate_missingness():
    profile = DatasetProfile(
        dataset_name="employees.csv",
        row_count=100,
        column_count=1,
        columns=[
            ColumnProfile(
                name="salary",
                dtype="float64",
                missing_count=20,
                unique_count=80,
            )
        ],
        missing_values=20,
        duplicate_rows=0,
    )

    detector = FindingDetector()

    findings = detector.detect(profile)

    assert len(findings) == 1
    assert findings[0].finding_type == "moderate_missingness"
    assert findings[0].severity == "medium"


def test_ignores_low_missingness():
    profile = DatasetProfile(
        dataset_name="employees.csv",
        row_count=100,
        column_count=1,
        columns=[
            ColumnProfile(
                name="salary",
                dtype="float64",
                missing_count=5,
                unique_count=95,
            )
        ],
        missing_values=5,
        duplicate_rows=0,
    )

    detector = FindingDetector()

    findings = detector.detect(profile)

    assert len(findings) == 0


def test_detects_high_duplicate_rate():
    profile = DatasetProfile(
        dataset_name="employees.csv",
        row_count=100,
        column_count=1,
        columns=[
            ColumnProfile(
                name="name",
                dtype="object",
                missing_count=0,
                unique_count=90,
            )
        ],
        missing_values=0,
        duplicate_rows=20,
    )

    detector = FindingDetector()

    findings = detector.detect(profile)

    assert len(findings) == 1
    assert findings[0].finding_type == "high_duplicate_rate"
    assert findings[0].severity == "high"


def test_detects_moderate_duplicate_rate():
    profile = DatasetProfile(
        dataset_name="employees.csv",
        row_count=100,
        column_count=1,
        columns=[
            ColumnProfile(
                name="name",
                dtype="object",
                missing_count=0,
                unique_count=95,
            )
        ],
        missing_values=0,
        duplicate_rows=7,
    )

    detector = FindingDetector()

    findings = detector.detect(profile)

    assert len(findings) == 1
    assert findings[0].finding_type == "moderate_duplicate_rate"
    assert findings[0].severity == "medium"


def test_no_findings_for_clean_dataset():
    profile = DatasetProfile(
        dataset_name="employees.csv",
        row_count=100,
        column_count=2,
        columns=[
            ColumnProfile(
                name="age",
                dtype="int64",
                missing_count=2,
                unique_count=50,
            ),
            ColumnProfile(
                name="salary",
                dtype="int64",
                missing_count=0,
                unique_count=90,
            ),
        ],
        missing_values=2,
        duplicate_rows=2,
    )

    detector = FindingDetector()

    findings = detector.detect(profile)

    assert len(findings) == 0

