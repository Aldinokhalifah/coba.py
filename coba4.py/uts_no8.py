import matplotlib.pyplot as plt
import numpy as np

# Data diri
nama = "Claude Anthropic"
nim = "12345678"
prodi = "Teknik Informatika"
peminatan = "Kecerdasan Buatan"

# Data mata kuliah dan nilai
mata_kuliah = ["Algoritma", "Basis Data", "Pemrograman Web", "Machine Learning", 
               "Computer Vision", "Natural Language Processing"]
nilai = [88, 92, 85, 95, 90, 94]

# Membuat figure dan axis
plt.figure(figsize=(10, 6))

# Membuat bar chart
bars = plt.bar(mata_kuliah, nilai, color='skyblue', edgecolor='navy')

# Menambahkan nilai di atas setiap bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1,
             f'{height}', ha='center', va='bottom')

# Menambahkan data diri di bagian atas visualisasi
plt.figtext(0.5, 0.95, f"Nama: {nama}\nNIM: {nim}\nProgram Studi: {prodi}\nPeminatan: {peminatan}",
            ha='center', va='top', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

# Menambahkan judul dan label
plt.title('Nilai Mata Kuliah', fontsize=14, pad=30)
plt.xlabel('Mata Kuliah')
plt.ylabel('Nilai')

# Mengatur batas sumbu y
plt.ylim(0, 100)

# Mengatur tampilan grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Rotasi label sumbu x
plt.xticks(rotation=30, ha='right')

# Mengatur layout agar tidak terpotong
plt.tight_layout()

# Menampilkan grafik
plt.show()