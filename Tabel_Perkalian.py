#Tabel_Perkalian
angka = int(input("Masukkan angka untuk tabel perkalian: "))

print(f"Tabel perkalian untuk {angka} adalah:")
for i in range(1, 11):
    hasil = angka * i
    print(f"{angka} x {i} = {hasil}")

