kalimat = "belajar pemrograman"


hasil = {}
vokal = ['a', 'i', 'u', 'e', 'o']

for i in kalimat:
    for huruf in vokal:
        if i == huruf and i in vokal:
            hasil.update({i : 1})
        else:
            hasil.update({i : 0})

print(hasil)