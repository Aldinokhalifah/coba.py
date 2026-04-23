class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(teks):
    s = Stack()
    
    # 1. Masukkan semua huruf ke Stack
    for huruf in teks:
        s.push(huruf)
    
    hasil_terbalik = ""
    
    # 2. Keluarkan semua sampai habis
    while not s.is_empty():
        hasil_terbalik += s.pop()
        
    return hasil_terbalik

def is_palindrome(teks):
    terbalik = reverse_string(teks)
    return teks.lower() == terbalik.lower()

# Test
nama = "ALDINO"
print(f"Original: {nama}")
print(f"Terbalik: {reverse_string(nama)}")
print(is_palindrome("katak"))