from pathlib import Path

import pandas as pd


class DatasetLoader:
    """Load datasets into pandas DataFrames."""

    def load_csv(self, path: Path) -> pd.DataFrame:
        """
        Load a CSV file into a pandas DataFrame.

        Parameters
        ----------
        path : Path
            Path to the CSV file.

        Returns
        -------
        pd.DataFrame
            The loaded dataset.

        Raises
        ------
        FileNotFoundError
            If the file does not exist.
        ValueError
            If the supplied path is not a CSV file.
        """

        if not path.exists():
            raise FileNotFoundError(f"Dataset not found: {path}")

        if not path.is_file():
            raise ValueError(f"Path is not a file: {path}")

        if path.suffix.lower() != ".csv":
            raise ValueError(f"Unsupported file type: {path.suffix}")

        return pd.read_csv(path)