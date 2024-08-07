import math

def kuadrat():
    try:
        angka = float(input('Masukkan angka: '))
        if angka < 0:
            raise ValueError('Angka tidak boleh negatif')
        hasil = math.sqrt(angka)
        print(f'Hasil kuadrat dari {angka} adalah : {hasil:.2f}')
    except ValueError as ve:
        print(f'Kesalahan: {ve}')
    
kuadrat()
