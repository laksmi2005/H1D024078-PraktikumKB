import tkinter as tk
from tkinter import messagebox

database_tht = {
    "Tonsilitis": {"gejala": ["G37", "G12", "G5", "G27", "G6", "G21"], "solusi": "Istirahat cukup, kumur air garam, dan minum cairan hangat."},
    "Sinusitis Maksilaris": {"gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"], "solusi": "Irigasi hidung dengan larutan saline dan gunakan dekongestan."},
    "Sinusitis Frontalis": {"gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"], "solusi": "Kompres hangat pada area dahi dan istirahat di ruang lembap."},
    "Sinusitis Edmoidalis": {"gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"], "solusi": "Konsultasi spesialis THT untuk pembersihan saluran ethmoid."},
    "Sinusitis Sfenoidalis": {"gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"], "solusi": "Pemberian antibiotik dan pereda nyeri sesuai resep dokter."},
    "Abses Peritonsiler": {"gejala": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"], "solusi": "Tindakan medis segera untuk pengosongan nanah (drainase)."},
    "Faringitis": {"gejala": ["G37", "G5", "G6", "G7", "G15"], "solusi": "Hindari rokok/iritan dan konsumsi permen pelega tenggorokan."},
    "Kanker Laring": {"gejala": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"], "solusi": "Pemeriksaan biopsi dan konsultasi onkologi segera."},
    "Deviasi Septum": {"gejala": ["G37", "G17", "G20", "G8", "G18", "G25"], "solusi": "Konsultasi bedah septoplasti jika pernapasan terganggu parah."},
    "Laringitis": {"gejala": ["G37", "G5", "G15", "G16", "G32"], "solusi": "Istirahatkan suara (jangan bicara) dan minum banyak air putih."},
    "Kanker Leher & Kepala": {"gejala": ["G5", "G22", "G8", "G28", "G3", "G11"], "solusi": "Pemeriksaan radiologi dan konsultasi spesialis bedah onkologi."},
    "Otitis Media Akut": {"gejala": ["G37", "G20", "G35", "G31"], "solusi": "Pemberian tetes telinga dan pereda demam."},
    "Contact Ulcers": {"gejala": ["G5", "G2"], "solusi": "Terapi suara dan hindari penggunaan suara secara berlebihan."},
    "Abses Parafaringeal": {"gejala": ["G5", "G16"], "solusi": "Perawatan intensif di rumah sakit dan pemberian antibiotik IV."},
    "Barotitis Media": {"gejala": ["G12", "G20"], "solusi": "Melakukan manuver valsava dan menghindari perubahan tekanan udara."},
    "Kanker Nafasoring": {"gejala": ["G17", "G8"], "solusi": "Pemeriksaan endoskopi hidung dan biopsi jaringan."},
    "Kanker Tonsil": {"gejala": ["G6", "G29"], "solusi": "Evaluasi bedah dan terapi radiasi sesuai stadium."},
    "Neuronitis Vestibularis": {"gejala": ["G35", "G24"], "solusi": "Latihan rehabilitasi vestibular dan obat anti-mual."},
    "Meniere": {"gejala": ["G20", "G35", "G14", "G4"], "solusi": "Diet rendah garam dan hindari pemicu vertigo."},
    "Tumor Syaraf Pendengaran": {"gejala": ["G12", "G34", "G23"], "solusi": "Pemeriksaan MRI dan observasi oleh dokter spesialis bedah saraf."},
    "Kanker Leher Metastatik": {"gejala": ["G29"], "solusi": "Pencarian sumber kanker primer dan terapi sistemik."},
    "Osteosklerosis": {"gejala": ["G34", "G9"], "solusi": "Penggunaan alat bantu dengar atau tindakan operasi stapedektomi."},
    "Vertigo Postular": {"gejala": ["G24"], "solusi": "Melakukan manuver Epley untuk reposisi kristal telinga dalam."}
}

daftar_gejala = [
    ("G1", "nafas abnormal"), ("G2", "suara serak"), ("G3", "perubahan kulit"),
    ("G4", "telinga penuh"), ("G5", "nyeri bicara menelan"), ("G6", "nyeri tenggorokan"),
    ("G7", "nyeri leher"), ("G8", "pendarahan hidung"), ("G9", "telinga berdenging"),
    ("G10", "air liur menetes"), ("G11", "perubahan suara"), ("G12", "sakit kepala"),
    ("G13", "nyeri pinggir hidung"), ("G14", "serangan vertigo"), ("G15", "getah bening"),
    ("G16", "leher bengkak"), ("G17", "hidung tersumbat"), ("G18", "infeksi sinus"),
    ("G19", "berat badan turun"), ("G20", "nyeri telinga"), ("G21", "selaput lendir merah"),
    ("G22", "benjolan leher"), ("G23", "tubuh tak seimbang"), ("G24", "bola mata bergerak"),
    ("G25", "nyeri wajah"), ("G26", "dahi sakit"), ("G27", "batuk"),
    ("G28", "tumbuh dimulut"), ("G29", "benjolan dileher"), ("G30", "nyeri antara mata"),
    ("G31", "radang gendang telinga"), ("G32", "tenggorokan gatal"), ("G33", "hidung meler"),
    ("G34", "tuli"), ("G35", "mual muntah"), ("G36", "letih lesu"), ("G37", "demam")
]

class THTExpert:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa THT - NIM H1H024035")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f8ff")
        
        self.gejala_terpilih = []
        self.index = 0

        self.lbl_judul = tk.Label(root, text="Aplikasi Pakar Diagnosa THT", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#2c3e50")
        self.lbl_judul.pack(pady=20)

        self.lbl_tanya = tk.Label(root, text="Klik tombol 'Mulai' untuk melakukan diagnosa.", wraplength=500, font=("Arial", 12), bg="#f0f8ff")
        self.lbl_tanya.pack(pady=30)

        self.btn_start = tk.Button(root, text="Mulai Diagnosa", command=self.mulai, bg="#3498db", fg="white", font=("Arial", 10, "bold"), width=20)
        self.btn_start.pack()

        self.frame_aksi = tk.Frame(root, bg="#f0f8ff")
        self.btn_ya = tk.Button(self.frame_aksi, text="YA", width=12, bg="#2ecc71", fg="white", font=("Arial", 10, "bold"), command=lambda: self.jawab('y'))
        self.btn_tidak = tk.Button(self.frame_aksi, text="TIDAK", width=12, bg="#e74c3c", fg="white", font=("Arial", 10, "bold"), command=lambda: self.jawab('t'))

    def mulai(self):
        self.gejala_terpilih = []
        self.index = 0
        self.btn_start.pack_forget()
        self.frame_aksi.pack(pady=20)
        self.btn_ya.pack(side=tk.LEFT, padx=15)
        self.btn_tidak.pack(side=tk.LEFT, padx=15)
        self.update_pertanyaan()

    def update_pertanyaan(self):
        if self.index < len(daftar_gejala):
            kode, teks = daftar_gejala[self.index]
            self.lbl_tanya.config(text=f"[{kode}] Apakah Anda mengalami {teks}?")
        else:
            self.tampilkan_hasil()

    def jawab(self, pilihan):
        if pilihan == 'y':
            self.gejala_terpilih.append(daftar_gejala[self.index][0])
        self.index += 1
        self.update_pertanyaan()

    def tampilkan_hasil(self):
        hasil_list = []
        for nama, data in database_tht.items():
            if all(g in self.gejala_terpilih for g in data["gejala"]):
                hasil_list.append(f"✅ {nama}\nSolusi: {data['solusi']}")

        self.frame_aksi.pack_forget()
        self.btn_start.pack(pady=20)
        self.btn_start.config(text="Diagnosa Ulang")

        if not hasil_list:
            messagebox.showinfo("Hasil Diagnosa", "Tidak ada penyakit THT yang cocok dengan gejala tersebut.")
        else:
            hasil_akhir = "\n\n".join(hasil_list)
            messagebox.showwarning("Hasil Diagnosa", f"Berdasarkan analisis, Anda terdeteksi:\n\n{hasil_akhir}")
        
        self.lbl_tanya.config(text="Diagnosa selesai. Hasil telah ditampilkan.")

if __name__ == "__main__":
    root = tk.Tk()
    app = THTExpert(root)
    root.mainloop()