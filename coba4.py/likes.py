class Likes:
    def __init__(self):
        self.akun = [
            {'nama': 'user 1', 'like': 0},
            {'nama': 'user 2', 'like': 0},
            {'nama': 'user 3', 'like': 0},
            {'nama': 'user 4', 'like': 0},
            {'nama': 'user 5', 'like': 0},
        ]

    def postingan(self):
        print('Akun dan likenya:')
        for user in self.akun:
            print(f"Nama: {user['nama']}, Like: {user['like']}")

        tambah = str(input('Tambahkan like untuk akun? ').lower())
        if tambah == 'iya':
            self.tambah()

    def tambah(self):
        nama_akun = input('Akun yang mana mau ditambah likenya? ').lower()
        akun_ditemukan = False

        for user in self.akun:
            if user['nama'].lower() == nama_akun:
                user['like'] += 1
                akun_ditemukan = True
                print(f"Like dari akun {user['nama']} berhasil ditambah.")
                break

        if not akun_ditemukan:
            print('Nama akun tidak valid.')

        print('Akun dan likenya:')
        for user in self.akun:
            print(f"Nama: {user['nama']}, Like: {user['like']}")

like = Likes()
like.postingan()
