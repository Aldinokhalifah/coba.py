students = [
    {"nama": "Alice", "program_studi": "Informatika", "IPK": 3.8},
    {"nama": "Bob", "program_studi": "Sistem Informasi", "IPK": 3.2},
    {"nama": "Charlie", "program_studi": "Informatika", "IPK": 3.5},
    {"nama": "Diana", "program_studi": "Teknik Elektro", "IPK": 3.1},
    {"nama": "Eve", "program_studi": "Informatika", "IPK": 2.9},
]

# Filter mahasiswa dengan IPK di atas 3.5
ipk = list(filter(lambda x: x['IPK'] > 3.5, students))
print('Mahasiswa IPK di atas 3.5:')
for i, student in enumerate(ipk, start=1):
    print(f'{i}. {student["nama"]}')

# Filter mahasiswa dari program studi Informatika
prodi = list(filter(lambda i: i['program_studi'] == 'Informatika', students))
print('\nMahasiswa Prodi Informatika:')
for i, student in enumerate(prodi, start=1):
    print(f'{i}. {student["nama"]}')

# Filter mahasiswa dengan IPK di bawah 3.0
ipk2 = list(filter(lambda y: y['IPK'] < 3.0, students))
print('\nMahasiswa IPK di bawah 3.0:')
for i, student in enumerate(ipk2, start=1):
    print(f'{i}. {student["nama"]}')

# filter prodi informatika dan ipk 3.0
# Definisikan fungsi lambda untuk filter mahasiswa dari prodi Informatika dengan IPK di atas 3.0
fungsi = lambda student: student['program_studi'] == 'Informatika' and student['IPK'] > 3.0

# Filter mahasiswa sesuai dengan kriteria
mh = list(filter(fungsi, students))

# Tampilkan hasil
print('\nMahasiswa prodi Informatika dan IPK di atas 3.0:')
for i, student in enumerate(mh, start=1):
    print(f'{i}. {student["nama"]}, IPK : {student["IPK"]}')

