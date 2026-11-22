
import pandas as pd


def calculate_metrics(df):

    total_revenue = df["Net_Sales"].sum()
    total_orders = df["Order_ID"].nunique()
    total_units = df["Quantity"].sum()

    average_order_value = (
        total_revenue / total_orders
        if total_orders > 0 else 0
    )

    return {
        "Total Revenue": total_revenue,
        "Total Orders": total_orders,
        "Total Units Sold": total_units,
        "Average Order Value": average_order_value
    }


def monthly_sales(df):

    result = (
        df.groupby(df["Date"].dt.to_period("M"))["Net_Sales"]
        .sum()
        .reset_index()
    )

    result["Month"] = result["Date"].astype(str)

    return result


def product_sales(df):

    return (
        df.groupby("Product")["Net_Sales"]
        .sum()
        .sort_values(ascending=False)
    )


def regional_sales(df):

    return (
        df.groupby("Region")["Net_Sales"]
        .sum()
        .sort_values(ascending=False)
    )


def salesperson_sales(df):

    return (
        df.groupby("Salesperson")["Net_Sales"]
        .sum()
        .sort_values(ascending=False)
    )


def category_sales(df):

    return (
        df.groupby("Category")["Net_Sales"]
        .sum()
        .sort_values(ascending=False)
    )
