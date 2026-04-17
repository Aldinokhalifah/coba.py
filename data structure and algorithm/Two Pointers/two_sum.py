def two_sum(number, target) :
    left = 0
    right = len(number) - 1

    while left < right :
        sum = number[left] + number[right]

        if sum == target :
            return [left + 1, right + 1]
        elif sum < target :
            left += 1
        else :
            right -= 1
    return [-1, -1]

print(two_sum([2, 7, 11, 15], 9))