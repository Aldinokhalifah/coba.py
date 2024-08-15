def info_pengguna(nama, **kwargs):
    print(f"Nama: {nama}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

info_pengguna("John Doe", umur=30, pekerjaan="Developer", kota="Jakarta")
