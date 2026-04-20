def twoSum(nums, target):
    seen = {}
    
    for i, item in enumerate(nums) :
        need = target - item
        if need in seen :
            return [seen[need] , i]
        seen[item] = i
    return []

print(twoSum([2, 7, 11, 15], 18))