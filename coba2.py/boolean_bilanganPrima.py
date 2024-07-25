angka = int(input("Masukkan bilangan bulat positif: "))

if angka > 1:
    for i in range(2, int(angka**0.5) + 1):
        if angka % i == 0:
            print(f'Bilangan {angka} bukan bilangan prima.')
            break
    else:
        print(f'Bilangan {angka} adalah bilangan prima.')
else:
    print(f'Bilangan {angka} bukan bilangan prima.')
