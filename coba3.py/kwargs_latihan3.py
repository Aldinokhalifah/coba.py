def kartu_identitas(nama, umur, **info):
    print(f'Nama: {nama}')
    print(f'Umur: {umur}')

    for key, value in info.items():
        print(f'{key} : {value}')

print(kartu_identitas('AL', 19, pekerjaan='Programmer', alamat='Jakarta', no_telp=123245))