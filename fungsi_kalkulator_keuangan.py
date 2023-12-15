def bunga_sederhana(modal, tingkat_bunga, waktu):
    return modal * (1 + tingkat_bunga * waktu)
    
def bunga_majemuk(modal, tingkat_bunga, waktu,n):
    return modal * (1 + tingkat_bunga / n) ** (n * waktu)

modal=float(input("masukkan modal awal:"))
tingkat_bunga=float(input("Masukkan tingkat bunga tahunan (dalam persen):")) / 100
waktu=float(input("Masukkan waktu investasi dalam tahun:"))
jenis_bunga=float(input("Pilih jenis bunga (1: Sederhana, 2: Majemuk):"))

match jenis_bunga:
    case 1:
        hasiil_akhir=bunga_sederhana(modal, tingkat_bunga, waktu)
        print("Modal awal :",modal)
        print("Tingkat bunga tahunan :",tingkat_bunga)
        print("Waktu  investasi :",waktu)
        print("Hasil akhirnya :",hasiil_akhir)
    case 2:
      n=int(input("Masukkan jumlah kali bunga majemuk diperhitungkan per tahun: "))
      hasiil_akhir=bunga_majemuk(modal, tingkat_bunga, waktu,n)
      print("Modal awal :",modal)
      print("Tingkat bunga tahunan :",tingkat_bunga)
      print("Waktu  investasi :",waktu)
      print("Hasil akhirnya :",hasiil_akhir)  
    case _:
        print("Tidak Valid!!!")
