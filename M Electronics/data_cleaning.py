
import pandas as pd


def clean_data(df):

    df = df.copy()

    # Remove exact duplicate records
    df = df.drop_duplicates()

    # Convert date column
    df["Date"] = pd.to_datetime(
        df["Date"], errors="coerce"
    )

    # Convert numerical columns
    numeric_columns = [
        "Quantity", "Unit_Price", "Discount", "Sales"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column], errors="coerce"
        )

    # Remove records without essential information
    required_columns = [
        "Order_ID", "Date", "Product",
        "Quantity", "Unit_Price"
    ]

    df = df.dropna(subset=required_columns)

    # Remove invalid numerical values
    df = df[
        (df["Quantity"] > 0) &
        (df["Unit_Price"] >= 0)
    ]

    # Fill optional missing values
    df["Region"] = df["Region"].fillna("Unknown")
    df["Salesperson"] = df["Salesperson"].fillna("Unknown")
    df["Category"] = df["Category"].fillna("Unknown")

    # Fill missing discounts with zero
    df["Discount"] = df["Discount"].fillna(0)

    # Keep discount within valid range
    df["Discount"] = df["Discount"].clip(0, 1)

    # Calculate gross sales
    df["Sales"] = df["Quantity"] * df["Unit_Price"]

    # Calculate revenue after discount
    df["Net_Sales"] = (
        df["Sales"] * (1 - df["Discount"])
    )

    return df.reset_index(drop=True)
