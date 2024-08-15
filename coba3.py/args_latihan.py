def jumlah_angka(*angka):
    total = 0 
    for i in angka:
        total += i
    return total
print(jumlah_angka(1,2,3,4,5,6,7,8,9))