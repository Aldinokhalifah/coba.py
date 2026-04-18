import matplotlib.pyplot as plt

# Data sample
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10, 20, 15, 25, 30, 45, 40, 50, 60, 55, 65, 70]
product_B_sales = [5, 10, 8, 15, 18, 20, 22, 30, 25, 35, 40, 45]

# Buat plot garis produk A
plt.plot(months, product_A_sales)

# Judul utama
plt.title('Penjualan Produk A Per Bulan')

# Label sumbu
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penjualan')

# Tampilkan nama kelompok dan NIM di atas grafik
nama_kelompok = 'Kelompok: Aldino Khalifah, Muhammad Nur Raply, Kheril Irli Januar'
nim_list = ['0110223089, 0110223098, 0110223111']
nim_text = ' | '.join(nim_list)

plt.text(0.5, 1.25, nama_kelompok, ha='center', va='bottom', transform=plt.gca().transAxes,
         fontsize=12, fontweight='bold')
plt.text(0.5, 1.15, nim_text, ha='center', va='bottom', transform=plt.gca().transAxes,
         fontsize=11)

plt.tight_layout(rect=[0, 0, 1, 0.9])  # Sisakan ruang atas lebih besar agar teks tidak terpotong
plt.show()