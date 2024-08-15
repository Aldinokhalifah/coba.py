def rata_rata(*nilai):
    for i in nilai:
        print(f'Nilai: {i}')
    
    return sum(nilai) / len(nilai)

print(rata_rata(89, 87, 90, 95, 86, 77, 98, 100, 78, 86))
