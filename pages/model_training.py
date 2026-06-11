import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib
import os
from utils.ui_styles import load_css

load_css()

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

st.title("🤖 Model Training")

st.markdown("---")

# ==========================================
# LOAD DATA
# ==========================================

if (
    os.path.exists("dataset/processed_sales.csv")
    and
    len(pd.read_csv("dataset/processed_sales.csv")) > 0
):

    df = pd.read_csv(
        "dataset/processed_sales.csv"
    )

else:

    df = pd.read_csv(
        "dataset/sales_data.csv"
    )

# ==========================================
# DATE PROCESSING
# ==========================================

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

df = df.dropna(
    subset=["Date"]
)

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["Quarter"] = df["Date"].dt.quarter

# ==========================================
# DATASET PREVIEW
# ==========================================

st.subheader("Dataset Used For Training")

st.dataframe(
    df.head(),
    use_container_width=True
)

# ==========================================
# KPI SECTION
# ==========================================

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "Rows",
        len(df)
    )

with c2:
    st.metric(
        "Products",
        df["Product"].nunique()
    )

with c3:
    st.metric(
        "Revenue",
        f"₹{df['Revenue'].sum():,.0f}"
    )

with c4:
    st.metric(
        "Profit",
        f"₹{df['Profit'].sum():,.0f}"
    )

st.markdown("---")

# ==========================================
# TARGET VARIABLE
# ==========================================

target = "Revenue"

st.info(
    f"Target Variable : {target}"
)

# ==========================================
# FEATURES
# ==========================================

feature_columns = [
    "Year",
    "Month",
    "Day",
    "Quarter"
]

st.info(
    f"Features Used : {', '.join(feature_columns)}"
)

# ==========================================
# TRAIN MODEL
# ==========================================

if st.button("🚀 Train Model"):

    X = df[feature_columns]

    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )

    # =====================================
    # SAVE MODEL IMMEDIATELY
    # =====================================

    os.makedirs(
        "model",
        exist_ok=True
    )

    model_path = (
        "model/sales_forecast_model.pkl"
    )

    joblib.dump(
        model,
        model_path
    )

    file_size = os.path.getsize(
        model_path
    )

    # =====================================
    # METRICS
    # =====================================

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_test,
            predictions
        )
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    st.subheader(
        "📊 Model Performance"
    )

    c1,c2,c3 = st.columns(3)

    with c1:
        st.metric(
            "MAE",
            f"{mae:,.2f}"
        )

    with c2:
        st.metric(
            "RMSE",
            f"{rmse:,.2f}"
        )

    with c3:
        st.metric(
            "R² Score",
            f"{r2:.4f}"
        )

    # =====================================
    # METRICS TABLE
    # =====================================

    st.subheader(
        "📋 Performance Summary"
    )

    metrics_df = pd.DataFrame({

        "Metric":[
            "MAE",
            "RMSE",
            "R² Score"
        ],

        "Value":[
            mae,
            rmse,
            r2
        ]
    })

    st.dataframe(
        metrics_df,
        use_container_width=True
    )

    # =====================================
    # ACTUAL VS PREDICTED
    # =====================================

    st.subheader(
        "📈 Actual vs Predicted"
    )

    comparison_df = pd.DataFrame({

        "Actual":
            y_test.values,

        "Predicted":
            predictions

    })

    fig = px.scatter(
        comparison_df,
        x="Actual",
        y="Predicted",
        color="Predicted"
    )

    fig.add_shape(
        type="line",
        x0=comparison_df[
            "Actual"
        ].min(),
        y0=comparison_df[
            "Actual"
        ].min(),
        x1=comparison_df[
            "Actual"
        ].max(),
        y1=comparison_df[
            "Actual"
        ].max()
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================
    # RESIDUAL PLOT
    # =====================================

    residuals = (
        y_test -
        predictions
    )

    st.subheader(
        "📉 Residual Analysis"
    )

    residual_df = pd.DataFrame({

        "Predicted":
            predictions,

        "Residual":
            residuals

    })

    fig = px.scatter(
        residual_df,
        x="Predicted",
        y="Residual",
        color="Residual"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================
    # RESIDUAL HISTOGRAM
    # =====================================

    st.subheader(
        "Residual Distribution"
    )

    fig = px.histogram(
        residuals,
        nbins=15
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================
    # FEATURE IMPORTANCE
    # =====================================

    st.subheader(
        "🔥 Feature Importance"
    )

    importance_df = pd.DataFrame({

        "Feature":
            feature_columns,

        "Importance":
            model.feature_importances_

    })

    fig = px.bar(
        importance_df,
        x="Feature",
        y="Importance",
        text_auto=True,
        color="Importance"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================
    # CORRELATION MATRIX
    # =====================================

    st.subheader(
        "🔥 Correlation Matrix"
    )

    corr = df[
        feature_columns +
        [target]
    ].corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale=
        "YlOrBr"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================
    # PREDICTION TABLE
    # =====================================

    st.subheader(
        "Prediction Results"
    )

    prediction_df = pd.DataFrame({

        "Actual":
            y_test.values,

        "Predicted":
            predictions,

        "Residual":
            residuals

    })

    st.dataframe(
        prediction_df,
        use_container_width=True
    )

    # =====================================
    # MODEL INFO
    # =====================================

    st.subheader(
        "📄 Model Information"
    )

    info_df = pd.DataFrame({

        "Parameter":[
            "Algorithm",
            "Train Rows",
            "Test Rows",
            "Features",
            "Model File Size"
        ],

        "Value":[
            "Random Forest",
            len(X_train),
            len(X_test),
            len(feature_columns),
            f"{file_size:,} bytes"
        ]
    })

    st.dataframe(
        info_df,
        use_container_width=True
    )

    # =====================================
    # DOWNLOAD MODEL
    # =====================================

    with open(
        model_path,
        "rb"
    ) as file:

        st.download_button(
            "⬇ Download Model",
            file,
            "sales_forecast_model.pkl",
            "application/octet-stream"
        )

    st.success(
        f"""
        ✔ Model Trained Successfully

        ✔ Model Saved Successfully

        ✔ File Size: {file_size:,} bytes

        ✔ Forecasting Page Ready
        """
    )