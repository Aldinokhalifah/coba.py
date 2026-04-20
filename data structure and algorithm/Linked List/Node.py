class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

# 1. Buat 3 Node terpisah
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# 2. Sambungkan! (Manual Linking)
node1.next = node2
node2.next = node3

current = node1

# 3. Menelusuri Linked List (Traversal)
while current != None :
    print(f"{current.data} ->", end=" ")
    current = current.next

print("null")