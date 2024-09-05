def divide_numbers():
    try:
        input1 = float(input('Masukkan angka pertama: '))  # Mengonversi input ke float
        input2 = float(input('Masukkan angka kedua: '))    # Mengonversi input ke float
        hitung = input1 / input2
        print(f"Hasil dari pembagian {input1} dibagi {input2} : {hitung}")
    except ValueError:
        print('Kesalahan: Nilai harus berupa angka yang valid.')
    except ZeroDivisionError:
        print('Kesalahan: Tidak bisa membagi dengan angka nol.')

divide_numbers()
