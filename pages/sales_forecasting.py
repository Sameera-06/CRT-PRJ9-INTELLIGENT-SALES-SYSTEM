import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib
import os
from utils.ui_styles import load_css

load_css()
from datetime import timedelta

st.title("📈 Sales Forecasting")

st.markdown("---")

# =====================================
# LOAD DATA
# =====================================

try:
    df = pd.read_csv("dataset/processed_sales.csv")
except:
    df = pd.read_csv("dataset/sales_data.csv")

# =====================================
# DATE PROCESSING
# =====================================

df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["Quarter"] = df["Date"].dt.quarter

# =====================================
# LOAD MODEL
# =====================================

st.subheader("Model Status")

try:

    model = joblib.load(
        "model/sales_forecast_model.pkl"
    )

    st.success(
        "Trained Model Loaded Successfully"
    )

except:

    st.error(
        "Model Not Found. Train Model First."
    )

    st.stop()

# =====================================
# HISTORICAL DATA
# =====================================

st.subheader("Historical Sales Data")

st.dataframe(
    df.head(20),
    use_container_width=True
)

# =====================================
# KPI SECTION
# =====================================

total_revenue = df["Revenue"].sum()

avg_revenue = df["Revenue"].mean()

total_orders = len(df)

products = df["Product"].nunique()

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "Revenue",
        f"₹{total_revenue:,.0f}"
    )

with col2:
    st.metric(
        "Average Revenue",
        f"₹{avg_revenue:,.0f}"
    )

with col3:
    st.metric(
        "Orders",
        total_orders
    )

with col4:
    st.metric(
        "Products",
        products
    )

st.markdown("---")

# =====================================
# FORECAST PERIOD
# =====================================

st.subheader("Forecast Configuration")

forecast_days = st.slider(
    "Forecast Future Days",
    7,
    90,
    30
)

# =====================================
# CREATE FUTURE DATA
# =====================================

last_date = df["Date"].max()

future_dates = pd.date_range(
    start=last_date + timedelta(days=1),
    periods=forecast_days
)

future_df = pd.DataFrame({
    "Date": future_dates
})

future_df["Year"] = future_df["Date"].dt.year
future_df["Month"] = future_df["Date"].dt.month
future_df["Day"] = future_df["Date"].dt.day
future_df["Quarter"] = future_df["Date"].dt.quarter

# =====================================
# MODEL FEATURES
# =====================================

required_features = [
    "Year",
    "Month",
    "Day",
    "Quarter"
]

# =====================================
# FORECAST
# =====================================

forecast_values = model.predict(
    future_df[required_features]
)

future_df["Forecast_Revenue"] = forecast_values

# =====================================
# FORECAST KPI
# =====================================

st.subheader("Forecast Summary")

forecast_total = future_df[
    "Forecast_Revenue"
].sum()

forecast_avg = future_df[
    "Forecast_Revenue"
].mean()

forecast_max = future_df[
    "Forecast_Revenue"
].max()

growth = (
    (
        forecast_avg -
        avg_revenue
    )
    /
    avg_revenue
) * 100

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "Forecast Revenue",
        f"₹{forecast_total:,.0f}"
    )

with c2:
    st.metric(
        "Avg Forecast",
        f"₹{forecast_avg:,.0f}"
    )

with c3:
    st.metric(
        "Max Forecast",
        f"₹{forecast_max:,.0f}"
    )

with c4:
    st.metric(
        "Growth %",
        f"{growth:.2f}%"
    )

st.markdown("---")

# =====================================
# HISTORICAL TREND
# =====================================

st.subheader("Historical Revenue Trend")

historical = (
    df.groupby("Date")["Revenue"]
    .sum()
    .reset_index()
)

fig = px.line(
    historical,
    x="Date",
    y="Revenue",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# FORECAST TREND
# =====================================

st.subheader("Forecast Revenue Trend")

fig = px.line(
    future_df,
    x="Date",
    y="Forecast_Revenue",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# HISTORICAL VS FORECAST
# =====================================

st.subheader("Historical vs Forecast")

historical_plot = historical.copy()

historical_plot.columns = [
    "Date",
    "Value"
]

historical_plot["Type"] = "Historical"

forecast_plot = future_df[
    ["Date","Forecast_Revenue"]
].copy()

forecast_plot.columns = [
    "Date",
    "Value"
]

forecast_plot["Type"] = "Forecast"

combined = pd.concat(
    [
        historical_plot,
        forecast_plot
    ]
)

fig = px.line(
    combined,
    x="Date",
    y="Value",
    color="Type"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# FORECAST DISTRIBUTION
# =====================================

st.subheader("Forecast Distribution")

fig = px.histogram(
    future_df,
    x="Forecast_Revenue",
    nbins=20
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# FORECAST BOXPLOT
# =====================================

st.subheader("Forecast Box Plot")

fig = px.box(
    future_df,
    y="Forecast_Revenue"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# MONTHLY FORECAST
# =====================================

st.subheader("Monthly Forecast Summary")

future_df["Month_Name"] = (
    future_df["Date"]
    .dt.strftime("%b")
)

monthly_forecast = (
    future_df.groupby(
        "Month_Name"
    )["Forecast_Revenue"]
    .sum()
    .reset_index()
)

fig = px.bar(
    monthly_forecast,
    x="Month_Name",
    y="Forecast_Revenue",
    text_auto=True,
    color="Forecast_Revenue"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# FORECAST TABLE
# =====================================

st.subheader("Forecast Data")

st.dataframe(
    future_df,
    use_container_width=True
)

# =====================================
# TOP FORECAST DAYS
# =====================================

st.subheader("Top Forecast Days")

top_days = future_df.sort_values(
    "Forecast_Revenue",
    ascending=False
).head(10)

st.dataframe(
    top_days,
    use_container_width=True
)

# =====================================
# DOWNLOAD FORECAST
# =====================================

csv = future_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇ Download Forecast CSV",
    data=csv,
    file_name="forecast_results.csv",
    mime="text/csv"
)

# =====================================
# FORECAST REPORT
# =====================================

st.markdown("---")

st.subheader("Forecast Report")

report_df = pd.DataFrame({

    "Metric":[
        "Forecast Days",
        "Forecast Revenue",
        "Average Forecast",
        "Growth %"
    ],

    "Value":[
        forecast_days,
        round(forecast_total,2),
        round(forecast_avg,2),
        round(growth,2)
    ]
})

st.dataframe(
    report_df,
    use_container_width=True
)

st.success("""
✔ Forecast Generated

✔ Future Revenue Predicted

✔ Growth Analysis Completed

✔ Forecast Dashboard Ready

✔ CSV Download Available
""")