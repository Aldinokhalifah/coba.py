def hitung_luas_persegi ():
    return sisi * sisi

def hitung_luas_lingkaran ():
    return 3.14 * (jari_jari ** 2)

sisi= float(input("Maasukkan sisi:"))
jari_jari= float(input("Maasukkan jari-jari:"))

print(f"Luas persegi dengan sisi {sisi} adalah",hitung_luas_persegi())
print(f"Luas lingkaran dengan jari-jari {jari_jari}adalah",hitung_luas_lingkaran())