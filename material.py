import streamlit as st
import math

def tampilkan():
    st.markdown("<h2>Perhitungan Material & Bahan</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #475569; font-weight: 500; margin-bottom: 2rem;'>Evaluasi mutu material struktur Beton, Baja, dan Kayu berdasarkan Standarisasi SNI terbaru.</p>", unsafe_allow_html=True)
    
    # Pilihan Kategori Material Menggunakan Radio Button
    kategori = st.radio("Pilih Jenis Material", ["Struktur Beton (SNI 2847)", "Struktur Baja (SNI 1729)", "Struktur Kayu (SNI 7973)"], horizontal=True)
    
    st.markdown("---")
    
    if kategori == "Struktur Beton (SNI 2847)":
        st.markdown("### Modulus Elastisitas Beton ($E_c$)")
        st.markdown("Menghitung nilai kekakuan elastis beton berdasarkan kuat tekan silinder ($f'_c$).")
        st.markdown("<p style='font-weight: 600; color: #0284c7;'>Rumus: $E_c = 4700 \times \sqrt{f'_c}$</p>", unsafe_allow_html=True)
        
        f_c = st.number_input("Kuat Tekan Beton - f'c (MPa)", min_value=1.0, value=25.0, step=0.5)
        
        if st.button("Hitung Modulus Elastisitas", type="primary"):
            ec = 4700 * math.sqrt(f_c)
            st.markdown(f"""
                <div class="result-box">
                    <div style="font-size: 0.9rem; color: #64748b; font-weight: 600; margin-bottom: 4px;">Modulus Elastisitas (Ec)</div>
                    <div style="font-size: 2rem; font-weight: 800; color: #0284c7;">{ec:,.2f} MPa</div>
                    <div style="font-size: 0.85rem; color: #334155; margin-top: 8px;">Berdasarkan formula SNI: 4700 × √({f_c})</div>
                </div>
            """, unsafe_allow_html=True)

    elif kategori == "Struktur Baja (SNI 1729)":
        st.markdown("### Kuat Tarik Nominal Penampang Baja ($Pn$)")
        st.markdown("Evaluasi kekuatan tarik nominal berdasarkan luas penampang efektif dan tegangan leleh.")
        st.markdown("<p style='font-weight: 600; color: #0284c7;'>Rumus: $P_n = A_g \times F_y$</p>", unsafe_allow_html=True)
        
        ag = st.number_input("Luas Penampang Bruto - Ag (mm²)", min_value=10.0, value=1200.0, step=50.0)
        fy = st.number_input("Tegangan Leleh - Fy (MPa)", min_value=100.0, value=250.0, step=10.0)
        
        if st.button("Hitung Kuat Tarik", type="primary"):
            pn = (ag * fy) / 1000.0
            st.markdown(f"""
                <div class="result-box">
                    <div style="font-size: 0.9rem; color: #64748b; font-weight: 600; margin-bottom: 4px;">Kuat Tarik Nominal (Pn)</div>
                    <div style="font-size: 2rem; font-weight: 800; color: #0284c7;">{pn:,.2f} kN</div>
                    <div style="font-size: 0.85rem; color: #334155; margin-top: 8px;">Formula: Pn = Ag × Fy / 1000</div>
                </div>
            """, unsafe_allow_html=True)

    elif kategori == "Struktur Kayu (SNI 7973)":
        st.markdown("### Tegangan Lentur Ijin Kayu ($\sigma_{m}$)")
        st.markdown("Evaluasi kapasitas tegangan lentur balok kayu struktural berdasarkan SNI 7973.")
        st.markdown("<p style='font-weight: 600; color: #0284c7;'>Rumus: $\sigma_{m} = \frac{M}{S}$</p>", unsafe_allow_html=True)
        
        m_omen = st.number_input("Momen Lentur - M (N·mm)", min_value=100.0, value=1500000.0, step=10000.0)
        s_section = st.number_input("Modulus Penampang - S (mm³)", min_value=10.0, value=1500.0, step=50.0)
        
        if st.button("Hitung Tegangan Lentur", type="primary"):
            sigma_m = m_omen / s_section
            st.markdown(f"""
                <div class="result-box">
                    <div style="font-size: 0.9rem; color: #64748b; font-weight: 600; margin-bottom: 4px;">Tegangan Lentur (σm)</div>
                    <div style="font-size: 2rem; font-weight: 800; color: #0284c7;">{sigma_m:,.2f} MPa</div>
                    <div style="font-size: 0.85rem; color: #334155; margin-top: 8px;">Formula: σm = M / S</div>
                </div>
            """, unsafe_allow_html=True)