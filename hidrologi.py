import streamlit as st
import math

def tampilkan():
    st.title("Perhitungan Hidrologi")
    
    topik = st.selectbox("Pilih Materi Hidrologi", [
        "Persamaan Keseimbangan Air",
        "Intensitas Hujan (Mononobe)",
        "Debit Limpasan (Rasional)",
        "Laju Infiltrasi (Horton)"
    ])
    st.divider()

    if topik == "Persamaan Keseimbangan Air":
        st.subheader("Keseimbangan Air (Water Balance)")
        st.latex(r"P = Q + E + \Delta S")
        p = st.number_input("Curah Hujan - P (mm)", value=0.0)
        q = st.number_input("Aliran Permukaan - Q (mm)", value=0.0)
        e = st.number_input("Evapotranspirasi - E (mm)", value=0.0)
        
        if st.button("Hitung Perubahan Cadangan Air (ΔS)"):
            delta_s = p - q - e
            st.success(f"Perubahan Cadangan Air (ΔS) = {delta_s:.2f} mm")

    elif topik == "Intensitas Hujan (Mononobe)":
        st.subheader("Rumus Mononobe")
        r24 = st.number_input("Curah Hujan Maks 24 Jam - R24 (mm)", value=0.0)
        t = st.number_input("Waktu Konsentrasi - t (jam)", min_value=0.1, value=1.0)
        
        if st.button("Hitung Intensitas Hujan (I)"):
            intensitas = (r24 / 24) * math.pow((24 / t), (2/3))
            st.success(f"Intensitas Curah Hujan (I) = {intensitas:.2f} mm/jam")

    elif topik == "Debit Limpasan (Rasional)":
        st.subheader("Metode Rasional")
        st.info("Menggunakan rumus metrik: Q = 0.278 × C × I × A")
        c = st.number_input("Koefisien Pengaliran (C)", min_value=0.0, max_value=1.0, value=0.5)
        i = st.number_input("Intensitas Hujan - I (mm/jam)", value=0.0)
        a = st.number_input("Luas Daerah Aliran - A (km²)", value=0.0)
        
        if st.button("Hitung Debit Puncak (Q)"):
            q_puncak = 0.278 * c * i * a
            st.success(f"Debit Limpasan Puncak (Q) = {q_puncak:.4f} m³/s")

    elif topik == "Laju Infiltrasi (Horton)":
        st.subheader("Persamaan Horton")
        fo = st.number_input("Laju Infiltrasi Awal - fo (mm/jam)", value=0.0)
        fc = st.number_input("Laju Infiltrasi Konstan - fc (mm/jam)", value=0.0)
        k = st.number_input("Konstanta Penurunan - k", value=0.0)
        t = st.number_input("Waktu - t (jam)", value=0.0)
        
        if st.button("Hitung Laju Infiltrasi (ft)"):
            ft = fc + (fo - fc) * math.exp(-k * t)
            st.success(f"Laju Infiltrasi pada waktu {t} jam (ft) = {ft:.4f} mm/jam")