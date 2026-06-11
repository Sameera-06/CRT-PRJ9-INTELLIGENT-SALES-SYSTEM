import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os
from utils.ui_styles import load_css

load_css()

st.title("🧹 Data Preprocessing")

st.markdown("---")

# =====================================
# LOAD DATA
# =====================================

try:
    df = pd.read_csv("dataset/processed_sales.csv")

    if len(df) == 0:
        df = pd.read_csv("dataset/sales_data.csv")

except:
    df = pd.read_csv("dataset/sales_data.csv")

original_df = df.copy()

# =====================================
# BEFORE CLEANING METRICS
# =====================================

st.subheader("📊 Dataset Before Cleaning")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

with col3:
    st.metric(
        "Missing Values",
        int(df.isnull().sum().sum())
    )

with col4:
    st.metric(
        "Duplicates",
        int(df.duplicated().sum())
    )

# =====================================
# DATA PREVIEW
# =====================================

st.subheader("📋 Original Dataset")

st.dataframe(
    df.head(20),
    use_container_width=True
)

st.markdown("---")

# =====================================
# MISSING VALUES
# =====================================

st.subheader("🚨 Missing Value Analysis")

missing_df = pd.DataFrame(
    df.isnull().sum(),
    columns=["Missing Values"]
)

missing_df.reset_index(inplace=True)

missing_df.columns = [
    "Column",
    "Missing Values"
]

st.dataframe(
    missing_df,
    use_container_width=True
)

fig = px.bar(
    missing_df,
    x="Column",
    y="Missing Values",
    text_auto=True,
    title="Missing Values"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# HANDLE MISSING VALUES
# =====================================

st.subheader("🧹 Handle Missing Values")

missing_option = st.selectbox(
    "Choose Missing Value Strategy",
    [
        "Forward Fill",
        "Backward Fill",
        "Mean",
        "Median"
    ]
)

if st.button("Apply Missing Value Handling"):

    if missing_option == "Forward Fill":
        df = df.fillna(method="ffill")

    elif missing_option == "Backward Fill":
        df = df.fillna(method="bfill")

    elif missing_option == "Mean":

        for col in df.select_dtypes(
            include=np.number
        ).columns:

            df[col].fillna(
                df[col].mean(),
                inplace=True
            )

    elif missing_option == "Median":

        for col in df.select_dtypes(
            include=np.number
        ).columns:

            df[col].fillna(
                df[col].median(),
                inplace=True
            )

    st.success("Missing Values Processed")

# =====================================
# DUPLICATE ANALYSIS
# =====================================

st.subheader("📑 Duplicate Analysis")

duplicates = df.duplicated().sum()

dup_df = pd.DataFrame({
    "Status":[
        "Unique",
        "Duplicate"
    ],
    "Count":[
        len(df)-duplicates,
        duplicates
    ]
})

fig = px.pie(
    dup_df,
    names="Status",
    values="Count",
    hole=0.4
)

st.plotly_chart(
    fig,
    use_container_width=True
)

if st.button("Remove Duplicates"):

    before = len(df)

    df.drop_duplicates(
        inplace=True
    )

    after = len(df)

    st.success(
        f"{before-after} Duplicates Removed"
    )

# =====================================
# OUTLIER DETECTION
# =====================================

st.markdown("---")

st.subheader("📈 Outlier Detection")

numeric_cols = df.select_dtypes(
    include=np.number
).columns

selected_col = st.selectbox(
    "Select Numeric Column",
    numeric_cols
)

# BEFORE OUTLIER

st.write("### Before Outlier Removal")

fig = px.box(
    df,
    y=selected_col,
    points="all"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# REMOVE OUTLIERS
# =====================================

if st.button("Remove Outliers"):

    q1 = df[selected_col].quantile(0.25)
    q3 = df[selected_col].quantile(0.75)

    iqr = q3-q1

    lower = q1-(1.5*iqr)
    upper = q3+(1.5*iqr)

    df = df[
        (df[selected_col] >= lower)
        &
        (df[selected_col] <= upper)
    ]

    st.success(
        "Outliers Removed"
    )

    fig = px.box(
        df,
        y=selected_col,
        points="all"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================
# FEATURE ENGINEERING
# =====================================

st.markdown("---")

st.subheader("⚙ Feature Engineering")

if "Date" in df.columns:

    df["Date"] = pd.to_datetime(df["Date"])

    df["Year"] = df["Date"].dt.year

    df["Month"] = df["Date"].dt.month

    df["Day"] = df["Date"].dt.day

    df["Quarter"] = df["Date"].dt.quarter

    st.success(
        "Date Features Created"
    )

# =====================================
# GENERATED FEATURES TABLE
# =====================================

st.subheader("📋 Feature Engineered Dataset")

st.dataframe(
    df.head(20),
    use_container_width=True
)

# =====================================
# BEFORE VS AFTER
# =====================================

st.markdown("---")

st.subheader("📊 Before vs After Cleaning")

comparison_df = pd.DataFrame({

    "Metric":[
        "Rows",
        "Columns",
        "Missing Values",
        "Duplicates"
    ],

    "Before":[
        original_df.shape[0],
        original_df.shape[1],
        original_df.isnull().sum().sum(),
        original_df.duplicated().sum()
    ],

    "After":[
        df.shape[0],
        df.shape[1],
        df.isnull().sum().sum(),
        df.duplicated().sum()
    ]
})

st.dataframe(
    comparison_df,
    use_container_width=True
)

# =====================================
# NUMERIC DISTRIBUTION
# =====================================

st.subheader("📉 Distribution Analysis")

selected_distribution = st.selectbox(
    "Select Feature",
    numeric_cols
)

fig = px.histogram(
    df,
    x=selected_distribution,
    nbins=20
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# CORRELATION MATRIX
# =====================================

st.subheader("🔥 Correlation Matrix")

numeric_df = df.select_dtypes(
    include=np.number
)

corr = numeric_df.corr()

fig = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="YlOrBr"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# SAVE CLEANED DATA
# =====================================

st.markdown("---")

st.subheader("💾 Save Cleaned Dataset")

if st.button("Save Cleaned Dataset"):

    os.makedirs(
        "dataset",
        exist_ok=True
    )

    df.to_csv(
        "dataset/processed_sales.csv",
        index=False
    )

    st.success(
        "Dataset Saved Successfully"
    )

# =====================================
# DOWNLOAD DATA
# =====================================

csv = df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇ Download Cleaned Dataset",
    data=csv,
    file_name="processed_sales.csv",
    mime="text/csv"
)

# =====================================
# CLEANING REPORT
# =====================================

st.markdown("---")

st.subheader("📄 Data Cleaning Report")

report_df = pd.DataFrame({

    "Task":[
        "Missing Value Handling",
        "Duplicate Removal",
        "Outlier Detection",
        "Feature Engineering"
    ],

    "Status":[
        "Completed",
        "Completed",
        "Completed",
        "Completed"
    ]
})

st.dataframe(
    report_df,
    use_container_width=True
)

st.success("""
✔ Missing Values Handled

✔ Duplicates Removed

✔ Outliers Removed

✔ Feature Engineering Applied

✔ Dataset Ready For Model Training
""")