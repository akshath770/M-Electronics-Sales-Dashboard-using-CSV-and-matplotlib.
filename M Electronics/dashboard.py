
import streamlit as st
import pandas as pd

from data_loader import load_data
from data_cleaning import clean_data

from analysis import (
    calculate_metrics,
    monthly_sales,
    product_sales,
    regional_sales,
    salesperson_sales,
    category_sales
)

from visualizations import (
    monthly_chart,
    product_chart,
    regional_chart,
    salesperson_chart,
    category_chart
)


def run_dashboard():

    st.set_page_config(
        page_title="M Electronics Dashboard",
        page_icon="📊",
        layout="wide"
    )

    st.title("M Electronics")
    st.subheader("Retail Sales Analysis Dashboard")

    st.markdown(
        "Analyse product sales, revenue and business performance."
    )

    # Load and clean dataset
    try:
        raw_data = load_data()
        df = clean_data(raw_data)

    except Exception as error:
        st.error(f"Unable to load dataset: {error}")
        return

    if df.empty:
        st.warning("No valid sales records found.")
        return

    # Sidebar filters
    st.sidebar.header("Dashboard Filters")

    min_date = df["Date"].min().date()
    max_date = df["Date"].max().date()

    selected_dates = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    if not isinstance(selected_dates, (tuple, list)):
        selected_dates = (selected_dates, selected_dates)

    if len(selected_dates) == 2:
        start_date, end_date = selected_dates
    else:
        start_date = end_date = selected_dates[0]

    products = sorted(df["Product"].unique())

    selected_products = st.sidebar.multiselect(
        "Select Products",
        products,
        default=products
    )

    regions = sorted(df["Region"].unique())

    selected_regions = st.sidebar.multiselect(
        "Select Regions",
        regions,
        default=regions
    )

    # Apply filters
    filtered_df = df[
        (df["Date"].dt.date >= start_date) &
        (df["Date"].dt.date <= end_date) &
        (df["Product"].isin(selected_products)) &
        (df["Region"].isin(selected_regions))
    ]

    if filtered_df.empty:
        st.warning("No records match the selected filters.")
        return

    # KPI metrics
    metrics = calculate_metrics(filtered_df)

    st.markdown("### Business Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Revenue",
        f"₹{metrics['Total Revenue']:,.2f}"
    )

    col2.metric(
        "Total Orders",
        f"{metrics['Total Orders']:,}"
    )

    col3.metric(
        "Units Sold",
        f"{metrics['Total Units Sold']:,.0f}"
    )

    col4.metric(
        "Average Order Value",
        f"₹{metrics['Average Order Value']:,.2f}"
    )

    st.divider()

    # Monthly sales
    st.markdown("### Monthly Sales Analysis")

    monthly_data = monthly_sales(filtered_df)

    st.pyplot(
        monthly_chart(monthly_data),
        width="stretch"
    )

    # Product analysis
    st.markdown("### Product Performance")

    col1, col2 = st.columns(2)

    with col1:
        st.pyplot(
            product_chart(product_sales(filtered_df)),
            width="stretch"
        )

    with col2:
        st.pyplot(
            regional_chart(regional_sales(filtered_df)),
            width="stretch"
        )

    # Category and salesperson analysis
    st.markdown("### Business Performance")

    col1, col2 = st.columns(2)

    with col1:
        st.pyplot(
            category_chart(category_sales(filtered_df)),
            width="stretch"
        )

    with col2:
        st.pyplot(
            salesperson_chart(salesperson_sales(filtered_df)),
            width="stretch"
        )

    st.divider()

    # Top selling products
    st.markdown("### Top 5 Revenue-Generating Products")

    top_products = product_sales(filtered_df).head(5)

    st.dataframe(
        top_products.rename("Revenue (₹)").reset_index(),
        width="stretch",
        hide_index=True
    )

    # Dataset preview
    with st.expander("View Sales Dataset"):
        st.dataframe(
            filtered_df,
            width="stretch",
            hide_index=True
        )

    # Download filtered data
    csv_data = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Filtered Sales Data",
        data=csv_data,
        file_name="M_Electronics_Sales_Report.csv",
        mime="text/csv"
    )

    st.caption(
        "M Electronics | Retail Sales Analysis Dashboard | "
        "Developed using Python, Pandas and Matplotlib"
    )
