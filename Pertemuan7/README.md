# Praktikum 7 - Jaringan Syaraf Tiruan 2
## Klasifikasi Spesies Bunga Iris menggunakan TensorFlow & Keras

### Tujuan
- Menerapkan konsep JST dalam kode Python menggunakan TensorFlow dan Keras

### Dataset
Dataset **Iris** dari UCI Machine Learning Repository (file lokal `iris.data`)

### Struktur Folder
```
H1D024002_PraktikumKB_Pertemuan7/
├── main1.ipynb
├── iris.data
├── main.py
└── README.md
```

### Cara Menjalankan
1. Buka `main1.ipynb` menggunakan Jupyter Notebook / Google Colab / Kaggle Notebook
2. Pastikan file `iris.data` berada di folder yang sama dengan `main1.ipynb`
3. Jalankan semua cell secara berurutan

### Arsitektur Model Neural Network

| Layer | Tipe | Parameter |
|-------|------|-----------|
| Input | Input | shape=(4,) |
| 1 | Dense | 1000 units, aktivasi ReLU |
| 2 | Dense | 500 units, aktivasi ReLU |
| 3 | Dense | 300 units, aktivasi ReLU |
| Output | Dense | 3 units, aktivasi Softmax |

### Library yang Digunakan
- TensorFlow / Keras
- NumPy
- Pandas
- scikit-learn
- Matplotlib
- Seaborn
