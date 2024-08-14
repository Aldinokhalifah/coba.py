names = ["Alice", "Bob", "Charlotte", "David", "Eve", "Franklin"]

nama = list(filter(lambda x : len(x) < 5, names))
print(nama)

nama2 = list(filter(lambda x : x[0] == 'B', nama))
print(nama2)