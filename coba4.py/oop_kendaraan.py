class Kendaraan:
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun

    def info_kendaraan(self):
        print(f'Merk : {self.merk}')
        print(f'Model : {self.model}')
        print(f'Tahun : {self.tahun}')


class Mobil(Kendaraan):
    def __init__(self, merk, model, tahun, jumlah_pintu):
        super().__init__(merk, model, tahun)
        self.jumlah_pintu = jumlah_pintu

    def info_kendaraan(self):
        super().info_kendaraan()  # Jangan gunakan 'return' di sini
        print(f'Jumlah Pintu : {self.jumlah_pintu}')


class Motor(Kendaraan):
    def __init__(self, merk, model, tahun, jenis_stang):
        super().__init__(merk, model, tahun)
        self.jenis_stang = jenis_stang

    def info_kendaraan(self):
        super().info_kendaraan()  # Jangan gunakan 'return' di sini
        print(f'Jenis Stang : {self.jenis_stang}')


class Garasi:
    def __init__(self):
        self.daftar_kendaraan = []

    def tambah_kendaraan(self, kendaraan):
        self.daftar_kendaraan.append(kendaraan)  # Perbaiki typo di sini
        print(f'{kendaraan.merk} {kendaraan.model} berhasil ditambahkan ke garasi.')

    def lihat_kendaraan(self):
        print('Daftar Kendaraan di Garasi:')
        for idx, kendaraan in enumerate(self.daftar_kendaraan, start=1):
            print(f'{idx}.')
            kendaraan.info_kendaraan()

# Membuat objek Mobil dan Motor
mobil1 = Mobil("Toyota", "Avanza", 2020, 4)
motor1 = Motor("Yamaha", "R15", 2018, "sport")

# Membuat objek Garasi
garasi = Garasi()

# Menambahkan kendaraan ke garasi
garasi.tambah_kendaraan(mobil1)
garasi.tambah_kendaraan(motor1)

# Melihat daftar kendaraan di garasi
garasi.lihat_kendaraan()
