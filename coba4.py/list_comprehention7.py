celsius = [x for x in range(0, 101, 10)]

Fahrenheit = []

for i in celsius:
    F = (i * 9/5) + 32
    Fahrenheit.append(F)

print(Fahrenheit)