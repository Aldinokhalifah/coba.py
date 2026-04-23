class Queue:
    def __init__(self):
        self.antrean = []

    def enqueue(self, data):
        # Tambahkan data ke belakang list
        self.antrean.append(data)

    def dequeue(self):
        # Cek dulu apakah kosong, kalau tidak, hapus index 0
        # Di Python: self.antrean.pop(0)
        if(len(self.antrean) > 0) :
            self.antrean.pop(0)

    def display(self):
        print("Antrean saat ini:", self.antrean)
        
    def peak(self) :
        if(len(self.antrean) > 0) :
            print(f"Urutan terdepan: {self.antrean[0]}")
        else :
            print("Antrian kosong")


q = Queue()

q.enqueue("Pembeli A")
q.enqueue("Pembeli B")
q.enqueue("Pembeli C")

q.peak()

q.display()

q.dequeue()

q.display()