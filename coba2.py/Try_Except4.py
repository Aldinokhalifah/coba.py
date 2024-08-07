def tuple():
    try:
        my_tuple = (1,2,3,4,5,6,7)
        akses = int(input('Masukkan indeks: '))
        hasil = my_tuple[akses]
        print(f'Indeks  {akses} dari tuple adalah {hasil}')
    except IndexError:
        print(f'Kesalahan: Indeks ke {akses} tidak ditemukan')
    except ValueError:
        print(f'Kesalahan: Input tidak boleh berupa angka desimal dan tidak boleh huruf')

tuple()