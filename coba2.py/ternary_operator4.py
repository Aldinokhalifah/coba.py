angka = 17

def tambah():
    global angka  # Deklarasi bahwa kita akan menggunakan variabel global
    angka += 1
    return angka  # Mengembalikan hasil penambahan

def kurang():
    global angka  # Deklarasi bahwa kita akan menggunakan variabel global
    angka -= 1
    return angka  # Mengembalikan hasil pengurangan

ternary = tambah() if (angka % 2 == 0) else kurang()

print(ternary)  # Menampilkan hasil dari operasi ternary
