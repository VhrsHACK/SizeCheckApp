# 🧥 SizeCheckApp - Sistem Rekomendasi Ukuran Pakaian

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Lisensi MIT](https://img.shields.io/badge/Lisensi-MIT-green.svg)](LICENSE)
[![Status Proyek](https://img.shields.io/badge/Status-Produksi%20Siap-brightgreen)]()

## ✨ Fitur Unggulan

- 🎯 Akurasi tinggi dengan algoritma Greedy
- 📈 Optimal untuk dataset besar (1000+ item)
- 🖥️ Antarmuka pengguna modern dan responsif
- 📱 Kompatibel dengan berbagai sistem operasi
- 🛠️ Validasi input cerdas dengan pesan error deskriptif

## 🚀 Instalasi Cepat

1. **Kloning repositori**
   ```bash
   git clone https://github.com/VhrsHACK/SizeCheckApp.git
   cd ukurlah
   ```

2. **Buat virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Penggunaan

1. Letakkan dataset di folder `dataset/ukuran_pakaian.csv`
2. Jalankan app:
   ```bash
   python -m app.main
   ```
3. Masukkan parameter tubuh dan lihat rekomendasi instan!

**Format Input:**
```
Lingkar Dada: 70-120 cm
Lebar Pundak: 30-50 cm
Lingkar Perut: 60-100 cm
Panjang Body: 60-80 cm
```

## 🏗️ Struktur Proyek

```plaintext
.
├── app/
│   ├── gui/       # Komponen UI dan styling
│   ├── mesin_rekomendasi.py  # Algoritma inti
│   └── pengolah_data.py      # Manajemen dataset
├── dataset/             # Penyimpanan data
├── uji_coba/           # Skrip testing
├── requirements.txt    # Dependensi
└── README.md           # Dokumentasi
```

## 🤝 Kontribusi

Kontribusi diterima dengan syarat:
1. Fork repositori
2. Buat branch fitur (`git checkout -b fitur/namafitur`)
3. Commit perubahan
4. Push ke branch
5. Buat Pull Request

**Panduan Coding:**
- Gunakan [Black](https://github.com/psf/black) untuk formatting
- Tulis test case untuk kode baru
- Dokumentasikan perubahan penting

## 📜 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE)

---

Dibangun dengan ❤️ oleh [VhrsHACK] menggunakan:
- [Pandas](https://pandas.pydata.org/) untuk analisis data
- [NumPy](https://numpy.org/) untuk komputasi numerik
- [Tkinter](https://docs.python.org/3/library/tkinter.html) untuk gui GUI

