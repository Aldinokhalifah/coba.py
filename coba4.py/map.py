products = [
    {"nama": "Laptop", "harga": 10000000, "diskon": 10, "jumlah": 4},
    {"nama": "Smartphone", "harga": 7000000, "diskon": 15, "jumlah": 4},
    {"nama": "Tablet", "harga": 3000000, "diskon": 5, "jumlah": 2},
    {"nama": "Headphone", "harga": 1000000, "diskon": 20, "jumlah": 6},
    {"nama": "Charger", "harga": 500000, "diskon": 0, "jumlah": 9},
]

def hitung_harga_akhir(produk):
    harga_awal = produk["harga"]
    diskon = produk["diskon"]
    jumlah = produk["jumlah"]
    harga_akhir = harga_awal * (1 - diskon / 100)
    pajak = harga_akhir * 0.10
    harga_setelah_pajak = harga_akhir + pajak
    total_biaya = harga_setelah_pajak * jumlah
    return {
        "nama": produk["nama"], 
        "harga_akhir": harga_akhir, 
        "harga_setelah_pajak": harga_setelah_pajak, 
        "total_biaya": total_biaya
    }

harga_akhir = list(map(hitung_harga_akhir, products))

print('\nHarga akhir dari produk:')
for i in harga_akhir:
    print(f'{i["nama"]}: RP{i["harga_akhir"]:,}')

print('\nHarga akhir dari produk setelah ditambah pajak:')
for i in harga_akhir:
    print(f'{i["nama"]}: RP{i["harga_setelah_pajak"]:,}')

print('\nHarga total biaya dari produk:')
for i in harga_akhir:
    print(f'{i["nama"]}: RP{i["total_biaya"]:,}')

print('\nProduk dengan harga akhir di bawah 5.000.000 setelah pajak:')
for i in harga_akhir:
    if i["harga_setelah_pajak"] < 5000000:
        print(f'{i["nama"]}: RP{i["harga_setelah_pajak"]:,}')
