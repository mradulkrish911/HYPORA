import pytest
from pydantic import ValidationError

from hypora.eda.models import Finding


def test_finding():
    finding = Finding(
        finding_type="high_missingness",
        column="income",
        description="Column 'income' has high missingness.",
        severity="high",
    )

    assert finding.finding_type == "high_missingness"
    assert finding.column == "income"
    assert finding.severity == "high"


def test_finding_without_column():
    finding = Finding(
        finding_type="duplicate_rows",
        description="Dataset contains duplicate rows.",
        severity="medium",
    )

    assert finding.column is None


def test_finding_requires_description():
    with pytest.raises(ValidationError):
        Finding(
            finding_type="high_missingness",
            column="income",
            severity="high",
        )