def dict():
    try:
        dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
        kunci = input('Masukkan kunci: ')
        nilai = dict[kunci]
        print(f'Nilai untuk kunci  {kunci} adalah {nilai}')
    except KeyError:
        print(f'Kesalahan: kunci {kunci} tidak ditemukan')

dict()