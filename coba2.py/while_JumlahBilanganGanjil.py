n = int(input("Masukkan angka:"))

jumlah_ganjil = 0
i = 1

while i <= n:
    if i % 2 != 0:
        jumlah_ganjil += i
    i += 1

print(f"Jumlah bilangan ganjil dari 1 hingga {n} adalah {jumlah_ganjil}.")
