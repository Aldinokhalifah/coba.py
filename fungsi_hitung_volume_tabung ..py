def hitung_volume_tabung (r,t):
    return 3.14 * r * r * t

r= float(input("Masukkan jari-jari alas:"))
t= float(input("Maukkan tinggi:"))

print("Maka volume tabung adalah:",hitung_volume_tabung(r,t))