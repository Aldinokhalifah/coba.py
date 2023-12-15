angka_pertama = int(input("Masukkan angka pertama: "))
angka_kedua = int(input("Masukkan angka kedua: "))

pilih_operasi = input("Pilih operasi yang akan dipakai (+, *, /, -): ")

match pilih_operasi:
    case "+":
        hasil = angka_pertama + angka_kedua
        print("Hasilnya adalah", hasil)
    case "-":
        hasil = angka_pertama - angka_kedua
        print("Hasilnya adalah", hasil)
    case "*":
        hasil = angka_pertama * angka_kedua
        print("Hasilnya adalah", hasil)
    case "/":
        hasil = angka_pertama / angka_kedua
        print("Hasilnya adalah", hasil)
    case _:
        print("Operasi yang dipilih tidak valid")
