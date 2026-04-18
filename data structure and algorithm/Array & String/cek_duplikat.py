def findDuplicate(arr) :
    data = set()

    for i in arr :
        if i in data :
            return True
        else :
            data.add(i)
            
    return False

print(findDuplicate([1, 2, 3, 4]))