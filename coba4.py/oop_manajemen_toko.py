class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity  

    def update_quantity(self, amount):
        self.quantity += amount
    
    def calculate_total_value(self):
        return self.price * self.quantity
    
    def __str__(self):
        return f'{self.name} - Harga: {self.price}, Stok: {self.quantity}, Nilai Total: {self.calculate_total_value()}'
    
class Store:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)

    def display_inventory(self):
        if not self.inventory:
            print("Inventaris kosong.")
            return
        print('Daftar Inventaris:')
        for i, product in enumerate(self.inventory, start=1):
            print(f'{i}. {product}')

    def remove_product(self, name):
        for i in self.inventory:
            if i.name == name:
                self.inventory.remove(i)
                print(f'Produk "{name}" telah dihapus dari inventaris.')
                return
        print(f'Produk "{name}" tidak ditemukan di inventaris.')

    def calculate_total_inventory_value(self):
        total_value = sum(product.calculate_total_value() for product in self.inventory)
        print(f'Total nilai inventaris: {total_value}')

# Pengujian
store = Store()

product1 = Product("Laptop", 1000, 10)
product2 = Product("Smartphone", 800, 20)
product3 = Product("Tablet", 600, 15)

store.add_product(product1)
store.add_product(product2)
store.add_product(product3)

print("Daftar Inventaris Setelah Penambahan:")
store.display_inventory()

# Perbarui stok produk
product1.update_quantity(5)
product2.update_quantity(-3)

print("\nDaftar Inventaris Setelah Pembaruan Stok:")
store.display_inventory()

print("\nTotal Nilai Inventaris:")
store.calculate_total_inventory_value()

# Hapus produk
print("\nHapus Produk:")
store.remove_product("Tablet")
store.display_inventory()
