from hypora.eda.models import Finding
from hypora.profiling.models import DatasetProfile


class FindingDetector:
    """Detect noteworthy patterns from a dataset profile."""

    def detect(self, profile: DatasetProfile) -> list[Finding]:
        findings = []

        # Check missingness for each column
        for column in profile.columns:
            missing_percentage = (
                #what if the profile.row_count is 0?
                (column.missing_count / profile.row_count) * 100
                if profile.row_count > 0
                else 0
            )

            # Constraints needs to be dynamic
            if missing_percentage > 30:
                findings.append(
                    Finding(
                        finding_type="high_missingness",
                        column=column.name,
                        description=(
                            f"Column '{column.name}' has "
                            f"{missing_percentage:.1f}% missing values."
                        ),
                        severity="high",
                    )
                )

            elif missing_percentage >= 10:
                findings.append(
                    Finding(
                        finding_type="moderate_missingness",
                        column=column.name,
                        description=(
                            f"Column '{column.name}' has "
                            f"{missing_percentage:.1f}% missing values."
                        ),
                        severity="medium",
                    )
                )

        # Check duplicate rows
        duplicate_percentage = (
            profile.duplicate_rows / profile.row_count
        ) * 100

        if duplicate_percentage > 10:
            findings.append(
                Finding(
                    finding_type="high_duplicate_rate",
                    description=(
                        f"Dataset contains "
                        f"{duplicate_percentage:.1f}% duplicate rows."
                    ),
                    severity="high",
                )
            )

        elif duplicate_percentage >= 5:
            findings.append(
                Finding(
                    finding_type="moderate_duplicate_rate",
                    description=(
                        f"Dataset contains "
                        f"{duplicate_percentage:.1f}% duplicate rows."
                    ),
                    severity="medium",
                )
            )

        return findings