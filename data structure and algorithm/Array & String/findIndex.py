def findIndex(arr, n):
    return arr.index(n) if n in arr else -1

print(findIndex([10, 20, 30, 40], 30))  # 2