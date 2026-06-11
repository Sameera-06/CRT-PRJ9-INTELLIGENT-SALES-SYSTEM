import streamlit as st
import pandas as pd
import plotly.express as px
import os
from utils.ui_styles import load_css

load_css()

st.title("📂 Data Upload & Validation")

st.markdown("---")

# ==========================================
# FILE UPLOAD
# ==========================================

uploaded_file = st.file_uploader(
    "Upload Sales CSV File",
    type=["csv"]
)

# ==========================================
# DEFAULT DATASET
# ==========================================

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset Uploaded Successfully")

else:

    try:
        df = pd.read_csv("dataset/sales_data.csv")

        st.info(
            "No file uploaded. Using sales_data.csv"
        )

    except:

        st.warning(
            "Please upload a dataset."
        )

        st.stop()

# ==========================================
# BASIC INFORMATION
# ==========================================

st.subheader("📊 Dataset Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Rows",
        df.shape[0]
    )

with col2:
    st.metric(
        "Columns",
        df.shape[1]
    )

with col3:
    st.metric(
        "Missing Values",
        int(df.isnull().sum().sum())
    )

with col4:
    st.metric(
        "Duplicate Rows",
        int(df.duplicated().sum())
    )

st.markdown("---")

# ==========================================
# DATA PREVIEW
# ==========================================

st.subheader("📋 Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

# ==========================================
# COLUMN INFORMATION
# ==========================================

st.subheader("📌 Column Information")

column_info = pd.DataFrame({
    "Column Name": df.columns,
    "Data Type": df.dtypes.astype(str)
})

st.dataframe(
    column_info,
    use_container_width=True
)

# ==========================================
# MISSING VALUES TABLE
# ==========================================

st.subheader("🚨 Missing Values Table")

missing_values = pd.DataFrame(
    df.isnull().sum(),
    columns=["Missing Values"]
)

missing_values.reset_index(inplace=True)

missing_values.columns = [
    "Column",
    "Missing Values"
]

st.dataframe(
    missing_values,
    use_container_width=True
)

# ==========================================
# MISSING VALUES CHART
# ==========================================

st.subheader("📈 Missing Values Analysis")

fig = px.bar(
    missing_values,
    x="Column",
    y="Missing Values",
    text_auto=True,
    color="Missing Values",
    title="Missing Values by Column"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# DUPLICATE ANALYSIS
# ==========================================

st.subheader("📊 Duplicate Analysis")

duplicate_count = df.duplicated().sum()

duplicate_df = pd.DataFrame({
    "Status": [
        "Unique Rows",
        "Duplicate Rows"
    ],
    "Count": [
        len(df)-duplicate_count,
        duplicate_count
    ]
})

fig = px.pie(
    duplicate_df,
    names="Status",
    values="Count",
    hole=0.4,
    title="Duplicate Records"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# DESCRIPTIVE STATISTICS
# ==========================================

st.subheader("📑 Statistical Summary")

st.dataframe(
    df.describe(),
    use_container_width=True
)

# ==========================================
# REVENUE HISTOGRAM
# ==========================================

if "Revenue" in df.columns:

    st.subheader("💰 Revenue Distribution")

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

# ==========================================
# PROFIT HISTOGRAM
# ==========================================

if "Profit" in df.columns:

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

# ==========================================
# NUMERICAL COLUMNS
# ==========================================

numeric_cols = df.select_dtypes(
    include=["int64","float64"]
).columns

if len(numeric_cols) > 0:

    st.subheader("📊 Numerical Columns")

    selected_col = st.selectbox(
        "Select Column",
        numeric_cols
    )

    fig = px.box(
        df,
        y=selected_col,
        title=f"{selected_col} Boxplot"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================
# SAVE DATASET
# ==========================================

st.subheader("💾 Save Dataset")

if st.button("Save Dataset"):

    os.makedirs(
        "dataset",
        exist_ok=True
    )

    df.to_csv(
        "dataset/processed_sales.csv",
        index=False
    )

    st.success(
        "Dataset Saved Successfully!"
    )

# ==========================================
# DOWNLOAD DATASET
# ==========================================

st.subheader("⬇ Download Dataset")

csv = df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="sales_data.csv",
    mime="text/csv"
)

# ==========================================
# DATA QUALITY REPORT
# ==========================================

st.markdown("---")

st.subheader("📄 Data Quality Report")

quality_df = pd.DataFrame({

    "Metric": [
        "Rows",
        "Columns",
        "Missing Values",
        "Duplicate Rows"
    ],

    "Value": [
        df.shape[0],
        df.shape[1],
        int(df.isnull().sum().sum()),
        int(df.duplicated().sum())
    ]
})

st.dataframe(
    quality_df,
    use_container_width=True
)

# ==========================================
# COMPLETION MESSAGE
# ==========================================

st.success("""
✔ Dataset Loaded

✔ Dataset Validated

✔ Missing Values Analyzed

✔ Duplicate Records Analyzed

✔ Statistical Summary Generated

✔ Dataset Ready For Preprocessing
""")