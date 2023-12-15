def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

# Memanggil fungsi dengan input "Hello, World!"
input_text = str(input("masukkan kalimat:"))
result = reverse_string(input_text)

# Mencetak hasilnya
print("Hasilnya adalah:", result)
