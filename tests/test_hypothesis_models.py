from pydantic import ValidationError
import pytest

from hypora.eda.models import Finding
from hypora.hypothesis.models import Hypothesis


def test_creates_valid_hypothesis():
    finding = Finding(
        finding_type="high_missingness",
        column="salary",
        description="Salary column has 40% missing values.",
        severity="high",
    )

    hypothesis = Hypothesis(
        description="Median imputation may preserve useful training data.",
        evidence=[finding],
        prediction="More training rows will be retained than with row deletion.",
    )

    assert hypothesis.description == (
        "Median imputation may preserve useful training data."
    )
    assert hypothesis.evidence == [finding]
    assert hypothesis.prediction == (
        "More training rows will be retained than with row deletion."
    )


def test_rejects_missing_description():
    with pytest.raises(ValidationError):
        Hypothesis(
            evidence=[],
            prediction="More training rows will be retained.",
        )


def test_rejects_invalid_evidence():
    with pytest.raises(ValidationError):
        Hypothesis(
            description="Test hypothesis",
            evidence=["not a Finding object"],
            prediction="An observable outcome will occur.",
        )