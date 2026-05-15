class Stack:
    def __init__(self):
        self.items = []
    def push(self, data):
        self.items.append(data)
    def pop(self):
        return self.items.pop() if self.items else None

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, data):
        self.items.append(data)
    def dequeue(self):
        return self.items.pop(0) if self.items else None

def cek_palindrom(teks):
    s = Stack()
    q = Queue()
    
    # 1. Masukkan setiap huruf ke dalam Stack DAN Queue
    for huruf in teks.lower():
        # LENGKAPI DI SINI
        s.push(huruf)
        q.enqueue(huruf)
        pass

    # 2. Bandingkan hasil pop dari Stack dengan dequeue dari Queue
    # Jika ada satu saja yang beda, berarti bukan palindrom
    while len(s.items) > 0 and len(q.items) > 0:
        if s.pop() != q.dequeue():
            return False
        
    return True

# Test
print(f"Apakah RADAR palindrom? {cek_palindrom('RADAR')}")
print(f"Apakah ALDINO palindrom? {cek_palindrom('ALDINO')}")