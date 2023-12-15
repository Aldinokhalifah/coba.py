angka_pertama = int(input("Masukkan angka pertama: "))
angka_kedua = int(input("Masukkan angka kedua: "))

pilih_operasi = input("Pilih operasi yang akan dipakai (+, *, /, -): ")

match pilih_operasi:
    case "+":
        hasil = angka_pertama + angka_kedua
        print(f"Angka pertama: {angka_pertama}")
        print(f"Angka kedua: {angka_kedua}")
        print(f"Pilihan operator: {pilih_operasi}")
        print(f"Hasil operator: {angka_pertama} {pilih_operasi} {angka_kedua} = {hasil}")
    case "-":
        hasil = angka_pertama - angka_kedua
        print(f"Angka pertama: {angka_pertama}")
        print(f"Angka kedua: {angka_kedua}")
        print(f"Pilihan operator: {pilih_operasi}")
        print(f"Hasil operator: {angka_pertama} {pilih_operasi} {angka_kedua} = {hasil}")
    case "*":
        hasil = angka_pertama * angka_kedua
        print(f"Angka pertama: {angka_pertama}")
        print(f"Angka kedua: {angka_kedua}")
        print(f"Pilihan operator: {pilih_operasi}")
        print(f"Hasil operator: {angka_pertama} {pilih_operasi} {angka_kedua} = {hasil}")
    case "/":
        hasil = angka_pertama / angka_kedua
        print(f"Angka pertama: {angka_pertama}")
        print(f"Angka kedua: {angka_kedua}")
        print(f"Pilihan operator: {pilih_operasi}")
        print(f"Hasil operator: {angka_pertama} {pilih_operasi} {angka_kedua} = {hasil}")
    case _:
        print("Operasi yang dipilih tidak valid")
