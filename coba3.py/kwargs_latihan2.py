def total_belanja(**belanja):
    total = 0
    for barang, harga in belanja.items():
        total += harga
        print(f'{barang} : {harga}')

    return total

tb = total_belanja(beras=12000, mie=32000, ayam=56000)
print(f'Total belanjaan: {tb}')