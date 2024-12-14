import re

teks = "Ada 1 apel, 2 jeruk, dan 3 pisang."

# Mencari semua kecocokan dalam suatu list
hasil = re.findall('[0-9]', teks)
print("findall:", hasil)

# Mencari objek spesifik
hasil2 = re.search('jeruk', teks)
if hasil2:
    print("Kata 'jeruk' ditemukan!")
else:
    print("Kata 'jeruk' tidak ditemukan!")

# Memisahkan teks berdasarkan pola RegEx
hasil3 = re.split(r'[, ]', teks)
print("split:", hasil3) 

#  Mengganti suatu karakter
hasil4 = re.sub('[0-9]', '$', teks)
print("sub:", hasil4) 