inputUser = int(input("masukkan angka yang bernilai kurang dari 3 dan lbih dari 10="))

kurangDari = (inputUser < 3)
print("kurang dari 3 =", kurangDari)

lebihDari = (inputUser > 10)
print("lebih dari 10 = ",lebihDari)

benar = kurangDari or lebihDari
print('angka yang anda masukkan =', benar)
 