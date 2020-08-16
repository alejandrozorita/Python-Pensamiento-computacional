a = [1, 2, 3]
b = a
print(a)
print(b)
print(id(a), id(b))

c = list(a)
print(c)
print(id(c))

d = a[::]
print (d)
print(id(d))
