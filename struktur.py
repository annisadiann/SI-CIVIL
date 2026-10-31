import streamlit as st
import math

def tampilkan():
    st.markdown('<div class="hero-title" style="font-size: 2.5rem; margin-bottom: 1rem;">Perhitungan <span>Struktur</span></div>', unsafe_allow_html=True)
    
    topik = st.selectbox("Pilih Modul Materi", [
        "Keseimbangan Statika (Reaksi Tumpuan)",
        "Momen Inersia Penampang",
        "Tegangan Normal", 
        "Regangan (Strain) & Hukum Hooke", 
        "Tegangan Lentur (Bending Stress)", 
        "Tegangan Geser (Shear Stress)"
    ])
    
    st.markdown("---")
    
    if topik == "Keseimbangan Statika (Reaksi Tumpuan)":
        st.markdown('### Reaksi Tumpuan Balok Sederhana')
        st.write("Menghitung reaksi tumpuan Sendi-Rol dengan satu beban terpusat (Point Load).")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            p = st.number_input("Beban Terpusat - P (kN)", value=0.0)
        with col2:
            l = st.number_input("Panjang Bentang Total - L (m)", min_value=0.1, value=10.0)
        with col3:
            a = st.number_input("Jarak Beban dari Tumpuan A (m)", min_value=0.0, max_value=float(l), value=5.0)
            
        if st.button("Hitung Reaksi Tumpuan", use_container_width=True, type="primary"):
            b = l - a
            ra = (p * b) / l
            rb = (p * a) / l
            
            c1, c2 = st.columns(2)
            c1.metric(label="Reaksi Tumpuan A (Ra)", value=f"{ra:.2f} kN")
            c2.metric(label="Reaksi Tumpuan B (Rb)", value=f"{rb:.2f} kN")

    elif topik == "Momen Inersia Penampang":
        st.markdown('### Momen Inersia (I)')
        bentuk = st.radio("Pilih Bentuk Penampang", ["Persegi Panjang", "Lingkaran"])
        
        if bentuk == "Persegi Panjang":
            col1, col2 = st.columns(2)
            with col1:
                b = st.number_input("Lebar Alas - b (mm)", min_value=0.1, value=100.0)
            with col2:
                h = st.number_input("Tinggi - h (mm)", min_value=0.1, value=200.0)
            
            if st.button("Hitung Inersia Persegi", use_container_width=True, type="primary"):
                ix = (b * (h**3)) / 12
                iy = (h * (b**3)) / 12
                c1, c2 = st.columns(2)
                c1.metric(label="Inersia Sumbu X (Ix)", value=f"{ix:,.2f} mm⁴")
                c2.metric(label="Inersia Sumbu Y (Iy)", value=f"{iy:,.2f} mm⁴")
                
        elif bentuk == "Lingkaran":
            d = st.number_input("Diameter - d (mm)", min_value=0.1, value=100.0)
            
            if st.button("Hitung Inersia Lingkaran", use_container_width=True, type="primary"):
                i = (math.pi * (d**4)) / 64
                st.metric(label="Momen Inersia (I)", value=f"{i:,.2f} mm⁴")

    elif topik == "Tegangan Normal":
        st.markdown('### Kalkulator Tegangan Normal')
        col1, col2 = st.columns(2)
        
        with col1:
            gaya = st.number_input("Gaya Aksial (N)", value=0.0)
        with col2:
            luas = st.number_input("Luas Penampang (mm²)", min_value=0.1, value=1.0)
            
        if st.button("Hitung Tegangan Normal", use_container_width=True, type="primary"):
            hasil = gaya / luas
            st.metric(label="Hasil Tegangan Normal (σ)", value=f"{hasil:.2f} MPa")
            
    elif topik == "Regangan (Strain) & Hukum Hooke":
        st.markdown('### Kalkulator Regangan')
        col1, col2 = st.columns(2)
        
        with col1:
            delta_l = st.number_input("Perubahan Panjang - ΔL (mm)", value=0.0)
        with col2:
            l_awal = st.number_input("Panjang Awal - L (mm)", min_value=0.1, value=1000.0)
            
        if st.button("Hitung Regangan", use_container_width=True, type="primary"):
            regangan = delta_l / l_awal
            st.metric(label="Hasil Regangan (ε)", value=f"{regangan:.5f}")
            
    elif topik == "Tegangan Lentur (Bending Stress)":
        st.markdown('### Kalkulator Tegangan Lentur')
        col1, col2, col3 = st.columns(3)
        
        with col1:
            momen = st.number_input("Momen Lentur - M (N.mm)", value=0.0)
        with col2:
            jarak_y = st.number_input("Jarak Garis Netral - y (mm)", value=0.0)
        with col3:
            inersia = st.number_input("Momen Inersia - I (mm⁴)", min_value=0.1, value=1.0)
            
        if st.button("Hitung Tegangan Lentur", use_container_width=True, type="primary"):
            teg_lentur = (momen * jarak_y) / inersia
            st.metric(label="Tegangan Lentur (σb)", value=f"{teg_lentur:.2f} MPa")
            
    elif topik == "Tegangan Geser (Shear Stress)":
        st.markdown('### Kalkulator Tegangan Geser')
        col1, col2 = st.columns(2)
        
        with col1:
            gaya_geser = st.number_input("Gaya Geser - V (N)", value=0.0)
        with col2:
            luas_geser = st.number_input("Luas Penampang Geser - A (mm²)", min_value=0.1, value=1.0)
            
        if st.button("Hitung Tegangan Geser", use_container_width=True, type="primary"):
            teg_geser = gaya_geser / luas_geser
            st.metric(label="Tegangan Geser (τ)", value=f"{teg_geser:.2f} MPa")