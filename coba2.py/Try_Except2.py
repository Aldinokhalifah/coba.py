def ganjil_genap():
    try:
        angka = int(input('Masukkan angka: '))
        if angka % 2 == 0:
            print(f'{angka} adalah angka genap')
        else:
            print(f'{angka} adalah angka ganjil')
    except ValueError:
        print(f'Kesalahan: Input harus berupa angka')

ganjil_genap()