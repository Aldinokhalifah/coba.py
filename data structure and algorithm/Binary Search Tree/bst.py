class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_rekursif(self.root, data)

    def _insert_rekursif(self, node_saat_ini, data):
        if data < node_saat_ini.data:
            if node_saat_ini.left is None:
                node_saat_ini.left = Node(data)
            else:
                self._insert_rekursif(node_saat_ini.left, data)
        else:
            if node_saat_ini.right is None:
                node_saat_ini.right = Node(data)
            else:
                self._insert_rekursif(node_saat_ini.right, data)

    # --- FUNGSI UTAMA SEARCH ---
    def search(self, data):
        # Memulai pencarian rekursif dari root
        return self._search_rekursif(self.root, data)

    # Helper function menggunakan rekursif (Logika kamu sudah mantap di sini!)
    def _search_rekursif(self, node_saat_ini, data):
        if node_saat_ini is None:
            return False
        elif node_saat_ini.data == data:
            return True
        elif data < node_saat_ini.data:
            return self._search_rekursif(node_saat_ini.left, data)
        else:
            return self._search_rekursif(node_saat_ini.right, data)

    # Fungsi Utama yang dipanggil dari luar
    def cetak_inorder(self):
        print("Isi BST (In-Order): ", end="")
        self._inorder_rekursif(self.root)
        print() # Menambah baris baru di akhir

    # Helper function rekursif
    def _inorder_rekursif(self, node_saat_ini):
        if node_saat_ini is not None:
            # 1. Kunjungi anak kiri dulu sampai mentok
            self._inorder_rekursif(node_saat_ini.left)
            
            # 2. Cetak data node saat ini
            print(node_saat_ini.data, end=" ")
            
            # 3. Kunjungi anak kanan
            self._inorder_rekursif(node_saat_ini.right)
            
    def hitung_total(self):
        return self._hitung_total_rekursif(self.root)
    
    def _hitung_total_rekursif(self, node_saat_ini):
        if node_saat_ini is None:
            return 0
        return node_saat_ini.data + self._hitung_total_rekursif(node_saat_ini.left) + self._hitung_total_rekursif(node_saat_ini.right)
    
    def hitung_total_node(self):
        return self._hitung_total_node(self.root)

    def _hitung_total_node(self, node_saat_ini):
        if node_saat_ini is None:
            return 0
        return 1 + self._hitung_total_node(node_saat_ini.left) + self._hitung_total_node(node_saat_ini.right)

pohon = BST()
pohon.insert(50)
pohon.insert(30)
pohon.insert(70)
pohon.insert(20)
pohon.insert(40)

print(pohon.search(40))  # Harusnya: True
print(pohon.search(90))  # Harusnya: False
pohon.cetak_inorder()
print(pohon.hitung_total())
print(pohon.hitung_total_node())