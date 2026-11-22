
import matplotlib.pyplot as plt


def monthly_chart(data):

    fig, ax = plt.subplots(figsize=(9, 4))

    ax.plot(
        data["Month"],
        data["Net_Sales"],
        marker="o",
        linewidth=2
    )

    ax.set_title("Monthly Sales Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue (Rs.)")
    ax.tick_params(axis="x", rotation=30)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    return fig


def product_chart(data):

    fig, ax = plt.subplots(figsize=(9, 5))

    data.sort_values().plot(
        kind="barh",
        ax=ax
    )

    ax.set_title("Revenue by Product")
    ax.set_xlabel("Revenue (Rs.)")
    ax.set_ylabel("Product")

    fig.tight_layout()
    return fig


def regional_chart(data):

    fig, ax = plt.subplots(figsize=(7, 5))

    if data.sum() > 0:
        ax.pie(
            data,
            labels=data.index,
            autopct="%1.1f%%",
            startangle=90
        )
        ax.set_title("Regional Sales Distribution")
    else:
        ax.text(0.5, 0.5, "No sales data available",
                ha="center", va="center")

    fig.tight_layout()
    return fig


def salesperson_chart(data):

    fig, ax = plt.subplots(figsize=(9, 4))

    data.sort_values().plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Sales by Salesperson")
    ax.set_xlabel("Salesperson")
    ax.set_ylabel("Revenue (Rs.)")
    ax.tick_params(axis="x", rotation=30)

    fig.tight_layout()
    return fig


def category_chart(data):

    fig, ax = plt.subplots(figsize=(8, 4))

    data.sort_values().plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Revenue by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Revenue (Rs.)")
    ax.tick_params(axis="x", rotation=30)

    fig.tight_layout()
    return fig
