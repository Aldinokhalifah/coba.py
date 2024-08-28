class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False
    
    def return_book(self):
        self.available = True

class library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self,book):
        self.books.append(book)

    def display_books(self):
        for i in self.books:
            status = "Available" if i.available else "Borrowed"
            print(f"{i} - {status}")

    def borrow_book(self,title):
        for i in self.books:
            if i.title == title and i.available:
                i.borrow()
                print(f"You have borrowed '{title}'.")
                return
        print(f"'{title}' is not available.")

    def return_book(self, title):
        for i in self.books:
            if i.title == title and not i.available:
                i.return_book()
                print(f'You have returned {title}.')
                return
        print(f"'{title}' was not borrowed.")
    
    def delete(self):
        self.display_books()
        choose = input('Judul buku mana yang mau dihapus: ')
        
        # Cari buku yang judulnya cocok dengan input pengguna
        for book in self.books:
            if book.title == choose:
                self.books.remove(book)
                print(f'Buku yang berjudul "{choose}" telah dihapus.')
                return

        # Jika buku tidak ditemukan
        print(f'Buku dengan judul "{choose}" tidak ditemukan.')

    def member(self):
        sign_up = input('Nama: ')
        self.members.append(sign_up)  # Tambahkan nama anggota ke daftar

        print('Anggota dari Perpustakaan:')
        for idx, member in enumerate(self.members, start=1):
            print(f'{idx}. {member}')
    
    def delete_member(self):
        if not self.members:
            print('Tidak ada anggota yang terdaftar.')
            return

        print('Anggota dari Perpustakaan:')
        for idx, member in enumerate(self.members, start=1):
            print(f'{idx}. {member}')
        
        delete = input('Anggota mana yang akan dihapus: ')
        
        if delete in self.members:
            self.members.remove(delete)
            print(f'Anggota yang bernama "{delete}" telah dihapus.')
        else:
            print('Anggota yang dimaksud tidak terdaftar')




perpus = library()

book1 = book("Python Programming", "John Doe")
book2 = book("Data Science Handbook", "Jane Smith")
book3 = book("Machine Learning Basics", "Alice Johnson")

perpus.add_book(book1)
perpus.add_book(book2)
perpus.add_book(book3)

print("Available Books in the Library:")
perpus.display_books()

print("\nBorrowing 'Python Programming':")
perpus.borrow_book('Python Programming')

print("\nAvailable Books in the Library after borrowing:")
perpus.display_books()

print("\nReturning 'Python Programming':")
perpus.return_book("Python Programming")

print("\nAvailable Books in the Library after returning:")
perpus.display_books()

print("Daftar Buku Sebelum Penghapusan:")
perpus.display_books()

perpus.delete()

print("\nDaftar Buku Setelah Penghapusan:")
perpus.display_books()


perpus.member()
perpus.member()
perpus.delete_member()




    