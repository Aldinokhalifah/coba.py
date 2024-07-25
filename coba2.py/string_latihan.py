nama_depan = 'Ucup'
nama_tengah = 'D'
nama_akhir = 'Fame'

nama_lengkap =f'{nama_depan} {nama_tengah} {nama_akhir}'
print(nama_lengkap)

# mneghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari nama lengkap =",panjang)

# mengecek apakah ada karakter atau string di dalam string
d = "a"
status = d in nama_lengkap
print('huruf a ada di dalam nama lengkap =', status)

d = "d"
status = d not in nama_lengkap
print('huruf d tidak ada di dalam nama lengkap =', status)

# indexing
print(f"index ke-0 = {nama_lengkap[0]}")
print(f"index ke-5 = {nama_lengkap[5]}")
print(f"index ke-(-1) = {nama_lengkap[-1]}")
print(f"index ke-[0:4] = {nama_lengkap[0:4]}")

# item paling kecil dan besar
print(f'item paling kecil : {min(nama_lengkap)}')
print(f'item paling besar : {max(nama_lengkap)}')

# operator dalam bentuk method
data= "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada", data ,"=", jumlah)