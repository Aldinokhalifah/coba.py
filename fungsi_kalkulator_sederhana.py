def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b != 0:
        return a / b
    else:
        print("Pembagian dengan nol tidak diizinkan!")
        return None

angka_pertama = int(input("Masukkan angka pertama: "))
angka_kedua = int(input("Masukkan angka kedua: "))
pilih_operasi = int(input("Pilih operasi (1: Penjumlahan, 2: Pengurangan, 3: Perkalian, 4: Pembagian): "))

if 1 <= pilih_operasi <= 4:
    if pilih_operasi == 1:
        hasil = penjumlahan(angka_pertama, angka_kedua)
        print(f"Hasil Penjumlahan: {hasil}")
    elif pilih_operasi == 2:
        hasil = pengurangan(angka_pertama, angka_kedua)
        print(f"Hasil Pengurangan: {hasil}")
    elif pilih_operasi == 3:
        hasil = perkalian(angka_pertama, angka_kedua)
        print(f"Hasil Perkalian: {hasil}")
    elif pilih_operasi == 4:
        hasil = pembagian(angka_pertama, angka_kedua)
        if hasil is not None:
            print(f"Hasil Pembagian: {hasil}")
else:
    print("Operasi yang dipilih tidak valid!")
