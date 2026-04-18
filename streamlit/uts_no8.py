import matplotlib.pyplot as plt
import numpy as np

nama = "Aldino Khalifah"
nim = "0110223089"
prodi = "Teknik Informatika"
peminatan = "Visualisasi Data"


mata_kuliah = ["Dasar-Dasar Pemrograman", "Basis Data", "Big Data", 
            "Pemrograman Web 1", "Bahasa Indonesia", "Pendidikan Agama", "Visualisasi Data"]
nilai = [90, 85, 92, 87, 80, 75, 95]

# Membuat figure dan axis
plt.figure(figsize=(10, 6))

# Membuat bar chart horizontal
bars = plt.barh(mata_kuliah, nilai, color='lightcoral', edgecolor='maroon')

for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width + 1, bar.get_y() + bar.get_height()/2, f'{width}', 
            ha='left', va='center')

# Menambahkan data diri di bagian atas visualisasi
plt.figtext(0.5, 0.95, f"Nama: {nama}\nNIM: {nim}\nProgram Studi: {prodi}\nPeminatan: {peminatan}",
            ha='center', va='top', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

# Menambahkan judul dan label
plt.title('Nilai Akhir Mata Kuliah', fontsize=14)
plt.xlabel('Nilai Akhir Kuliah')
plt.ylabel('')

# Mengatur batas sumbu x
plt.xlim(0, 100)

# Mengatur tampilan grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.gca().invert_yaxis()

plt.tight_layout()

plt.show()