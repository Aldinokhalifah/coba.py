# Inisialisasi dua angka pertama dalam deret Fibonacci
a, b = 0, 1

# Gunakan loop for untuk mencetak 10 suku pertama
for _ in range(10):
    print(a)
    a, b = b, a + b
