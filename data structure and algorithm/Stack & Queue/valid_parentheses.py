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

def is_balanced(kode):
    s = Stack()
    # Dictionary untuk memetakan pasangan kurung tutup ke bukanya
    pasangan = {')': '(', ']': '[', '}': '{'}
    
    for karakter in kode:
        # Jika ketemu kurung buka, masukkan ke Stack
        if karakter in "([{":
            s.push(karakter)
        
        # Jika ketemu kurung tutup
        elif karakter in ")]}":
            # Kasus 1: Ada tutup tapi Stack kosong (berarti tidak ada bukanya)
            if s.is_empty():
                return False
            
            # Kasus 2: Ambil yang teratas, cek apakah cocok dengan pasangannya
            teratas = s.pop()
            if teratas != pasangan[karakter]:
                return False
                
    # Di akhir, Stack harus benar-benar kosong agar dianggap seimbang
    return s.is_empty()

# --- Test Case ---
print(is_balanced("({[]})"))      # True
print(is_balanced("([)]"))        # False (Urutan salah)
print(is_balanced("((())"))       # False (Kurang tutup)
print(is_balanced("print(10)"))   # True (Mengabaikan karakter selain kurung)