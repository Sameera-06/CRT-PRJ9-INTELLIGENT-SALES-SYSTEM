import streamlit as st
from utils.ui_styles import load_css

load_css()
# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Intelligent Sales System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* MAIN BACKGROUND */

.stApp{
    background: linear-gradient(
        135deg,
        #ff512f,
        #dd2476,
        #6a11cb
    );
}

/* SIDEBAR */

section[data-testid="stSidebar"]{
    background: rgba(17,24,39,0.95);
}

/* HEADINGS */

h1{
    color:white !important;
    text-align:center;
    font-size:50px !important;
    font-weight:bold !important;
}

h2,h3,h4,h5,h6{
    color:#FFE082 !important;
}

/* TEXT */

label,p,span,div{
    color:white;
}

/* GLASS KPI CARDS */

[data-testid="stMetric"]{

    background: rgba(255,255,255,0.12);

    backdrop-filter: blur(12px);

    border: 1px solid rgba(255,255,255,0.25);

    border-radius:20px;

    padding:15px;

    box-shadow:
    0px 8px 25px rgba(0,0,0,0.25);

}

/* INFO CARDS */

[data-testid="stInfo"]{

    background: rgba(255,255,255,0.10);

    backdrop-filter: blur(10px);

    border-radius:15px;

}

/* SUCCESS */

[data-testid="stSuccess"]{

    border-radius:15px;

}

/* BUTTONS */

.stButton button{

    background: linear-gradient(
        135deg,
        #FFD54F,
        #FFB300
    );

    color:black;

    font-weight:bold;

    border:none;

    border-radius:12px;

    height:50px;

    width:100%;
}

/* DATAFRAMES */

[data-testid="stDataFrame"]{

    border-radius:15px;

    overflow:hidden;

}

/* CONTAINER SPACING */

.block-container{
    padding-top:2rem;
}

/* FEATURE CARDS */

.feature-card{

    background: rgba(255,255,255,0.12);

    backdrop-filter: blur(10px);

    border: 1px solid rgba(255,255,255,0.20);

    border-radius:20px;

    padding:25px;

    min-height:200px;

    box-shadow:
    0px 8px 25px rgba(0,0,0,0.25);

}

/* HERO CARD */

.hero-card{

    background: rgba(255,255,255,0.12);

    backdrop-filter: blur(12px);

    border: 1px solid rgba(255,255,255,0.25);

    border-radius:25px;

    padding:30px;

    text-align:center;

    margin-bottom:20px;

    box-shadow:
    0px 8px 25px rgba(0,0,0,0.25);

}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HERO SECTION
# ==========================================

st.markdown("""
<div class="hero-card">

<h1>📊 AI Intelligent Sales Forecasting & Inventory Optimization</h1>

<h3>
Transforming Business Decisions Using AI & Machine Learning
</h3>

</div>
""", unsafe_allow_html=True)

# ==========================================
# KPI SECTION
# ==========================================

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Revenue",
        "₹12.5M",
        "▲ 12%"
    )

with col2:
    st.metric(
        "📦 Orders",
        "8,950",
        "▲ 8%"
    )

with col3:
    st.metric(
        "📈 Profit",
        "₹3.1M",
        "▲ 6%"
    )

with col4:
    st.metric(
        "🎯 Forecast Accuracy",
        "94%",
        "▲ 2%"
    )

st.markdown("---")

# ==========================================
# PROJECT OVERVIEW
# ==========================================

st.subheader("🚀 Project Overview")

st.info("""
This AI-powered platform helps businesses forecast future sales,
optimize inventory levels, monitor KPIs, generate reports and
deliver powerful business intelligence insights.
""")

st.markdown("---")

# ==========================================
# FEATURE CARDS
# ==========================================

c1,c2 = st.columns(2)

with c1:

    st.markdown("""
    <div class="feature-card">

    <h3>📈 Sales Forecasting</h3>

    <p>
    Predict future sales using Machine Learning models and
    identify revenue trends for better decision making.
    </p>

    <ul>
    <li>Revenue Forecasting</li>
    <li>Trend Analysis</li>
    <li>Growth Prediction</li>
    <li>Forecast Dashboard</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class="feature-card">

    <h3>📦 Inventory Optimization</h3>

    <p>
    Calculate Safety Stock, Reorder Points and monitor
    inventory health using intelligent analytics.
    </p>

    <ul>
    <li>Safety Stock</li>
    <li>Reorder Point</li>
    <li>Inventory Health</li>
    <li>Stock Alerts</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ==========================================
# MODULES
# ==========================================

st.subheader("🛠 Available Modules")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.success("📤 Data Upload")

with c2:
    st.success("🧹 Data Preprocessing")

with c3:
    st.success("📊 EDA Analysis")

with c4:
    st.success("🤖 Model Training")

c5,c6,c7,c8 = st.columns(4)

with c5:
    st.success("📈 Sales Forecasting")

with c6:
    st.success("📦 Inventory Optimization")

with c7:
    st.success("📄 Reports")

with c8:
    st.success("📋 Dashboard")

st.markdown("---")

# ==========================================
# NAVIGATION INFO
# ==========================================

st.warning("""
👈 Use the Streamlit navigation menu on the left to access all modules.
""")

st.success("✅ System Ready")