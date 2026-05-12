# Pertemuan 6  - Jaringan Syaraf Tiruan (JST)

## Deskripsi
Repositori ini berisi hasil pengerjaan modul Praktikum Kecerdasan Buatan (KB) Pertemuan 6 yang berfokus pada implementasi **Jaringan Syaraf Tiruan (JST)**. Praktikum ini mencakup dua metode pembelajaran utama, yaitu **Perceptron** untuk masalah yang dapat dipisahkan secara linier dan **Backpropagation** untuk masalah non-linier seperti XOR.

## Isi Repositori
Folder `Pertemuan6` berisi beberapa file penting sebagai berikut:
* `perceptron.py`: Source code class Perceptron dan fungsi aktivasi.
* `perceptron_or.py`: Implementasi Perceptron untuk menyelesaikan masalah logika OR.
* `Backpropagation.py`: Source code class Backpropagation (termasuk hidden layer dan fungsi aktivasi sigmoid).
* `Backpropagation_xor.py`: Implementasi Backpropagation untuk menyelesaikan masalah logika XOR.
* `Hasil Perceptron.txt`: Log hasil iterasi, pembaruan bobot, dan bias pada algoritma Perceptron.
* `hasilBackpropagation.txt`: Log hasil iterasi dan penurunan Sum Square Error (SSE) pada algoritma Backpropagation.

## Hasil Praktikum
1. **Perceptron (OR Gate)**: 
   Model berhasil melakukan klasifikasi dengan benar. Garis pemisah (*decision boundary*) terbentuk untuk memisahkan data input sesuai dengan target yang ditentukan.
   
2. **Backpropagation (XOR Gate)**: 
   Model berhasil mencapai target error yang ditentukan (0.001). Grafik menunjukkan penurunan SSE yang signifikan seiring bertambahnya epoch, menandakan proses pembelajaran pada hidden layer berjalan dengan baik.

## Cara Menjalankan
1. Clone repositori ini.
2. Pastikan telah menginstal `numpy` dan `matplotlib`.
3. Jalankan file utama dengan perintah:
   ```bash
   python Pertemuan6/perceptron_or.py
   python Pertemuan6/Backpropagation_xor.py