class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def info_produk(self):
        print(f"Nama : {self.nama}")
        print(f"Harga : {self.harga}")
        print(f"Stok : {self.stok}")


class Pelanggan:
    def __init__(self, nama):
        self.nama = nama
        self.keranjang = {}

    def tambah_ke_keranjang(self, produk, jumlah):
        if produk.nama in self.keranjang:
            self.keranjang[produk.nama] += jumlah
        else:
            self.keranjang[produk.nama] = jumlah
        print(f"{jumlah} {produk.nama} ditambahkan ke keranjang.")

    def lihat_keranjang(self):
        print(f'Keranjang belanja {self.nama}')
        for key, value in self.keranjang.items():
            print(f"{key} - Jumlah: {value}")

    def bayar(self):
        self.keranjang.clear()
        print(f'Keranjang telah kosong')


class Toko:
    def __init__(self):
        self.daftar_produk = []

    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)
        print(f'{produk.nama} telah ditambahkan ke toko.')

    def lihat_produk(self):
        print(f'Produk yang tersedia di toko:')
        for idx, produk in enumerate(self.daftar_produk, start=1):
            print(f'{idx}. {produk.nama} - Harga: {produk.harga}, Stok: {produk.stok}')

    def proses_pembelian(self, pelanggan):
        total_harga = 0

        # Periksa stok untuk setiap produk di keranjang pelanggan
        for nama_produk, jumlah in pelanggan.keranjang.items():
            for produk in self.daftar_produk:
                if produk.nama == nama_produk:
                    if produk.stok >= jumlah:
                        # Kurangi stok
                        produk.stok -= jumlah
                        # Hitung total harga
                        total_harga += produk.harga * jumlah
                        print(f"{jumlah} {produk.nama} berhasil dibeli.")
                    else:
                        print(f"Maaf, stok {produk.nama} tidak mencukupi.")
                        return

        print(f"Total harga: {total_harga}")
        pelanggan.bayar()


# Contoh penggunaan
produk1 = Produk("Laptop", 15000000, 10)
produk2 = Produk("Kamera", 5000000, 5)

toko = Toko()
toko.tambah_produk(produk1)
toko.tambah_produk(produk2)

pelanggan1 = Pelanggan("Andi")
pelanggan1.tambah_ke_keranjang(produk1, 2)
pelanggan1.tambah_ke_keranjang(produk2, 1)
pelanggan1.lihat_keranjang()

toko.lihat_produk()
toko.proses_pembelian(pelanggan1)
toko.lihat_produk()
