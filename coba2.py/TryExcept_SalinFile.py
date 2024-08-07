def salin_file():
    try:
        sumber = input("Masukkan nama file sumber: ")
        tujuan = input("Masukkan nama file tujuan: ")
        
        with open(sumber, 'r') as file_sumber:
            konten = file_sumber.read()
        
        with open(tujuan, 'w') as file_tujuan:
            file_tujuan.write(konten)
        
        print(f"Konten berhasil disalin dari {sumber} ke {tujuan}")
    except FileNotFoundError:
        print(f"Kesalahan: File '{sumber}' tidak ditemukan.")
    except IOError:
        print("Kesalahan: Terjadi masalah saat menulis ke file tujuan.")

# Memanggil fungsi untuk uji coba
salin_file()