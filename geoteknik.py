import streamlit as st
import math

def tampilkan():
    st.title("Perhitungan Geoteknik")
    
    topik = st.selectbox("Pilih Materi Geoteknik", [
        "Fase Tanah (Angka Pori, Porositas, Kadar Air)",
        "Tegangan Efektif (Terzaghi)",
        "Kuat Geser Tanah (Mohr-Coulomb)",
        "Daya Dukung Tanah (Terzaghi)",
        "Penurunan Konsolidasi"
    ])
    st.divider()

    if topik == "Fase Tanah (Angka Pori, Porositas, Kadar Air)":
        st.subheader("Hubungan Berat & Volume (Fase Tanah)")
        pilihan = st.radio("Hitung Parameter:", ["Angka Pori (e)", "Porositas (n)", "Kadar Air (w)"])
        
        if pilihan == "Angka Pori (e)":
            vv = st.number_input("Volume Rongga Pori - Vv", value=0.0)
            vs = st.number_input("Volume Butiran Padat - Vs", min_value=0.001, value=1.0)
            if st.button("Hitung Angka Pori"):
                st.success(f"Angka Pori (e) = {vv/vs:.4f}")
                
        elif pilihan == "Porositas (n)":
            vv = st.number_input("Volume Rongga Pori - Vv", value=0.0)
            v_total = st.number_input("Volume Total - V", min_value=0.001, value=1.0)
            if st.button("Hitung Porositas"):
                st.success(f"Porositas (n) = {(vv/v_total)*100:.2f} %")
                
        elif pilihan == "Kadar Air (w)":
            ww = st.number_input("Berat Air - Ww", value=0.0)
            ws = st.number_input("Berat Butiran Padat - Ws", min_value=0.001, value=1.0)
            if st.button("Hitung Kadar Air"):
                st.success(f"Kadar Air (w) = {(ww/ws)*100:.2f} %")

    elif topik == "Tegangan Efektif (Terzaghi)":
        st.subheader("Prinsip Tegangan Efektif Terzaghi")
        tegangan_total = st.number_input("Tegangan Total - σ (kPa)", value=0.0)
        tekanan_pori = st.number_input("Tekanan Air Pori - u (kPa)", value=0.0)
        if st.button("Hitung Tegangan Efektif"):
            tegangan_efektif = tegangan_total - tekanan_pori
            st.success(f"Tegangan Efektif (σ') = {tegangan_efektif:.2f} kPa")

    elif topik == "Kuat Geser Tanah (Mohr-Coulomb)":
        st.subheader("Kriteria Keruntuhan Mohr-Coulomb")
        c = st.number_input("Kohesi Tanah - c (kPa)", value=0.0)
        tegangan_efektif = st.number_input("Tegangan Normal Efektif - σ' (kPa)", value=0.0)
        sudut_geser = st.number_input("Sudut Geser Dalam - φ (derajat)", value=0.0)
        if st.button("Hitung Kuat Geser"):
            rad = math.radians(sudut_geser)
            tau = c + (tegangan_efektif * math.tan(rad))
            st.success(f"Kuat Geser Tanah (τ) = {tau:.2f} kPa")

    elif topik == "Daya Dukung Tanah (Terzaghi)":
        st.subheader("Persamaan Daya Dukung Terzaghi (Pondasi Menerus)")
        c = st.number_input("Kohesi - c (kPa)", value=0.0)
        nc = st.number_input("Faktor Kapasitas Dukung - Nc", value=0.0)
        q = st.number_input("Tekanan Overburden - q (kPa)", value=0.0)
        nq = st.number_input("Faktor Kapasitas Dukung - Nq", value=0.0)
        gamma = st.number_input("Berat Volume Tanah - γ (kN/m³)", value=0.0)
        b = st.number_input("Lebar Pondasi - B (m)", value=0.0)
        ngamma = st.number_input("Faktor Kapasitas Dukung - Nγ", value=0.0)
        
        if st.button("Hitung Kapasitas Dukung Ultimit"):
            qu = (c * nc) + (q * nq) + (0.5 * gamma * b * ngamma)
            st.success(f"Kapasitas Dukung Ultimit (qu) = {qu:.2f} kPa")

    elif topik == "Penurunan Konsolidasi":
        st.subheader("Consolidation Settlement")
        cc = st.number_input("Indeks Kompresi - Cc", value=0.0)
        h = st.number_input("Tebal Lapisan Lempung - H (m)", value=0.0)
        e0 = st.number_input("Angka Pori Awal - e0", value=0.0)
        sigma_0 = st.number_input("Tegangan Efektif Awal - σ0' (kPa)", min_value=0.001, value=1.0)
        delta_sigma = st.number_input("Tambahan Tegangan - Δσ (kPa)", value=0.0)
        
        if st.button("Hitung Penurunan Konsolidasi"):
            sc = (cc * h / (1 + e0)) * math.log10((sigma_0 + delta_sigma) / sigma_0)
            st.success(f"Penurunan Konsolidasi (Sc) = {sc:.4f} m")