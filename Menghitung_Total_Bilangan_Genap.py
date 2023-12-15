#Menghitung Total Bilangan Genap
ba = int(input("masukkan batas awal"))
bt = int(input("masukkan batas terakhir"))

for i in range(ba,bt + 1):
    if i % 2 == 0:
        print(i)