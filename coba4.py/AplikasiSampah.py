class Edukasi :
    def tampilkanEdukasi() :
        print('\n === Edukasi Pengelolaan Sampah ===')
        print('- Pisahkan sampah organik dan anorganik.')
        print('- Kurangi penggunaan plastik sekali pakai.')
        print('- Manfaatkan barang bekas untuk didaur ulang.')

class LaporanSampah :
    def __init__(self):
        self.laporan = []

    def tambahLaporan(self, isiLaporan) :
        self.laporan.append(isiLaporan)
        
        while True:
            tanya = input("Apakah anda mau menambah laporan lagi? (iya / tidak) ").lower()
            if tanya == "iya":
                tambahLagi = input('Masukkan laporan sampah: ')
                self.laporan.append(tambahLagi)
            else:
                break

        print('Laporan telah ditambahkan!')

    
    def tampilkanLaporan(self):
        for i in self.laporan:
            print(f"{self.laporan.index(i) + 1}. {i}")

class BankSampah:
    def __init__(self):
        self.totalBerat = 0
    
    def setorSampah(self):
        while True:
            berat_sampah = int(input("Masukkan berat sampah(KG): "))
            self.totalBerat += berat_sampah
            
            tanya = input("Apakah anda mau menambah sampah lagi? (iya / tidak) ").lower()
            if tanya != "iya":
                break
        
        print(f"Sampah berhasil disetor, Total berat sekarang: {self.totalBerat}")

    def tampilkanSaldo(self) :
        print('\n === Informasi Bank Sampah ===')
        print(f'Total berat sampah: {self.totalBerat} KG')
        print(f'Total estimasi saldo: Rp{self.totalBerat * 500}')
    

def main():
    edukasi = Edukasi()
    laporan_sampah = LaporanSampah()
    bank_sampah = BankSampah()

    while True:
        print("\n=== Aplikasi Pengelolaan Sampah ===")
        print("1. Edukasi")
        print("2. Laporkan Sampah")
        print("3. Bank Sampah")
        print("4. Keluar")
        
        try:
            pilihan = int(input("Pilih menu: "))
            
            if pilihan == 1:
                Edukasi.tampilkanEdukasi()
            elif pilihan == 2:
                laporan = input("Tulis laporan sampah: ")
                laporan_sampah.tambahLaporan(laporan)
                laporan_sampah.tampilkanLaporan()
            elif pilihan == 3:
                bank_sampah.setorSampah()
                bank_sampah.tampilkanSaldo()
            elif pilihan == 4:
                print("Terima kasih telah menggunakan aplikasi ini!")
                break
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Masukkan angka yang valid!")

if __name__ == "__main__":
    main()