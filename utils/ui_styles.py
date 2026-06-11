import streamlit as st

def load_css():

    st.markdown("""
    <style>

    /* APP BACKGROUND */

    .stApp{
        background: linear-gradient(
            135deg,
            #ff512f,
            #dd2476,
            #6a11cb
        );
    }

    /* SIDEBAR */

    [data-testid="stSidebar"]{
        background: rgba(17,24,39,0.95);
    }

    /* HEADINGS */

    h1{
        color:white !important;
        font-weight:bold !important;
    }

    h2,h3,h4,h5,h6{
        color:#FFE082 !important;
    }

    /* TEXT */

    p,label,span,div{
        color:white;
    }

    /* KPI CARDS */

    [data-testid="stMetric"]{

        background: rgba(255,255,255,0.12);

        backdrop-filter: blur(12px);

        border-radius:20px;

        border:1px solid rgba(255,255,255,0.20);

        padding:15px;

        box-shadow:
        0px 8px 25px rgba(0,0,0,0.25);

    }

    /* DATAFRAMES */

    [data-testid="stDataFrame"]{

        border-radius:15px;

        overflow:hidden;

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

    }

    /* DOWNLOAD BUTTONS */

    .stDownloadButton button{

        background: linear-gradient(
            135deg,
            #00E676,
            #00C853
        );

        color:white;

        font-weight:bold;

        border:none;

        border-radius:12px;
    }

    /* SUCCESS */

    [data-testid="stSuccess"]{

        border-radius:15px;

    }

    /* INFO */

    [data-testid="stInfo"]{

        border-radius:15px;

    }

    /* WARNING */

    [data-testid="stWarning"]{

        border-radius:15px;

    }

    /* SELECT BOX */

    .stSelectbox div{

        border-radius:10px;

    }

    /* SLIDER */

    .stSlider{

        padding-top:10px;

    }

    /* PLOTLY */

    .js-plotly-plot{

        border-radius:20px;

    }

    </style>
    """, unsafe_allow_html=True)