def profil_pengguna(nama,umur,*hobi, **info_lain):
    print(f'Nama: {nama}')
    print(f'Umur: {umur}')
    print(f'Hobi: ')

    for h in hobi:
        print('-' + h)
    
    for key, value in info_lain.items():
        print(f'{key}: {value}')

print(profil_pengguna('AL', 19, 'Olahraga', 'Lari', 'Belajar', alamat='Jakarta', pekerjaan='Programmer'))
