import streamlit as st
import pandas as pd
import plotly.express as px
from reports.generate_pdf_report import generate_pdf_report
from utils.ui_styles import load_css
load_css()
st.title("📄 Business Reports")

try:
    df = pd.read_csv("dataset/processed_sales.csv")
except:
    df = pd.read_csv("dataset/sales_data.csv")

st.subheader("Executive Summary")

total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_orders = len(df)

c1,c2,c3 = st.columns(3)

c1.metric("Revenue",f"₹{total_revenue:,.0f}")
c2.metric("Profit",f"₹{total_profit:,.0f}")
c3.metric("Orders",total_orders)

st.markdown("---")

st.subheader("Revenue by Product")

product_df = (
    df.groupby("Product")["Revenue"]
    .sum()
    .reset_index()
)

fig = px.bar(
    product_df,
    x="Product",
    y="Revenue",
    color="Revenue"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Revenue by Region")

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

st.subheader("Detailed Report")

st.dataframe(
    df,
    use_container_width=True
)

if st.button("Generate PDF Report"):

    generate_pdf_report(df)

    with open(
        "reports/Sales_Report.pdf",
        "rb"
    ) as pdf:

        st.download_button(
            "⬇ Download PDF Report",
            pdf,
            "Sales_Report.pdf",
            "application/pdf"
        )

    st.success("Report Generated Successfully")