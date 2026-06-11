import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from utils.ui_styles import load_css

load_css()

st.title("📊 Executive Dashboard")

# ==========================
# LOAD DATA
# ==========================

df = pd.read_csv("dataset/sales_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

# ==========================
# SIDEBAR FILTERS
# ==========================

st.sidebar.header("Dashboard Filters")

region_filter = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category_filter = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[
    (df["Region"].isin(region_filter)) &
    (df["Category"].isin(category_filter))
]

# ==========================
# KPI SECTION
# ==========================

total_revenue = filtered_df["Revenue"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order_ID"].count()
total_products = filtered_df["Product"].nunique()

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Revenue",
        f"₹{total_revenue:,.0f}"
    )

with col2:
    st.metric(
        "📈 Profit",
        f"₹{total_profit:,.0f}"
    )

with col3:
    st.metric(
        "🛒 Orders",
        total_orders
    )

with col4:
    st.metric(
        "📦 Products",
        total_products
    )

st.markdown("---")

# ==========================
# REVENUE TREND
# ==========================

st.subheader("📈 Revenue Trend")

daily_revenue = (
    filtered_df.groupby("Date")["Revenue"]
    .sum()
    .reset_index()
)

fig = px.line(
    daily_revenue,
    x="Date",
    y="Revenue",
    markers=True,
    title="Revenue Over Time"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================
# MONTHLY SALES
# ==========================

st.subheader("📊 Monthly Sales")

filtered_df["Month"] = (
    filtered_df["Date"]
    .dt.strftime("%b")
)

monthly_sales = (
    filtered_df.groupby("Month")["Revenue"]
    .sum()
    .reset_index()
)

fig = px.bar(
    monthly_sales,
    x="Month",
    y="Revenue",
    text_auto=True,
    title="Monthly Revenue"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================
# PIE CHART
# ==========================

col1,col2 = st.columns(2)

with col1:

    st.subheader("🌎 Revenue by Region")

    region_sales = (
        filtered_df.groupby("Region")["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        region_sales,
        names="Region",
        values="Revenue",
        hole=0.4
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader("📦 Revenue by Category")

    category_sales = (
        filtered_df.groupby("Category")["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        category_sales,
        names="Category",
        values="Revenue"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================
# PRODUCT ANALYSIS
# ==========================

st.subheader("🏆 Top Products")

product_sales = (
    filtered_df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig = px.bar(
    product_sales,
    x="Revenue",
    y="Product",
    orientation="h",
    text_auto=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================
# PROFIT ANALYSIS
# ==========================

st.subheader("💹 Profit Analysis")

fig = px.bar(
    filtered_df,
    x="Product",
    y="Profit",
    color="Category",
    title="Profit by Product"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================
# HISTOGRAM
# ==========================

col1,col2 = st.columns(2)

with col1:

    st.subheader("Revenue Distribution")

    fig = px.histogram(
        filtered_df,
        x="Revenue",
        nbins=15
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader("Profit Distribution")

    fig = px.histogram(
        filtered_df,
        x="Profit",
        nbins=15
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================
# BOX PLOT
# ==========================

col1,col2 = st.columns(2)

with col1:

    st.subheader("Revenue Boxplot")

    fig = px.box(
        filtered_df,
        y="Revenue"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader("Profit Boxplot")

    fig = px.box(
        filtered_df,
        y="Profit"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================
# SCATTER PLOT
# ==========================

st.subheader("Revenue vs Profit")

fig = px.scatter(
    filtered_df,
    x="Revenue",
    y="Profit",
    color="Category",
    size="Quantity",
    hover_name="Product"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================
# INVENTORY ANALYSIS
# ==========================

st.subheader("📦 Inventory Status")

inventory_df = (
    filtered_df.groupby("Product")["Current_Stock"]
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

# ==========================
# TOP PRODUCTS TABLE
# ==========================

st.subheader("🏅 Top Products Table")

top_products = (
    filtered_df.groupby("Product")
    .agg({
        "Revenue":"sum",
        "Profit":"sum",
        "Quantity":"sum"
    })
    .reset_index()
    .sort_values(
        "Revenue",
        ascending=False
    )
)

st.dataframe(
    top_products,
    use_container_width=True
)

# ==========================
# RECENT TRANSACTIONS
# ==========================

st.subheader("📋 Recent Transactions")

st.dataframe(
    filtered_df.sort_values(
        "Date",
        ascending=False
    ),
    use_container_width=True
)

# ==========================
# SUMMARY
# ==========================

st.markdown("---")

st.success(
    "Dashboard Loaded Successfully"
)