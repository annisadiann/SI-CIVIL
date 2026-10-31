import streamlit as st
import math

def tampilkan():
    st.title("Perhitungan Material & Bahan")
    
    kategori = st.radio("Pilih Jenis Material", ["Struktur Beton (SNI 2847)", "Struktur Baja (SNI 1729)", "Struktur Kayu (SNI 7973)"])
    st.divider()

    if kategori == "Struktur Beton (SNI 2847)":
        topik = st.selectbox("Pilih Perhitungan Beton", ["Modulus Elastisitas Beton", "Kuat Tekan Karakteristik"])
        
        if topik == "Modulus Elastisitas Beton":
            st.subheader("Modulus Elastisitas Beton (Ec)")
            fc = st.number_input("Kuat Tekan Beton - f'c (MPa)", min_value=0.0, value=25.0)
            
            if st.button("Hitung Modulus Elastisitas", type="primary", use_container_width=True):
                ec = 4700 * math.sqrt(fc)
                st.metric(label="Modulus Elastisitas Beton (Ec)", value=f"{ec:.2f} MPa")
                
        elif topik == "Kuat Tekan Karakteristik":
            st.info("Kalkulator Kuat Tekan Karakteristik dapat ditambahkan di sini.")

    elif kategori == "Struktur Baja (SNI 1729)":
        topik = st.selectbox("Pilih Perhitungan Baja", ["Kuat Tarik Rencana (Leleh)", "Kelangsingan Kolom"])
        
        if topik == "Kuat Tarik Rencana (Leleh)":
            st.subheader("🏗️ Kuat Tarik (Kondisi Leleh Penampang Utuh)")
            col1, col2 = st.columns(2)
            with col1:
                fy = st.number_input("Tegangan Leleh - fy (MPa)", min_value=0.0, value=240.0)
            with col2:
                ag = st.number_input("Luas Penampang Bruto - Ag (mm²)", min_value=0.1, value=1000.0)
            
            if st.button("Hitung Kuat Tarik", type="primary", use_container_width=True):
                kuat_tarik = 0.9 * fy * ag
                st.metric(label="Kuat Tarik Rencana (ϕPn)", value=f"{kuat_tarik:.2f} N")
                
        elif topik == "Kelangsingan Kolom":
            st.info("Kalkulator Kelangsingan Kolom dapat ditambahkan di sini.")

    elif kategori == "Struktur Kayu (SNI 7973)":
        topik = st.selectbox("Pilih Perhitungan Kayu", ["Kadar Air (Moisture Content)", "Tegangan Desain Terkoreksi"])
        
        if topik == "Kadar Air (Moisture Content)":
            st.subheader("💧 Kalkulator Kadar Air Kayu")
            col1, col2 = st.columns(2)
            with col1:
                berat_awal = st.number_input("Berat Awal Kayu (gram)", value=0.0)
            with col2:
                berat_kering = st.number_input("Berat Kering Oven (gram)", min_value=0.1, value=1.0)
                
            if st.button("Hitung Kadar Air", type="primary", use_container_width=True):
                kadar_air = ((berat_awal - berat_kering) / berat_kering) * 100
                st.metric(label="Kadar Air (MC)", value=f"{kadar_air:.2f} %")
                
        elif topik == "Tegangan Desain Terkoreksi":
            st.subheader("🪵 Kalkulator Tegangan Desain Terkoreksi")
            st.write("Gunakan faktor koreksi yang relevan sesuai kondisi (default: 1.0).")
            
            fb = st.number_input("Nilai Desain Acuan - misal: Kuat Lentur Fb (MPa)", value=0.0)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                cm = st.number_input("Faktor Layan Basah (Cm)", value=1.0)
            with col2:
                ct = st.number_input("Faktor Temperatur (Ct)", value=1.0)
            with col3:
                cf = st.number_input("Faktor Ukuran (Cf)", value=1.0)
                
            if st.button("Hitung Tegangan Terkoreksi", type="primary", use_container_width=True):
                fb_aksen = fb * cm * ct * cf
                st.metric(label="Tegangan Desain Terkoreksi (F')", value=f"{fb_aksen:.2f} MPa")