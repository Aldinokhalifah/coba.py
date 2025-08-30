arr = [2, 5, 3, 5, 2, 6]
seen = set()

first_duplicate = None
for num in arr:
    if num in seen:
        first_duplicate = num
        break
    seen.add(num)

if first_duplicate:
    print("Elemen duplikat pertama:", first_duplicate)
else:
    print("Tidak ada duplikat")
