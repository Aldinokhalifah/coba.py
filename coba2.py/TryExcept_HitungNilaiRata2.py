def nilai_rata_rata():
    try:
        nilai_input = input('Masukkan angka yg dipisahkan dengan koma: ')
        nilai_list = [float(nilai) for nilai in nilai_input.split(',')]
        rata_rata = sum(nilai_list) / len(nilai_list)
        print(f"Rata-rata dari nilai yang dimasukkan adalah: {rata_rata:.2f}")
    except ValueError:
        print('Kesalahan: Input tidak valid. Pastikan untuk memasukkan angka yang dipisahkan oleh koma.')
    else:
        nilai_list.sort()
        print(f'Urutan nilai dari yg terendah: {nilai_list}')
        print(f'Nilai  yg terendah: {min(nilai_list)}')
        print(f'Nilai  yg tertinggi: {max(nilai_list)}')

nilai_rata_rata()
