def cek_palindrome():
    input_kata = str(input("Masukkan kata: "))
    return input_kata == input_kata[:: -1]

print(cek_palindrome())