# bilangan bulat
angka = 15
format_str = f"Bilangan bulat = {angka: d}"
print(format_str)

#bilangan dengan ordo ribuan
angka = 2000
format_str = f"Ribuan = {angka:,}"
print(format_str)

#bilangan dengan ordo jutaan
angka = 2000000
format_str = f"Jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"Desimal = {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"Leading zero = {angka:010.2f}"
print(format_str)

# memformat persen
persen = 0.045
fromat_persen = f"Persen = {persen:.2%}"
print(fromat_persen)

# melakukan operasi aritmatika
harga = 10000
jumlah = 5

format_string = f"harga total = RP. {harga*jumlah:,}"
print(format_string)

# fromat angka lain (binary, octal, hexxadecimal)
angka = 277
binary = F"binary = {bin(angka)}"
octal = F"octal = {oct(angka)}"
hex = F"hex = {hex(angka)}"

print(binary)
print(octal)
print(hex)