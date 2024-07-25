a = 9 
b = 5

# bitwise OR (|)
c = a | b
print('========OR========')
print(f"nilai : {a} binary : {format(a, '08b')}")
print(f"nilai : {b} binary : {format(b, '08b')}")
print('-------------------------------')
print(f"nilai : {c} binary : {format(c, '08b')}")

# bitwise AND (&)
c = a & b
print('========AND========')
print(f"nilai : {a} binary : {format(a, '08b')}")
print(f"nilai : {b} binary : {format(b, '08b')}")
print('-------------------------------')
print(f"nilai : {c} binary : {format(c, '08b')}")

# shifting

# shifting right (>>)
c = a >> 2
print('========>>========')
print(f"nilai : {a} binary : {format(a, '08b')}")
print('-------------------------------')
print(f"nilai : {c} binary : {format(c, '08b')}")


# shifting right (<<)
c = a << 4
print('========<<========')
print(f"nilai : {a} binary : {format(a, '08b')}")
print('-------------------------------')
print(f"nilai : {c} binary : {format(c, '08b')}")