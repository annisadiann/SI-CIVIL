import streamlit as st
import base64
import os
from streamlit_option_menu import option_menu

st.set_page_config(page_title="SI-CIVIL", layout="wide", initial_sidebar_state="expanded")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_b64 = ""
if os.path.exists("sivil.jpg"):
    img_b64 = get_base64_of_bin_file("sivil.jpg")

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif !important;
    }}

    .block-container {{
        padding-top: 3rem !important;
        max-width: 1200px !important;
    }}

    /* LATAR BELAKANG: Gambar latar terlihat jelas dengan overlay terang */
    .stApp {{
        background: linear-gradient(rgba(255, 255, 255, 0.75), rgba(248, 250, 252, 0.82)), url("data:image/jpeg;base64,{img_b64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* SIDEBAR PUTIH BERSIH */
    [data-testid="stSidebar"] {{
        background-color: #ffffff !important;
        border-right: 1px solid #cbd5e1 !important;
    }}
    
    [data-testid="stSidebarNav"] {{display: none;}}

    /* KOTAK INPUT, SELECTBOX, & NUMBER INPUT PUTIH BERSIH & TEKS GELAP */
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div,
    input, 
    .stSelectbox div[data-baseweb="select"],
    .stNumberInput div[data-baseweb="input"] {{
        background-color: #ffffff !important;
        background: #ffffff !important;
        color: #0f172a !important;
        -webkit-text-fill-color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
    }}
    
    div[data-baseweb="select"] span, 
    div[data-baseweb="select"] div,
    .stNumberInput input,
    .stTextInput input {{
        color: #0f172a !important;
        -webkit-text-fill-color: #0f172a !important;
    }}
    
    /* Dropdown list option */
    ul[role="listbox"] {{
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
    }}
    ul[role="listbox"] li span {{
        color: #0f172a !important;
    }}

    /* Label pilihan */
    .stRadio label p, .stRadio label span, .stSelectbox label p, .stNumberInput label p {{
        color: #0f172a !important;
        font-weight: 600 !important;
    }}

    /* TOMBOL UTAMA (PRIMARY BUTTON) */
    button[kind="primary"], div.stButton > button {{
        background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%) !important;
        background-color: #0284c7 !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }}
    button[kind="primary"]:hover, div.stButton > button:hover {{
        opacity: 0.9 !important;
        background: linear-gradient(135deg, #0284c7 0%, #1d4ed8 100%) !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }}

    /* MEMBUAT KOTAK PUTIH OTOMATIS PADA HASIL METRIK / ANGKA OUTPUT DI STREAMLIT */
    div[data-testid="stMetric"], div.stAlert, .result-box {{
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 12px !important;
        padding: 1.25rem !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03) !important;
    }}

    /* Tipografi Utama */
    .hero-title {{
        font-size: 4rem;
        font-weight: 800;
        color: #0f172a !important;
        letter-spacing: -0.03em;
        line-height: 1.1;
        margin-bottom: 0.5rem;
    }}
    .hero-title span {{
        background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    .hero-subtitle {{
        font-size: 1.15rem;
        color: #334155 !important;
        font-weight: 500;
        max-width: 650px;
        line-height: 1.6;
        margin-bottom: 3.5rem;
    }}

    /* Kartu Beranda */
    .card {{
        background: rgba(255, 255, 255, 0.95) !important;
        border: 1px solid rgba(0, 0, 0, 0.08);
        border-radius: 16px;
        padding: 2rem;
        height: 100%;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.03);
        transition: all 0.3s ease;
    }}
    .card:hover {{
        border-color: rgba(14, 165, 233, 0.4);
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
    }}
    .card-title {{
        font-size: 1.25rem;
        font-weight: 700;
        color: #0f172a !important;
        margin-bottom: 0.75rem;
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 0.75rem;
    }}
    .card-text {{
        font-size: 0.95rem;
        color: #475569 !important;
        line-height: 1.6;
        font-weight: 500;
    }}

    h1, h2, h3, h4, h5, h6, p, label, span {{
        color: #0f172a;
    }}

    #MainMenu, header, footer {{visibility: hidden;}}
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.markdown('<div style="font-size: 0.85rem; font-weight: 700; color: #0f172a; letter-spacing: 0.15em; margin-bottom: 15px; margin-left: 10px;">NAVIGASI SISTEM</div>', unsafe_allow_html=True)
    
    menu = option_menu(
        menu_title=None,
        options=["Beranda", "Struktur", "Material", "Hidrologi", "Geoteknik"],
        icons=["house", "calculator", "box", "droplet", "globe"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#ffffff"},
            "icon": {"color": "#0284c7", "font-size": "1.1rem"}, 
            "nav-link": {
                "font-size": "0.95rem", 
                "font-weight": "600",
                "color": "#0f172a",
                "text-align": "left", 
                "margin": "0px", 
                "--hover-color": "#f1f5f9",
                "border-radius": "8px",
                "padding": "12px 15px"
            },
            "nav-link-selected": {
                "background-color": "#e0f2fe",
                "color": "#0369a1",
                "border": "1px solid #bae6fd",
                "font-weight": "700"
            },
        }
    )

if menu == "Beranda":
    st.markdown('<div class="hero-title">Sistem Kalkulasi<br><span>Teknik Sipil.</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Platform komputasi terintegrasi untuk mendukung akurasi perhitungan struktur, analisis material, hidrologi, dan rekayasa geoteknik.</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1], gap="large")
    
    with col1:
        st.markdown("""
            <div class="card">
                <div class="card-title">Standarisasi SNI</div>
                <div class="card-text">Penerapan regulasi teknis terbaru untuk evaluasi mutu material beton, baja, dan kayu struktural.</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="card">
                <div class="card-title">Komputasi Struktur</div>
                <div class="card-text">Penyelesaian analisis tegangan normal, lentur, geser, serta deformasi regangan secara presisi.</div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="card">
                <div class="card-title">Analisis Tanah & Air</div>
                <div class="card-text">Kalkulasi kapasitas daya dukung Terzaghi, infiltrasi Horton, dan intensitas curah hujan kawasan.</div>
            </div>
        """, unsafe_allow_html=True)

elif menu == "Struktur":
    import struktur
    struktur.tampilkan()
elif menu == "Material":
    import material
    material.tampilkan()
elif menu == "Hidrologi":
    import hidrologi
    hidrologi.tampilkan()
elif menu == "Geoteknik":
    import geoteknik
    geoteknik.tampilkan()