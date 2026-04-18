def findSmallestSum(arr, s) :
    window_start = 0
    window_sum = 0
    min_length = float('inf')
    
    for window_end in range(len(arr)) :
        window_sum += arr[window_end]
        
        while window_sum >= s :
            current_window_size = window_end - window_start + 1
            
            min_length = min(min_length, current_window_size)
            
            window_sum -= arr[window_start]
            window_start += 1
    return min_length if min_length != float('inf') else 0

print(findSmallestSum([2, 1, 5, 2, 8], 7))