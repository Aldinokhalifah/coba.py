def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

bilangan_prima = [i for i in range(1, 101) if is_prime(i)]
print(bilangan_prima)