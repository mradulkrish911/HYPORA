import pandas as pd

from hypora.profiling.models import ColumnProfile, DatasetProfile


class DatasetProfiler:
    """Generate a structural profile of a dataset."""

    def profile(
        self,
        df: pd.DataFrame,
        dataset_name: str
    ) -> DatasetProfile:
        """
        Generate a structural profile of a dataset.

        Parameters
        ----------
        df : pd.DataFrame
            Dataset to profile.

        dataset_name : str
            Name of the dataset.

        Returns
        -------
        DatasetProfile
            Structured profile containing dataset and column-level
            information.
        """

        # Dataset-level information
        row_count, column_count = df.shape

        # Missing values
        missing_counts = df.isna().sum()
        total_missing = int(missing_counts.sum())

        # Unique values
        unique_counts = df.nunique()

        # Duplicate rows
        duplicate_rows = int(df.duplicated().sum())

        # Column-level profiles
        columns = []

        for column in df.columns:
            column_profile = ColumnProfile(
                name=column,
                dtype=str(df[column].dtype),
                missing_count=int(missing_counts[column]),
                unique_count=int(unique_counts[column]),
            )

            columns.append(column_profile)

        # Create and return the validated DatasetProfile
        return DatasetProfile(
            dataset_name=dataset_name,
            row_count=row_count,
            column_count=column_count,
            columns=columns,
            missing_values=total_missing,
            duplicate_rows=duplicate_rows,
        )