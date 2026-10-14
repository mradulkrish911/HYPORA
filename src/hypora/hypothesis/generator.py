
from hypora.eda.models import Finding
from hypora.hypothesis.models import Hypothesis


class HypothesisGenerator:
    """Generate hypotheses from detected findings."""

    def generate(self, findings: list[Finding]) -> list[Hypothesis]:
        hypotheses = []

        for finding in findings:
            if finding.finding_type == "high_missingness":
                hypothesis = Hypothesis(
                    description=(
                        f"Imputing missing values in '{finding.column}' "
                        "may preserve useful data."
                    ),
                    evidence=[finding],
                    prediction=(
                        "Imputation will retain more usable rows than "
                        "dropping rows with missing values."
                    ),
                )
                hypotheses.append(hypothesis)

        return hypotheses
