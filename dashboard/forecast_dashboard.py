import streamlit as st

def show_kpis(
sales,
revenue,
products
):

    c1,c2,c3=st.columns(3)

    c1.metric(
        "Total Sales",
        sales
    )

    c2.metric(
        "Revenue",
        revenue
    )

    c3.metric(
        "Products",
        products
    )