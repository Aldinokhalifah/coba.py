def findMaxSum(arr, k) :
    if len(arr) == 0 : return 0
    if len(arr) < k: return 0

    max_sum = sum(arr[:k])
    window_sum = max_sum
    
    for i in range(k, len(arr)) :
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

print(findMaxSum([2, 1, 5, 1, 3, 2], 3))