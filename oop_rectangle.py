class Rectangle :

    def __init__(self,panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        print("Luas persegi panjang :",self.panjang * self.lebar)

    def keliling(self):
        print("Keliling persegi panjang :",2*self.panjang + 2*self.lebar)

x = Rectangle(12,22)
x.luas()
x.keliling()

   
