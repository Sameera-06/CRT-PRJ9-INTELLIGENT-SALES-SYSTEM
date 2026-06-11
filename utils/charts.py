import plotly.express as px

def revenue_line_chart(df):

    return px.line(
        df,
        x="Date",
        y="Revenue",
        markers=True,
        title="Revenue Trend"
    )

def revenue_pie_chart(df):

    region_df = (
        df.groupby("Region")
        ["Revenue"]
        .sum()
        .reset_index()
    )

    return px.pie(
        region_df,
        names="Region",
        values="Revenue",
        hole=0.4
    )

def product_bar_chart(df):

    product_df = (
        df.groupby("Product")
        ["Revenue"]
        .sum()
        .reset_index()
    )

    return px.bar(
        product_df,
        x="Product",
        y="Revenue",
        color="Revenue"
    )

def revenue_histogram(df):

    return px.histogram(
        df,
        x="Revenue",
        nbins=20
    )

def profit_boxplot(df):

    return px.box(
        df,
        y="Profit",
        points="all"
    )

def revenue_profit_scatter(df):

    return px.scatter(
        df,
        x="Revenue",
        y="Profit",
        size="Quantity",
        color="Category"
    )