def faktorial_rekursif(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial_rekursif(n - 1)

print("Faktorial Rekursif")
n = int(input("Masukkan angka: "))

hasil_faktorial = faktorial_rekursif(n)
print(f"Maka hasil faktorial rekursif dari {n} yaitu {hasil_faktorial}")
