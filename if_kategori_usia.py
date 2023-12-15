masukkan_usia = int(input("Masukkan usia: "))

if 0 <= masukkan_usia <= 4:
    rentan = "balita"
elif 5 <= masukkan_usia <= 12:
    rentan = "anak-anak"
elif 13 <= masukkan_usia <= 17:
    rentan = "remaja"
elif 18 <= masukkan_usia <= 59:
    rentan = "dewasa"
elif masukkan_usia >= 60:
    rentan = "lanjut usia"
else:
    rentan = "kategori usia tidak valid"

print("Kategori usia anda adalah", rentan)
