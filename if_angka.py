angka = int(input("Masukkan angka:"))
pilih_operasi = input("Masukkan operasi (+, -, 0):")

if angka > 0:
    print("Angka yang Anda masukkan adalah positif.")
elif angka < 0:
    print("Angka yang Anda masukkan adalah negatif.")
else:
    print("Angka yang Anda masukkan adalah nol.")

if pilih_operasi == "+":
    print(f"Anda memilih operasi penambahan (+).")
elif pilih_operasi == "-":
    print(f"Anda memilih operasi pengurangan (-).")
elif pilih_operasi == "0":
    print(f"Anda memilih operasi nol (0).")
else:
    print(f"Pilihan operasi tidak valid.")
