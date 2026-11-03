# 🏗️ SI-CIVIL: Sistem Kalkulasi Teknik Sipil Berbasis Web

[![Python Version](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-red.svg)](https://streamlit.io/)
[![Standard](https://img.shields.io/badge/Standard-SNI%202847%20%7C%201729%20%7C%207973-green.svg)](https://bsn.go.id/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**SI-CIVIL** adalah platform komputasi rekayasa teknik sipil terintegrasi berbasis web yang dirancang untuk mendukung akurasi, kecepatan, dan kepraktisan perhitungan teknis sesuai standar baku Standar Nasional Indonesia (SNI) serta prinsip dasar mekanika rekayasa.

---

## 📑 Daftar Isi
- [Fitur Utama](#-fitur-utama)
- [Struktur Modul Komputasi](#-struktur-modul-komputasi)
- [Teknologi yang Digunakan](#-teknologi-yang-digunakan)
- [Cara Instalasi & Menjalankan](#-cara-instalasi--menjalankan)
- [Struktur Direktori Repositori](#-struktur-direktori-repositori)
- [Dokumentasi Lengkap](#-dokumentasi-lengkap)
- [Standar Acuan Teknis](#-standar-acuan-teknis)

---

## ✨ Fitur Utama
1. **Navigasi Cepat & Responsif**: Antarmuka berbasis Streamlit dengan komponen navigasi sidebar modern (*Streamlit Option Menu*).
2. **Kalkulasi Multidisiplin**: Mengintegrasikan 4 bidang utama teknik sipil dalam satu dashboard.
3. **Standarisasi SNI**: Dilengkapi perhitungan modulus beton, kuat tarik leleh baja, dan reduksi tegangan kayu sesuai standar SNI terbaru.
4. **Validasi Numerik Instan**: Menampilkan hasil secara real-time dengan metrik dan format satuan teknis yang jelas.

---

## 📐 Struktur Modul Komputasi

### 1. 🧮 Analisis Struktur (`struktur.py`)
- Reaksi tumpuan sendi-rol balok sederhana dengan beban titik terpusat.
- Momen inersia penampang persegi panjang ($I_x, I_y$) dan penampang lingkaran ($I$).
- Tegangan normal aksial ($\sigma = P/A$).
- Regangan aksial batang ($\varepsilon = \Delta L/L$).
- Tegangan lentur balok ($\sigma_b = M \cdot y / I$).
- Tegangan geser penampang ($\tau = V/A$).

### 2. 📦 Karakterisasi Material (`material.py`)
- **Struktur Beton (SNI 2847)**: Modulus elastisitas beton normal ($E_c = 4700\sqrt{f'_c}$).
- **Struktur Baja (SNI 1729)**: Kuat tarik rencana leleh penampang utuh ($\phi P_n = 0.90 \cdot f_y \cdot A_g$).
- **Struktur Kayu (SNI 7973)**: Kadar air kayu uji oven (*Moisture Content*) dan tegangan lentur desain terkoreksi ($F' = F_b \times C_m \times C_t \times C_f$).

### 3. 💧 Hidrologi Terapan (`hidrologi.py`)
- Persamaan neraca kesetimbangan air (*Water Balance Equation*: $\Delta S = P - Q - E$).
- Intensitas curah hujan metode Mononobe ($I = \frac{R_{24}}{24}(\frac{24}{t})^{2/3}$).
- Debit banjir puncak saluran metode Rasional ($Q = 0.278 \cdot C \cdot I \cdot A$).
- Kurva laju infiltrasi tanah metode Horton ($f_t = f_c + (f_0 - f_c)e^{-kt}$).

### 4. 🌐 Geoteknik & Mekanika Tanah (`geoteknik.py`)
- Hubungan fase tanah: Angka Pori ($e$), Porositas ($n$), dan Kadar Air ($w$).
- Prinsip tegangan efektif Terzaghi ($\sigma' = \sigma - u$).
- Kuat geser tanah kriteria keruntuhan Mohr-Coulomb ($\tau = c + \sigma'\tan\phi$).
- Kapasitas daya dukung ultimit pondasi dangkal menerus Terzaghi ($q_u$).
- Penurunan konsolidasi primer tanah lempung satu dimensi ($S_c$).

---

## 🛠️ Teknologi yang Digunakan
- **Bahasa**: Python 3.9+
- **Framework Web**: Streamlit
- **Komponen Menu**: `streamlit-option-menu`
- **Desain & Tipografi**: HTML5 / CSS3 (Inter Google Fonts & Modern Gradient Cards)

---

## 🚀 Cara Instalasi & Menjalankan

### 1. Clone Repository
```bash
git clone https://github.com/username/SI-CIVIL.git
cd SI-CIVIL
```

### 2. Pasang Dependensi
Pastikan Python sudah terpasang di komputer Anda, lalu jalankan:
```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi
```bash
streamlit run main.py
```
Aplikasi akan otomatis terbuka pada peramban web di alamat: `http://localhost:8501`.

---

## 📂 Struktur Direktori Repositori
```text
SI-CIVIL/
│
├── main.py                          # File utama routing & dashboard beranda
├── struktur.py                      # Modul komputasi analisis struktur
├── material.py                      # Modul evaluasi material berbasis SNI
├── hidrologi.py                     # Modul perhitungan hidrologi & drainase
├── geoteknik.py                     # Modul mekanika tanah & pondasi
├── requirements.txt                 # Daftar pustaka paket Python
├── README.md                        # Ringkasan dokumentasi repositori
├── sivil.jpg                        # Latar belakang grafis aplikasi
├── LAPORAN_PENGEMBANGAN_SOFTWARE.md # Laporan komprehensif pengembangan software
└── BUKU_PANDUAN_USER_MANUAL.md      # Buku manual panduan lengkap pengguna
```

---

## 📖 Dokumentasi Lengkap
Untuk membaca dokumentasi teknis dan pengoperasian secara mendalam, silakan merujuk pada:
1. 📄 **[Laporan Pengembangan Software](LAPORAN_PENGEMBANGAN_SOFTWARE.md)**: Memuat latar belakang, perancangan arsitektur, diagram alir (flowchart), pengujian validasi 20 skenario uji (test matrix), dan pembahasan.
2. 📘 **[Buku Panduan Pengguna (User Manual)](BUKU_PANDUAN_USER_MANUAL.md)**: Panduan langkah demi langkah cara memasang, menggunakan setiap fitur modul, serta troubleshooting masalah umum.

---

## 📚 Standar Acuan Teknis
- **SNI 2847:2019**: Persyaratan Beton Struktural untuk Bangunan Gedung.
- **SNI 1729:2020**: Spesifikasi untuk Bangunan Gedung Baja Struktural.
- **SNI 7973:2013**: Spesifikasi Desain untuk Konstruksi Kayu.
- **Karl Terzaghi (1943)**: *Theoretical Soil Mechanics*.
- **Ven Te Chow (1988)**: *Applied Hydrology*.
