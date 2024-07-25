kalimat = "Pemrograman Python sangat menyenangkan dan powerful!"
print(kalimat)

jumlah = len(kalimat)
print(jumlah)

kata_kalimat = kalimat.split()
print(kata_kalimat)

kata_balik = kata_kalimat[::-1]
print(kata_balik)

kalimat_gabungan = ' '.join(kata_kalimat)
print("Kalimat gabungan:", kalimat_gabungan)

kalimat_upper = kalimat.upper()
print("Kalimat uppercase:", kalimat_upper)
