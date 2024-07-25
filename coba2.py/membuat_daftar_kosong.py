# daftar = []

# angka = int(input('masukkan angka:'))
# stop = input('apakah ingin berhenti setelah ini:')


# if stop == "iya":
#     for i in range(1, angka):
#         print('Daftar:', i)
#         daftar.append(i)
#     print('Daftar: Stop')
#     print('Daftar yang dibuat:', daftar)
           
# else:
#     for i in range(1, angka):
#         print('Daftar:', i)

daftar = []

while True:
    angka = input('Masukkan angka (atau ketik "stop" untuk selesai): ')
    
    if angka.lower() == 'stop':
        break

    try:
        angka = int(angka)
        daftar.append(angka)
    except ValueError:
        print("Input tidak valid, masukkan angka atau ketik 'stop'.")

print('Daftar yang dibuat:', daftar)



