arr = [4, 5, 1, 2, 1, 2, 5]

# Hitung frekuensi tiap elemen
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1

# Cari elemen pertama yang frekuensinya 1
first_not_duplicate = None
for num in arr:
    if freq[num] == 1:
        first_not_duplicate = num
        break

if first_not_duplicate is not None:
    print(f'Elemen pertama yang tidak duplikat: {first_not_duplicate}')
else:
    print('Semua elemen duplikat')
