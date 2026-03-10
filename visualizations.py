"""
visualizations.py
-----------------
Sales analytics visualizations for the 2025 coffee sales project.
All data is loaded from exported PostgreSQL query results in /query_results.
Charts are saved as PNG files in /charts.

Pipeline:
    coffee_data/ (raw) → PostgreSQL (analysis.sql) → query_results/ → visualizations.py → charts/
"""

import os
import pandas as pd
import plotly.express as px

# Paths
BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
DATA_DIR    = os.path.join(BASE_DIR, "query_results")
OUTPUT_DIR  = os.path.join(BASE_DIR, "charts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load(filename):
    """Load a CSV from the query_results folder."""
    return pd.read_csv(os.path.join(DATA_DIR, filename))

def save(fig, filename):
    """Save a Plotly figure as PNG to the Charts folder."""
    fig.write_image(os.path.join(OUTPUT_DIR, filename), scale=3)
    print(f"Saved: {filename}")

# 1. Daily Revenue Trend

df = load("daily_revenue.csv")
df["order_date"] = pd.to_datetime(df["order_date"])

fig = px.line(
    df,
    x="order_date",
    y="daily_revenue",
    title="Daily Revenue Trend (2025)",
    labels={"order_date": "Date", "daily_revenue": "Revenue"},
    template="plotly_white"
)
fig.update_traces(mode="lines+markers", line=dict(color="#1f77b4", width=2))
fig.update_layout(
    title_font_size=22,
    xaxis_title="Date",
    yaxis_title="Revenue",
    hovermode="x unified"
)
save(fig, "daily_revenue_chart.png")

# 2. Monthly Revenue

df = load("monthly_revenue.csv")
df["month"] = pd.to_datetime(df["month"])
df = df.sort_values("month")

fig = px.bar(
    df,
    x="month",
    y="revenue",
    title="Monthly Revenue (2025)",
    labels={"month": "Month", "revenue": "Revenue"},
    text="revenue",
    template="plotly_white",
    color="revenue",
    color_continuous_scale="Blues"
)
fig.update_traces(texttemplate="%{text:,}", textposition="outside")
fig.update_layout(
    title_font_size=22,
    xaxis_title="Month",
    yaxis_title="Revenue",
    hovermode="x unified",
    uniformtext_minsize=8,
    uniformtext_mode="hide"
)
fig.update_yaxes(tickformat=",")
save(fig, "monthly_revenue_chart.png")

# 3. Top 10 Best-Selling Products

df = load("top_products.csv")
df = df.sort_values("total_units_sold", ascending=True)

fig = px.bar(
    df,
    x="total_units_sold",
    y="product_name",
    orientation="h",
    title="Top 10 Best-Selling Products",
    labels={"total_units_sold": "Units Sold", "product_name": "Product"},
    text="total_units_sold",
    template="plotly_white",
    color="total_units_sold",
    color_continuous_scale="Blues"
)
fig.update_traces(texttemplate="%{text:,}", textposition="outside")
fig.update_layout(
    title_font_size=22,
    xaxis_title="Units Sold",
    yaxis_title="Product",
    hovermode="y unified"
)
save(fig, "top_products_chart.png")

# 4. Revenue by Product Category

df = load("revenue_by_category.csv")
df = df.sort_values("revenue", ascending=True)

fig = px.bar(
    df,
    x="revenue",
    y="category",
    orientation="h",
    title="Revenue by Product Category (2025)",
    labels={"revenue": "Revenue", "category": "Category"},
    text="revenue",
    template="plotly_white",
    color="revenue",
    color_continuous_scale="Blues"
)
fig.update_traces(texttemplate="%{text:,.0f}", textposition="outside")
fig.update_layout(
    title_font_size=22,
    xaxis_title="Revenue",
    yaxis_title="Category",
    hovermode="y unified"
)
save(fig, "revenue_by_product_category_chart.png")

# 5. Store Revenue by City

df = load("store_revenue_by_city.csv")
df = df.sort_values("revenue", ascending=True)

fig = px.bar(
    df,
    x="revenue",
    y="city",
    orientation="h",
    color="country",
    title="Store Revenue by City (2025)",
    labels={"revenue": "Revenue", "city": "City", "country": "Country"},
    text="revenue",
    template="plotly_white",
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig.update_traces(texttemplate="%{text:,}", textposition="outside")
fig.update_layout(
    title_font_size=22,
    xaxis_title="Revenue",
    yaxis_title="City",
    hovermode="y unified",
    legend_title_text="Country"
)
save(fig, "store_revenue_by_city_chart.png")

# 6. Peak Ordering Hours

df = load("peak_ordering_hours.csv")
df = df.sort_values("hour")

fig = px.bar(
    df,
    x="hour",
    y="order_count",
    title="Peak Ordering Hours (2025)",
    labels={"hour": "Hour of Day", "order_count": "Number of Orders"},
    text="order_count",
    template="plotly_white",
    color="order_count",
    color_continuous_scale="Blues"
)
fig.update_traces(texttemplate="%{text:,}", textposition="outside")
fig.update_layout(
    title_font_size=22,
    xaxis_title="Hour of Day",
    yaxis_title="Number of Orders",
    hovermode="x unified",
    xaxis=dict(tickmode="linear", tick0=0, dtick=1)
)
save(fig, "peak_ordering_hours_chart.png")

# 7. Top 20 Customers by Lifetime Value

df = load("top_customers_by_value.csv")
df = df.sort_values("lifetime_value", ascending=True)

fig = px.bar(
    df,
    x="lifetime_value",
    y="name",
    orientation="h",
    color="loyalty_tier",
    title="Top 20 Customers by Lifetime Value",
    labels={"lifetime_value": "Lifetime Value", "name": "Customer", "loyalty_tier": "Loyalty Tier"},
    text="lifetime_value",
    template="plotly_white",
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig.update_traces(texttemplate="%{text:,}", textposition="outside")
fig.update_layout(
    title_font_size=22,
    xaxis_title="Lifetime Value",
    yaxis_title="Customer",
    hovermode="y unified",
    legend_title_text="Loyalty Tier"
)
save(fig, "top_customers_by_value_chart.png")

# 8. Seasonal Drink Performance (Pumpkin Spice Latte)

df = load("seasonal_drink_performance.csv")
df["month"] = pd.to_datetime(df["month"])
df = df.sort_values("month")

fig = px.line(
    df,
    x="month",
    y="units_sold",
    title="Seasonal Drink Performance — Pumpkin Spice Latte (2025)",
    labels={"month": "Month", "units_sold": "Units Sold"},
    template="plotly_white",
    markers=True
)
fig.update_traces(line=dict(color="#e07b39", width=2))
fig.update_layout(
    title_font_size=22,
    xaxis_title="Month",
    yaxis_title="Units Sold",
    hovermode="x unified"
)
save(fig, "seasonal_drink_performance_chart.png")

# 9. Revenue by Loyalty Tier

df = load("revenue_by_loyalty_tier.csv")
df = df.sort_values("revenue", ascending=True)

fig = px.bar(
    df,
    x="revenue",
    y="loyalty_tier",
    orientation="h",
    title="Revenue by Loyalty Tier",
    labels={"revenue": "Revenue", "loyalty_tier": "Loyalty Tier"},
    text="revenue",
    template="plotly_white",
    color="revenue",
    color_continuous_scale="Blues"
)
fig.update_traces(texttemplate="%{text:,}", textposition="outside")
fig.update_layout(
    title_font_size=22,
    xaxis_title="Revenue",
    yaxis_title="Loyalty Tier",
    hovermode="y unified"
)
save(fig, "revenue_by_loyalty_tier_chart.png")

# 10. Top 10 Customers by Number of Orders

df = load("top_customers_by_activity.csv")
df = df.sort_values("total_orders", ascending=True)

fig = px.bar(
    df,
    x="total_orders",
    y="name",
    orientation="h",
    title="Top 10 Customers by Number of Orders",
    labels={"total_orders": "Total Orders", "name": "Customer"},
    text="total_orders",
    template="plotly_white",
    color="total_orders",
    color_continuous_scale="Blues"
)
fig.update_traces(texttemplate="%{text}", textposition="outside")
fig.update_layout(
    title_font_size=22,
    xaxis_title="Total Orders",
    yaxis_title="Customer",
    hovermode="y unified"
)
save(fig, "top_customers_by_activity_chart.png")

# 11. Top 10 Customers by Revenue

df = load("top_10_customers_by_value.csv")
df = df.sort_values("revenue", ascending=True)

fig = px.bar(
    df,
    x="revenue",
    y="name",
    orientation="h",
    title="Top 10 Customers by Revenue",
    labels={"revenue": "Revenue", "name": "Customer"},
    text="revenue",
    template="plotly_white",
    color="revenue",
    color_continuous_scale="Blues"
)
fig.update_traces(texttemplate="%{text:,}", textposition="outside")
fig.update_layout(
    title_font_size=22,
    xaxis_title="Revenue",
    yaxis_title="Customer",
    hovermode="y unified"
)
save(fig, "top_10_customers_by_revenue_chart.png")

# 12. Monthly Revenue by City — Line Chart

df = load("monthly_revenue_by_city.csv")
df["month"] = pd.to_datetime(df["month"])
df = df.sort_values("month")

fig = px.line(
    df,
    x="month",
    y="revenue",
    color="city",
    title="Monthly Revenue by City (2025)",
    labels={"month": "Month", "revenue": "Revenue", "city": "City"},
    template="plotly_white"
)
fig.update_traces(mode="lines+markers")
fig.update_layout(
    title_font_size=22,
    xaxis_title="Month",
    yaxis_title="Revenue",
    hovermode="x unified",
    legend_title_text="City"
)
save(fig, "monthly_revenue_by_city_chart.png")

# 13. Annual Total Revenue by City

annual = (
    df.groupby("city", as_index=False)["revenue"]
    .sum()
    .sort_values("revenue", ascending=False)
)

fig = px.bar(
    annual,
    x="city",
    y="revenue",
    color="city",
    title="Annual Total Revenue by City (2025)",
    labels={"city": "City", "revenue": "Annual Revenue"},
    template="plotly_white",
    text_auto=".3s"
)
fig.update_traces(textposition="outside", marker_line_width=0)
fig.update_layout(
    title_font_size=22,
    xaxis_title="City",
    yaxis_title="Annual Revenue",
    showlegend=False,
    yaxis=dict(
        tickformat="~s",
        range=[0, annual["revenue"].max() * 1.12]
    ),
    xaxis=dict(categoryorder="total descending"),
    uniformtext_minsize=8,
    uniformtext_mode="hide"
)
save(fig, "annual_total_revenue_by_city_chart.png")

# 14. Top Products by Country

df = load("top_products_by_country.csv")
df_top = df[df["rank"] == 1].sort_values("units_sold", ascending=True)

fig = px.bar(
    df_top,
    x="units_sold",
    y="country",
    orientation="h",
    title="Best-Selling Product per Country (2025)",
    labels={"units_sold": "Units Sold", "country": "Country", "product_name": "Product"},
    text="product_name",
    template="plotly_white",
    color="units_sold",
    color_continuous_scale="Blues"
)
fig.update_traces(textposition="outside")
fig.update_layout(
    title_font_size=22,
    xaxis_title="Units Sold",
    yaxis_title="Country",
    hovermode="y unified"
)
save(fig, "top_products_by_country_chart.png")

# ---------------------------------------------------------------------------
print(f"\nAll charts saved to: {OUTPUT_DIR}")
