# Membuat matriks 3x3
matriks = []

# Memasukkan elemen-elemen matriks
for i in range(3):
    baris = input(f"Masukkan elemen matriks (baris {i+1}, pisahkan dengan spasi): ")
    elemen = [int(x) for x in baris.split()]
    matriks.append(elemen)

# Mencetak matriks
print("\nMatriks Awal:")
for baris in matriks:
    print(" ".join(map(str, baris)))

# Membuat matriks transpose
transpose = [[matriks[j][i] for j in range(len(matriks))] for i in range(len(matriks[0]))]

# Mencetak matriks transpose
print("\nMatriks Transpose:")
for baris in transpose:
    print(" ".join(map(str, baris)))
