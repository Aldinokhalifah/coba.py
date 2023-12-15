import random

def hitung_bilangan_genap(daftar_bilangan):
    jumlah_genap = 0
    for bilangan in daftar_bilangan:
        if bilangan % 2 == 0:
            jumlah_genap += bilangan
    return jumlah_genap

# Membuat daftar bilangan bulat secara acak
daftar_acak = [random.randint(1, 100) for _ in range(10)]

# Mencetak daftar acak
print("Daftar bilangan acak:", daftar_acak)

# Memanggil fungsi untuk menghitung jumlah bilangan genap
hasil = hitung_bilangan_genap(daftar_acak)

# Mencetak hasil
print("Jumlah bilangan genap dalam daftar:", hasil)
