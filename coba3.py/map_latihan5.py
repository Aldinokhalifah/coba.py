import math

numbers = [1, 2, 3, 4, 5]

fact = list(map(lambda x : math.factorial(x), numbers))
print(fact)