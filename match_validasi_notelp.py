import re

def validasi_nomor_telepon(nomor_telepon):
    # Definisikan pola regex untuk validasi nomor telepon
    pola = r'^\+62\d{10}$'
    
    # Lakukan pencocokan pola dengan nomor telepon yang diberikan
    hasil_pencocokan = re.match(pola, nomor_telepon)
    
    # Periksa apakah pencocokan berhasil
    if hasil_pencocokan:
        print("Nomor telepon valid!")
    else:
        print("Nomor telepon tidak valid. Pastikan dimulai dengan \"+62\" dan memiliki 10 digit angka.")

# Meminta pengguna memasukkan nomor telepon
nomor_telepon_input = input("Masukkan nomor telepon: ")

# Memanggil fungsi validasi_nomor_telepon dengan nomor telepon yang dimasukkan pengguna
validasi_nomor_telepon(nomor_telepon_input)
