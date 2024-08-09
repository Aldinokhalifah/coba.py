list1 = ["A", "B", "C"]
list2 = [1, 2, 3]

combinations = [f"{letter}{number}" for letter in list1 for number in list2]

print(combinations)
