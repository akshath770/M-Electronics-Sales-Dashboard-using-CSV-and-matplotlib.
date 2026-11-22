
import pandas as pd
from pathlib import Path

DATA_FILE = Path(__file__).parent / "product_sales_practice.csv"


def load_data():
    """Load sales data from the CSV file."""

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}"
        )

    df = pd.read_csv(DATA_FILE)

    if df.empty:
        raise ValueError("The CSV dataset is empty.")

    return df
