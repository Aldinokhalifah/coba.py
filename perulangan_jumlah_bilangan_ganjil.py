# Meminta pengguna memasukkan nilai N
N = int(input("Masukkan nilai N: "))

# Inisialisasi jumlah bilangan ganjil
jumlah_ganjil = 0

# Perulangan untuk menghitung jumlah bilangan ganjil
for i in range(1, N+1):
    if i % 2 != 0:
        jumlah_ganjil += i

# Menampilkan hasil
print(f"Jumlah bilangan ganjil dari 1 hingga {N} adalah {jumlah_ganjil}.")

