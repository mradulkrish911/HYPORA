from hypora.eda.models import Finding
from hypora.hypothesis.generator import HypothesisGenerator


def test_generates_hypothesis_for_high_missingness():
    finding = Finding(
        finding_type="high_missingness",
        column="salary",
        description="Salary column has 40% missing values.",
        severity="high",
    )

    generator = HypothesisGenerator()

    hypotheses = generator.generate([finding])

    assert len(hypotheses) == 1
    assert hypotheses[0].evidence == [finding]