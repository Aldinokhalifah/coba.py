class Animal:
    def __init__(self,nama, makanan):
        self.nama = nama
        self.makanan = makanan

    def info_nama(self):
        print(f'Ini adalah {self.nama}')

    def info_makanan(self):
        print((f'Memakan {self.makanan}'))

class cat(Animal):
    def __init__(self, nama, makanan, umur):
        super().__init__(nama, makanan)
        self.umur = umur


    def sound(self):
        print('miau miau')
    
    def info_umur(self):
        print(f'Umur saya {self.umur} tahun')

class dog(Animal):
    def __init__(self, nama, makanan, umur):
        super().__init__(nama, makanan)
        self.umur = umur


    def sound(self):
        print('woof woof')
    
    def info_umur(self):
        print(f'Umur saya {self.umur} tahun')

    def info_makanan(self):
         super().info_makanan()
         print(f'Makanan kesukaan {self.makanan}')

    

my_cat = cat('kucing', 'ikan',20)
my_cat.info_nama()
my_cat.info_makanan()
# my_cat.sound()
my_cat.info_umur()

my_dog = dog('anjing', 'daging',22)
my_dog.info_nama()
my_dog.info_makanan()
# my_dog.sound()
my_dog.info_umur()

animals = [my_cat, my_dog]

for i in animals:
    i.sound()