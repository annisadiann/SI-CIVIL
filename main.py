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

    /* Latar belakang halaman utama */
    .stApp {{
        background: linear-gradient(rgba(255, 255, 255, 0.75), rgba(248, 250, 252, 0.85)), url("data:image/jpeg;base64,{img_b64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Sidebar Terang */
    [data-testid="stSidebar"] {{
        background-color: #ffffff !important;
        border-right: 1px solid rgba(0, 0, 0, 0.08);
    }}
    
    [data-testid="stSidebarNav"] {{display: none;}}

    /* Memaksa SEMUA jenis kotak input (Selectbox, Number Input, Text Input) menjadi terang */
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div,
    div[data-testid="stNumberInput"] div[data-baseweb="input"] > div,
    div[data-testid="stTextInput"] div[data-baseweb="input"] > div {{
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
        color: #0f172a !important;
    }}
    
    /* Memaksa teks di dalam kotak input menjadi gelap (terbaca) */
    div[data-testid="stSelectbox"] *,
    div[data-testid="stNumberInput"] input,
    div[data-testid="stTextInput"] input {{
        color: #0f172a !important;
    }}
    
    /* Memaksa popup daftar dropdown menjadi terang */
    div[role="listbox"] {{
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
    }}
    div[role="listbox"] li {{
        color: #0f172a !important;
    }}

    /* Memaksa Tombol Hitung (Primary Button) agar tidak menghitam */
    button[kind="primary"] {{
        background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }}
    button[kind="primary"]:hover {{
        opacity: 0.9 !important;
    }}

    /* Tipografi Halaman Depan */
    .hero-title {{
        font-size: 4rem;
        font-weight: 800;
        color: #0f172a;
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
        color: #334155;
        font-weight: 500;
        max-width: 650px;
        line-height: 1.6;
        margin-bottom: 3.5rem;
    }}

    /* Kartu Fitur Beranda */
    .card {{
        background: rgba(255, 255, 255, 0.85);
        border: 1px solid rgba(0, 0, 0, 0.08);
        border-radius: 16px;
        padding: 2rem;
        height: 100%;
        backdrop-filter: blur(10px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    }}
    .card:hover {{
        border-color: rgba(14, 165, 233, 0.4);
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 0 15px rgba(14, 165, 233, 0.15);
    }}
    .card-title {{
        font-size: 1.25rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.75rem;
        border-bottom: 1px solid rgba(0, 0, 0, 0.08);
        padding-bottom: 0.75rem;
    }}
    .card-text {{
        font-size: 0.95rem;
        color: #334155;
        line-height: 1.6;
        font-weight: 500;
    }}

    h1, h2, h3, p, label {{
        color: #0f172a !important;
    }}

    #MainMenu, header, footer {{visibility: hidden;}}
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.markdown('<div style="font-size: 0.85rem; font-weight: 700; color: #475569; letter-spacing: 0.15em; margin-bottom: 15px; margin-left: 10px;">NAVIGASI SISTEM</div>', unsafe_allow_html=True)
    
    menu = option_menu(
        menu_title=None,
        options=["Beranda", "Struktur", "Material", "Hidrologi", "Geoteknik"],
        icons=["house", "calculator", "box", "droplet", "globe"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#64748b", "font-size": "1.1rem"}, 
            "nav-link": {
                "font-size": "0.95rem", 
                "font-weight": "600",
                "color": "#334155",
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