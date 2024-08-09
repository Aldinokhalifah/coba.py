list = [[1, 2], [3, 4], [5, 6]]
list2 = [i for sublist in list for i in sublist]

print(list2)
