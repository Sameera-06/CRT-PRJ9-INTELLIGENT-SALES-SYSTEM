import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np
from utils.ui_styles import load_css

load_css()

st.title("🔍 Exploratory Data Analysis (EDA)")

# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv("dataset/sales_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

# =====================================
# DATASET OVERVIEW
# =====================================

st.subheader("📋 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

with col3:
    st.metric("Products", df["Product"].nunique())

with col4:
    st.metric("Regions", df["Region"].nunique())

st.markdown("---")

# =====================================
# RAW DATA
# =====================================

st.subheader("📄 Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

# =====================================
# DATA TYPES
# =====================================

st.subheader("📌 Column Information")

info_df = pd.DataFrame({
    "Column": df.columns,
    "Datatype": df.dtypes.astype(str)
})

st.dataframe(
    info_df,
    use_container_width=True
)

# =====================================
# DESCRIPTIVE STATISTICS
# =====================================

st.subheader("📊 Descriptive Statistics")

st.dataframe(
    df.describe(),
    use_container_width=True
)

# =====================================
# MISSING VALUES
# =====================================

st.subheader("🚨 Missing Values Analysis")

missing_df = pd.DataFrame(
    df.isnull().sum(),
    columns=["Missing Values"]
)

missing_df.reset_index(inplace=True)
missing_df.columns = ["Column", "Missing Values"]

fig = px.bar(
    missing_df,
    x="Column",
    y="Missing Values",
    text_auto=True,
    title="Missing Values by Column"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# CORRELATION HEATMAP
# =====================================

st.subheader("🔥 Correlation Heatmap")

numeric_df = df.select_dtypes(include=np.number)

corr = numeric_df.corr()

heatmap = go.Figure(
    data=go.Heatmap(
        z=corr.values,
        x=corr.columns,
        y=corr.columns,
        text=np.round(corr.values, 2),
        texttemplate="%{text}",
        colorscale="YlOrBr"
    )
)

heatmap.update_layout(
    height=600
)

st.plotly_chart(
    heatmap,
    use_container_width=True
)

# =====================================
# REVENUE HISTOGRAM
# =====================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("📈 Revenue Distribution")

    fig = px.histogram(
        df,
        x="Revenue",
        nbins=20,
        title="Revenue Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader("📈 Profit Distribution")

    fig = px.histogram(
        df,
        x="Profit",
        nbins=20,
        title="Profit Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================
# BOXPLOTS
# =====================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("📦 Revenue Boxplot")

    fig = px.box(
        df,
        y="Revenue",
        points="all"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader("📦 Profit Boxplot")

    fig = px.box(
        df,
        y="Profit",
        points="all"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================
# REGION ANALYSIS
# =====================================

st.subheader("🌎 Revenue by Region")

region_df = (
    df.groupby("Region")["Revenue"]
    .sum()
    .reset_index()
)

fig = px.pie(
    region_df,
    names="Region",
    values="Revenue",
    hole=0.4
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# CATEGORY ANALYSIS
# =====================================

st.subheader("📦 Revenue by Category")

category_df = (
    df.groupby("Category")["Revenue"]
    .sum()
    .reset_index()
)

fig = px.bar(
    category_df,
    x="Category",
    y="Revenue",
    color="Category",
    text_auto=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# TOP PRODUCTS
# =====================================

st.subheader("🏆 Top Products")

product_df = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig = px.bar(
    product_df,
    x="Revenue",
    y="Product",
    orientation="h",
    text_auto=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# REVENUE VS PROFIT
# =====================================

st.subheader("💰 Revenue vs Profit")

fig = px.scatter(
    df,
    x="Revenue",
    y="Profit",
    size="Quantity",
    color="Category",
    hover_name="Product"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# MONTHLY REVENUE
# =====================================

st.subheader("📅 Monthly Revenue Trend")

df["Month"] = df["Date"].dt.strftime("%b")

monthly_df = (
    df.groupby("Month")["Revenue"]
    .sum()
    .reset_index()
)

fig = px.line(
    monthly_df,
    x="Month",
    y="Revenue",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# INVENTORY ANALYSIS
# =====================================

st.subheader("📦 Inventory Analysis")

inventory_df = (
    df.groupby("Product")["Current_Stock"]
    .sum()
    .reset_index()
)

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
# INVENTORY TABLE
# =====================================

st.subheader("📋 Inventory Table")

st.dataframe(
    inventory_df,
    use_container_width=True
)

# =====================================
# SALES SUMMARY TABLE
# =====================================

st.subheader("📑 Product Performance")

summary_df = (
    df.groupby("Product")
    .agg({
        "Revenue":"sum",
        "Profit":"sum",
        "Quantity":"sum"
    })
    .reset_index()
)

st.dataframe(
    summary_df,
    use_container_width=True
)

# =====================================
# EDA INSIGHTS
# =====================================

st.markdown("---")

st.success("""
EDA Completed Successfully

✔ Revenue Trends Analyzed

✔ Product Performance Analyzed

✔ Inventory Analysis Completed

✔ Correlation Analysis Completed

✔ Outlier Detection Visualized
""")