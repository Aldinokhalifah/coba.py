class Restoran:
    def open(self):
        print("Selamat Datang di toko kami")
        pesan = input("Apakah kamu ingin memesan sesuatu? ").lower()
        match pesan:
            case 'iya':
                jenis_pesan = input("Apakah kamu ingin memesan makanan atau minuman? ").lower()
                if jenis_pesan == 'makanan':
                    self.makanan()
                elif jenis_pesan == 'minuman':
                    self.minuman()
                else:
                    print("Pilihan tidak valid.")
            case 'tidak':
                print("Baik, terima kasih telah mengunjungi toko kami!")
            case _:
                print("Pilihan tidak valid.")

    def makanan(self):
        makanan = [
            {'nama': 'Nasi goreng', 'harga': 10000},
            {'nama': 'Nasi Uduk', 'harga': 5000},
            {'nama': 'Lontong Sayur', 'harga': 12000},
            {'nama': 'Mie Goreng', 'harga': 14000}
        ]
        print("Menu Makanan:")
        for item in makanan:
            print(f"{item['nama']}: Rp{item['harga']}")

        pesanan = input("Makanan apa yang ingin kamu pesan? ").lower()
        for item in makanan:
            if item['nama'].lower() == pesanan:
                print(f"Makanan yang kamu pesan: {item['nama']}, Harga: Rp{item['harga']}")
                pembayaran = input("Lanjutkan Pembayaran? ").lower()
                match pembayaran:
                    case 'iya':
                        self.pembayaran()
                        return
                    case 'tidak':
                        print("Pesanan dibatalkan.")
                        return
        print("Makanan yang kamu pesan tidak ada di menu.")

    def minuman(self):
        minuman = [
            {'nama': 'Air Putih', 'harga': 1000},
            {'nama': 'Jus', 'harga': 15000},
            {'nama': 'Susu', 'harga': 12000},
            {'nama': 'Soda', 'harga': 20000}
        ]
        print("Menu Minuman:")
        for item in minuman:
            print(f"{item['nama']}: Rp{item['harga']}")

        pesanan = input("Minuman apa yang ingin kamu pesan? ").lower()
        for item in minuman:
            if item['nama'].lower() == pesanan:
                print(f"Minuman yang kamu pesan: {item['nama']}, Harga: Rp{item['harga']}")
                pembayaran = input("Lanjutkan Pembayaran? ").lower()
                match pembayaran:
                    case 'iya':
                        self.pembayaran()
                        return
                    case 'tidak':
                        print("Pesanan dibatalkan.")
                        return
        print("Minuman yang kamu pesan tidak ada di menu.")

    def pembayaran(self):
        print("Pembayaran berhasil. Terima kasih sudah memesan!")

restoran = Restoran()
restoran.open()