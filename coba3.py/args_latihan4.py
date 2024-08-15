def maks(*angka):
    for i in angka:
        print(f'Angka: {i}')
        
    print(f'Maksimal: {max(angka)}')
    print(f'Minimal: {min(angka)}')
    print(f'Rata-rata: {sum(angka) / len(angka):.2f}')
    print(f'Total: {sum(angka)}')
maks(12,98,100,34,65,34,76)