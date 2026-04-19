def min_subarray_len(s, nums):
    window_start = 0
    current_sum = 0
    min_length = float('inf')
    
    for window_end in range(len(nums)) :
        current_sum += nums[window_end]
        
        while current_sum >= s :
            current_window_size = window_end - window_start + 1
            
            min_length = min(min_length, current_window_size)
            
            current_sum -= nums[window_start]
            window_start += 1
    return min_length

print(min_subarray_len(8, [2, 3, 1, 2, 4, 3]))