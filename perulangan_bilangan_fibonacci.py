# Meminta pengguna memasukkan batas deret Fibonacci
batas = int(input("Masukkan batas deret Fibonacci: "))

# Inisialisasi elemen pertama dan kedua
elemen_sebelumnya = 0
elemen_sekarang = 1

# Menampilkan elemen pertama (0) sebagai bagian dari output
print("Deret Fibonacci hingga batas", batas, ":", elemen_sebelumnya, end=", ")

# Perulangan untuk menghasilkan deret Fibonacci
while elemen_sekarang <= batas:
    print(elemen_sekarang, end=", ")

    # Menghitung elemen selanjutnya dalam deret Fibonacci
    elemen_selanjutnya = elemen_sebelumnya + elemen_sekarang

    # Memperbarui nilai elemen_sebelumnya dan elemen_sekarang
    elemen_sebelumnya = elemen_sekarang
    elemen_sekarang = elemen_selanjutnya
