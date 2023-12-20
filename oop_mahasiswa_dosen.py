class Mahasiswa :
    def __init__(self,nama,umur,jurusan,IPK):
        self.nama = nama
        self.umur = umur
        self.jurusan = jurusan
        self.ipk = IPK


    def naik(self,perubahan):
        self.ipk += perubahan

    def turun(self,perubahan):
        self.ipk -= perubahan


    def cek(self):
        if self.ipk >= 3.0 :
            print("Anda dinyatakan lulus dengan IPK",self.ipk)
        else :
            print("Anda dinyatakan tidak lulus")

    def cetak(self):
        print(f"""
            Nama \t: {self.nama}
            Umur \t: {self.umur}
            Jurusan \t: {self.jurusan}
            IPK \t: {self.ipk}   """)
        
class Dosen :
    def __init__(self,nama,umur,matkul):
         self.nama = nama
         self.umur = umur
         self.matkul = matkul

    def ucap(self):
        print("Selamat Pagi,profesor",self.nama)

    def baru(self,matkul_baru):
        print("Profesor",self.nama,"diganti mata kuliah yang ia ajar menjadi",matkul_baru)


    def info(self):
        print(f"""
            Nama \t \t: {self.nama}
            Umur \t \t: {self.umur}
            Matkul yang diajar \t: {self.matkul} """)





x = Mahasiswa("Haryanto",20,"Teknik Informatika",3.88)
x.naik(1.2)
x.cetak()
x.cek()

y = Dosen("Agus",44,"Teknik Informatika")
y.info()
y.ucap()
y.baru("Sistem Informasi")