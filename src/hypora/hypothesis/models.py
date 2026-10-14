from pydantic import BaseModel

from hypora.eda.models import Finding


class Hypothesis(BaseModel):
    """Represent a testable hypothesis about a dataset."""

    description: str
    evidence: list[Finding]
    prediction: str