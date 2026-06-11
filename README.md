# 📊 AI Intelligent Sales Forecasting & Inventory Optimization System

## 🚀 Project Overview

AI Intelligent Sales Forecasting & Inventory Optimization System is a Business Intelligence and Machine Learning application developed using Streamlit, Python, and Scikit-Learn.

The system helps organizations analyze sales performance, forecast future revenue, optimize inventory levels, generate business reports, and make data-driven decisions through interactive dashboards and visualizations.

---

## 🎯 Objectives

* Analyze historical sales performance
* Forecast future sales using Machine Learning
* Optimize inventory levels
* Calculate Safety Stock and Reorder Points
* Generate business intelligence reports
* Visualize KPIs through interactive dashboards

---

## ✨ Features

### 📤 Data Upload

* Upload CSV datasets
* Dataset preview
* Data validation
* File information

### 🧹 Data Preprocessing

* Missing value handling
* Duplicate removal
* Outlier detection
* Outlier removal
* Feature engineering
* Data quality analysis

### 📊 Exploratory Data Analysis (EDA)

* Revenue analysis
* Profit analysis
* Product analysis
* Category analysis
* Region analysis
* Correlation heatmaps
* Histograms
* Boxplots
* Scatter plots
* Pie charts
* Donut charts

### 🤖 Model Training

* Random Forest Regression
* Train/Test Split
* MAE Calculation
* RMSE Calculation
* R² Score Evaluation
* Feature Importance Analysis
* Actual vs Predicted Visualization
* Residual Analysis

### 📈 Sales Forecasting

* Revenue prediction
* Historical vs Forecast comparison
* Growth analysis
* Forecast dashboard
* Forecast KPI monitoring
* Monthly forecast analysis

### 📦 Inventory Optimization

* Safety Stock Calculation
* Reorder Point Calculation
* Inventory Health Monitoring
* Stock Alerts
* Critical Stock Detection
* Low Stock Analysis
* Inventory KPIs

### 📄 Reports

* Executive Summary
* Sales Reports
* Inventory Reports
* PDF Report Generation
* CSV Export

### 📋 Dashboard

* KPI Monitoring
* Revenue Tracking
* Sales Performance
* Inventory Status
* Interactive Business Insights

---

## 🛠️ Technologies Used

### Frontend

* Streamlit

### Data Processing

* Pandas
* NumPy

### Data Visualization

* Plotly
* Matplotlib

### Machine Learning

* Scikit-Learn
* Random Forest Regressor

### Reporting

* ReportLab

### Database

* SQLite

---

## 📂 Project Structure

```text
intelligent-sales-system/
│
├── app.py
├── requirements.txt
├── README.md
│
├── dashboard/
│   ├── forecast_dashboard.py
│   ├── inventory_dashboard.py
│   ├── kpi_dashboard.py
│   ├── inventory_analysis.py
│   └── sales_analysis.py
│
├── database/
│   ├── create_tables.py
│   ├── data_operations.py
│   ├── database_connection.py
│   └── sales.db
│
├── dataset/
│   ├── processed_sales.csv
│   ├── sales_data.csv
│   └── sample_sales_data.csv
│
├── inventory_optimizer/
│   ├── reorder_calculator.py
│   ├── safety_stock.py
│   └── stock_alerts.py
│
├── model/
│   ├── evaluation.py
│   ├── model_loader.py
│   ├── predict.py
│   ├── sales_forecast_model.pkl
│   └── train_model.py
│
├── pages/
│   ├── data_upload.py
│   ├── data_preprocessing.py
│   ├── eda_analysis.py
│   ├── model_training.py
│   ├── sales_forecasting.py
│   ├── inventory_optimization.py
│   ├── reports.py
│   └── dashboard.py
│
├── preprocessing/
│   ├── data_cleaning.py
│   ├── outlier_handler.py
│   ├── feature_engineering.py
│   └── preprocessing_pipeline.py
│
├── reports/
│   ├── generate_pdf_report.py
│   └── report_templates.py
│
└── utils/
    ├── charts.py
    ├── constants.py
    ├── file_manager.py
    ├── helper_functions.py
    ├── logger.py
    ├── ui_components.py
    └── ui_styles.py
```

---

## 📈 Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Feature Engineering
4. Train-Test Split
5. Random Forest Model Training
6. Model Evaluation
7. Forecast Generation
8. Inventory Optimization
9. Report Generation

---

## 📊 Evaluation Metrics

### Mean Absolute Error (MAE)

Measures average prediction error.

### Root Mean Square Error (RMSE)

Measures model prediction accuracy.

### R² Score

Measures goodness of fit.

---

## 📦 Inventory Optimization Logic

### Safety Stock

Safety Stock helps prevent stockouts during unexpected demand spikes.

### Reorder Point

Reorder Point determines when inventory should be replenished.

Formula:

Reorder Point = Average Demand + Safety Stock

---

## 🎨 Dashboard Components

* KPI Cards
* Revenue Trend Analysis
* Product Performance
* Regional Analysis
* Forecast Charts
* Inventory Health Dashboard
* Correlation Heatmaps
* Interactive Filters

---

## 📥 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Intelligent-Sales-System.git
```

### Navigate to Project

```bash
cd AI-Intelligent-Sales-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📷 Output Screens
<img width="1919" height="914" alt="Screenshot 2026-06-11 182127" src="https://github.com/user-attachments/assets/009c79c1-ab93-4225-bc1f-4fb4dedb4935" />


* Home Dashboard
* KPI Dashboard
* EDA Analysis Dashboard
* Model Training Dashboard
* Sales Forecast Dashboard
* Inventory Optimization Dashboard
* Reports Dashboard

---

## 🌟 Key Benefits

* Improved Sales Planning
* Better Inventory Management
* Reduced Stock-Out Risk
* Enhanced Decision Making
* Interactive Business Intelligence
* Automated Forecasting

---

## 👨‍💻 Developed By

Sameera.sk

AI Intelligent Sales Forecasting & Inventory Optimization System

Built using Python, Streamlit, Machine Learning, Business Intelligence, and Data Analytics.

---

Live Link : https://crt-prj9-intelligent-sales-system.onrender.com


---
