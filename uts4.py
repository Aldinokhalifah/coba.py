def hitung_luas_keliling_layang_layang(d1, d2):
    luas = 0.5 * d1 * d2
    keliling = 2 * (d1 + d2)
    return luas, keliling

def hitung_luas_keliling_trapesium(a, b, h):
    luas = 0.5 * (a + b) * h
    keliling = a + b + 2 * ((a-b)**2 + h**2)**0.5
    return luas, keliling

def main():
    nim = int(input("Masukkan NIM: "))
    
    if nim % 2 == 1:  # NIM ganjil, hitung layang-layang
        d1 = float(input("Masukkan panjang diagonal 1: "))
        d2 = float(input("Masukkan panjang diagonal 2: "))
        luas, keliling = hitung_luas_keliling_layang_layang(d1, d2)
        jenis_bangun = "Layang-layang"
    else:  # NIM genap, hitung trapesium
        a = float(input("Masukkan panjang sisi atas: "))
        b = float(input("Masukkan panjang sisi bawah: "))
        h = float(input("Masukkan tinggi: "))
        luas, keliling = hitung_luas_keliling_trapesium(a, b, h)
        jenis_bangun = "Trapesium"

    print(f"\nJenis bangun datar: {jenis_bangun}")
    print(f"Luas {jenis_bangun}: {luas}")
    print(f"Keliling {jenis_bangun}: {keliling}")

if __name__ == "__main__":
    main()

 