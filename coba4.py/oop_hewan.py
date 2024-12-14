class Animal:
    def __init__(self):
        self.animals = []

    def index(self):
        print('Daftar Hewan:')
        for i in self.animals:
            print(f'- {i}')

    def store(self, hewanBaru):
        self.animals.append(hewanBaru)
        print(f'Menambahkan hewan {hewanBaru}')
        self.index()

    def update(self, index, hewanBaru):
        if index < len(self.animals):
            print(f'Hewan {self.animals[index]} diupdate menjadi {hewanBaru}')
            self.animals[index] = hewanBaru
            self.index()
        else:
            print(f'Index {index} tidak ada dalam daftar hewan')

    def destroy(self, index):
        if index < len(self.animals):
            hewanTerhapus = self.animals.pop(index)
            print(f'Hewan {hewanTerhapus} telah dihapus')
            self.index()
        else:
            print(f'Index {index} tidak ada dalam daftar hewan')

# Membuat objek Animal
hewan = Animal()

# Menambahkan hewan ke dalam daftar menggunakan metode store
hewan.store('Monyet')
hewan.store('Kucing')
hewan.store('Anjing')
hewan.store('Rusa')
hewan.store('Sapi')
hewan.store('Kuda')

# Contoh penggunaan metode update
hewan.update(1, 'Kucing Kampung')

# Contoh penggunaan metode destroy
hewan.destroy(3)
