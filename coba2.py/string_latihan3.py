kalimat = "Python adalah bahasa pemrograman yang sangat powerful dan mudah dipelajari"
print(kalimat)

# menghitung kata yg ada di dlm string
jumlah = kalimat.count("Python")
print(jumlah)

# mengganti kata dlm string
ganti = kalimat.replace("powerful", "canggih")
print(ganti)

# mencari kata terpanjang di dlm string
kata_terpanjang = max(kalimat.split(), key=len)
print(kata_terpanjang)

# membalik urutan string
kata_balik = ' '.join(kalimat.split()[::-1])
print(kata_balik)