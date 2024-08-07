def konversi_integer():
    try:
        angka = float(input('Masukkan angka desimal: '))
        hasil = int(angka)
        print(f'Nilai {angka} berhasil dikonversi menjadi integer: {hasil}')
    except ValueError:
        print('Kesalahan: Input tidak bisa dikonversi menjadi integer.')

konversi_integer()
