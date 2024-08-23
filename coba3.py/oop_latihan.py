class orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def halo(self):
        print(f'Halo nama saya {self.nama}')

    def info_umur(self):
        print(f'Umur saya {self.umur}')

my_class = orang('AL', 19)
print(my_class.nama)
my_class.halo()
print(my_class.umur)
my_class.info_umur()
