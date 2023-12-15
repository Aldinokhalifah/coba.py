masukkan_suhu= int(input("masukkan suhu :"))
Masukkan_satuan= input("masukkan satuan (C/F) :")

match Masukkan_satuan:
    case "C":
        rumus= (masukkan_suhu - 32) * 5/9
        print("Hasil Konversi adalah",rumus,"Fahrenheit")
    case "F":
        rumus= (masukkan_suhu * 9/5) + 32
        print("Hasil Konversi adalah",rumus,"Celcius")
    case _:
        print("Satuan yang dimasukkan tidak valid")