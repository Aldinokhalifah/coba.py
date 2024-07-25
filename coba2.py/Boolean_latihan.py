# NOT

print(' ===NOT===')
a = True
b = False
c = not a
d = not b

print("data c=",c)
print("data c=",d)

# OR(jika salh satu true, maka hasilnya true)

print(' ===OR===')

a = False
b= False
c = a or b
print(a,'OR',b,'=',c)

a = True
b= False
c = a or b
print(a,'OR',b,' =',c)

a = False
b= True
c = a or b
print(a,'OR',b,' =',c)

a = True
b= True
c = a or b
print(a,'OR',b,'  =',c)


# and(jika dua buah true, maka hasilnya true)

print(' ===AND===')

a = False
b= False
c = a and b
print(a,'AND',b,'=',c)

a = True
b= False
c = a and b
print(a,'AND',b,' =',c)

a = False
b= True
c = a and b
print(a,'AND',b,' =',c)

a = True
b= True
c = a and b
print(a,'AND',b,'  =',c)