def faktorial(n):
    # 1. Base case
    if n == 0 or n == 1:
        return 1
    # 2. Recursive case
    else:
        return n * faktorial(n - 1)

# Pemanggilan fungsi
print(faktorial(5))  # Output: 120