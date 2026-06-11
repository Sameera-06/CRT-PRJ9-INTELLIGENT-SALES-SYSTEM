import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils.ui_styles import load_css

load_css()

st.title("📦 Inventory Optimization")

st.markdown("---")

# =====================================
# LOAD DATA
# =====================================

try:
    df = pd.read_csv("dataset/processed_sales.csv")
except:
    df = pd.read_csv("dataset/sales_data.csv")

# =====================================
# FIX DATA TYPES
# =====================================

numeric_columns = [
    "Quantity",
    "Current_Stock",
    "Revenue",
    "Profit",
    "Unit_Price"
]

for col in numeric_columns:

    if col in df.columns:

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

# Remove rows having invalid values

df = df.dropna(
    subset=["Quantity", "Current_Stock"]
)

# =====================================
# INVENTORY CALCULATIONS
# =====================================

inventory_df = (
    df.groupby("Product")
    .agg({
        "Quantity": "sum",
        "Current_Stock": "mean"
    })
    .reset_index()
)

inventory_df.rename(
    columns={
        "Quantity": "Demand"
    },
    inplace=True
)

inventory_df["Demand"] = pd.to_numeric(
    inventory_df["Demand"],
    errors="coerce"
)

inventory_df["Current_Stock"] = pd.to_numeric(
    inventory_df["Current_Stock"],
    errors="coerce"
)

# =====================================
# SAFETY STOCK
# =====================================

inventory_df["Safety_Stock"] = (
    inventory_df["Demand"] * 0.20
).round(0)

# =====================================
# REORDER POINT
# =====================================

inventory_df["Reorder_Point"] = (
    inventory_df["Demand"] * 0.50
    + inventory_df["Safety_Stock"]
).round(0)

# =====================================
# INVENTORY STATUS
# =====================================

def get_status(stock, reorder):

    if stock <= reorder * 0.5:
        return "Critical"

    elif stock <= reorder:
        return "Low"

    else:
        return "Healthy"

inventory_df["Status"] = inventory_df.apply(
    lambda row:
    get_status(
        row["Current_Stock"],
        row["Reorder_Point"]
    ),
    axis=1
)

# =====================================
# KPI SECTION
# =====================================

total_stock = inventory_df[
    "Current_Stock"
].sum()

total_safety_stock = inventory_df[
    "Safety_Stock"
].sum()

total_reorder = inventory_df[
    "Reorder_Point"
].sum()

products = inventory_df.shape[0]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Current Stock",
        int(total_stock)
    )

with col2:
    st.metric(
        "Safety Stock",
        int(total_safety_stock)
    )

with col3:
    st.metric(
        "Reorder Point",
        int(total_reorder)
    )

with col4:
    st.metric(
        "Products",
        products
    )

st.markdown("---")

# =====================================
# INVENTORY TABLE
# =====================================

st.subheader("📋 Inventory Overview")

st.dataframe(
    inventory_df,
    use_container_width=True
)

# =====================================
# CURRENT STOCK
# =====================================

st.subheader("📦 Current Stock Levels")

fig = px.bar(
    inventory_df,
    x="Product",
    y="Current_Stock",
    color="Current_Stock",
    text_auto=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# SAFETY STOCK
# =====================================

st.subheader("🛡 Safety Stock")

fig = px.bar(
    inventory_df,
    x="Product",
    y="Safety_Stock",
    color="Safety_Stock",
    text_auto=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# REORDER POINT
# =====================================

st.subheader("🔄 Reorder Point")

fig = px.bar(
    inventory_df,
    x="Product",
    y="Reorder_Point",
    color="Reorder_Point",
    text_auto=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# STATUS PIE CHART
# =====================================

st.subheader("📊 Inventory Health")

status_df = (
    inventory_df.groupby("Status")
    .size()
    .reset_index(name="Count")
)

fig = px.pie(
    status_df,
    names="Status",
    values="Count",
    hole=0.5
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# STOCK VS REORDER
# =====================================

st.subheader("📈 Stock vs Reorder Point")

comparison_df = inventory_df[
    [
        "Product",
        "Current_Stock",
        "Reorder_Point"
    ]
]

comparison_df = comparison_df.melt(
    id_vars="Product",
    var_name="Type",
    value_name="Value"
)

fig = px.bar(
    comparison_df,
    x="Product",
    y="Value",
    color="Type",
    barmode="group"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# HISTOGRAM
# =====================================

st.subheader("📉 Stock Distribution")

fig = px.histogram(
    inventory_df,
    x="Current_Stock",
    nbins=10
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# BOXPLOT
# =====================================

st.subheader("📦 Inventory Boxplot")

fig = px.box(
    inventory_df,
    y="Current_Stock",
    points="all"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# LOW STOCK
# =====================================

st.subheader("⚠ Low Stock Products")

low_stock = inventory_df[
    inventory_df["Status"] == "Low"
]

if len(low_stock) > 0:

    st.dataframe(
        low_stock,
        use_container_width=True
    )

else:

    st.success(
        "No Low Stock Products"
    )

# =====================================
# CRITICAL STOCK
# =====================================

st.subheader("🚨 Critical Stock Products")

critical_stock = inventory_df[
    inventory_df["Status"] == "Critical"
]

if len(critical_stock) > 0:

    st.dataframe(
        critical_stock,
        use_container_width=True
    )

else:

    st.success(
        "No Critical Products"
    )

# =====================================
# HEALTHY PRODUCTS
# =====================================

st.subheader("✅ Healthy Products")

healthy = inventory_df[
    inventory_df["Status"] == "Healthy"
]

st.dataframe(
    healthy,
    use_container_width=True
)

# =====================================
# SUMMARY TABLE
# =====================================

st.subheader("📊 Product Status Summary")

summary = (
    inventory_df.groupby("Status")
    .size()
    .reset_index(name="Products")
)

st.dataframe(
    summary,
    use_container_width=True
)

# =====================================
# DOWNLOAD REPORT
# =====================================

csv = inventory_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇ Download Inventory Report",
    data=csv,
    file_name="inventory_report.csv",
    mime="text/csv"
)

# =====================================
# INSIGHTS
# =====================================

st.markdown("---")

critical_count = len(
    inventory_df[
        inventory_df["Status"] == "Critical"
    ]
)

low_count = len(
    inventory_df[
        inventory_df["Status"] == "Low"
    ]
)

healthy_count = len(
    inventory_df[
        inventory_df["Status"] == "Healthy"
    ]
)

report_df = pd.DataFrame({

    "Metric": [
        "Healthy Products",
        "Low Stock Products",
        "Critical Products",
        "Total Products"
    ],

    "Value": [
        healthy_count,
        low_count,
        critical_count,
        products
    ]
})

st.dataframe(
    report_df,
    use_container_width=True
)

st.success("""
✔ Safety Stock Calculated

✔ Reorder Point Generated

✔ Inventory Health Analyzed

✔ Stock Alerts Generated

✔ Inventory Optimization Completed
""")