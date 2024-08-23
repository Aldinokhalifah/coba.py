class car:
    def __init__(self,nama, tahun, odometer, no_rangka):
        self.nama = nama
        self.tahun =  tahun
        self._odometer = odometer
        self.__no_Rangka = no_rangka

    def info_mobil(self):
        print(f'nama mobil {self.nama} dan tahun {self.tahun}')

    def info_odometer(self):
        print(f'odometer: {self._odometer} KM')

    def info_rangka(self):
        print(f"NO rangka: {self.__no_Rangka}")

my_car = car('BMW', 2023, 10000, 12752)
my_car.info_mobil()
print(my_car._odometer)
my_car.info_odometer()
my_car.info_rangka()
# eror
# print(my_car.__no_Rangka)
print(my_car._car__no_Rangka)