a=[1,2,3]
b=list(a)
c=a
print(a, id(a))
print(b, id(b))
print(c, id(c))
c[0] = 0

print(a, c)