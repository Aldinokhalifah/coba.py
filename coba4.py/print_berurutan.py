import string
import random
import time

# Memasukkan huruf, spasi, dan tanda baca ke dalam letters
letters = string.ascii_letters + ' ,.!?'

target = 'Hello, world'  # Contoh target string termasuk spasi dan koma
result = ''  # Mulai dengan string kosong untuk membangun hasil

for letter in target:
    while True:
        i = random.choice(letters)  # Pilih huruf atau karakter acak dari letters
        print(result + i)  # Cetak hasil sementara dengan huruf acak
        if i == letter:  # Jika huruf acak sama dengan huruf target
            result += i  # Tambahkan huruf ke result
            break  # Keluar dari loop
        time.sleep(0.1)  # Jeda selama 0,1 detik
