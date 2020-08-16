my_list = [1, 2, 3]

print(my_list[0])
print(my_list[1::2])

my_list.append(4)
print(my_list)

my_list[0] = 'a'
print(my_list)

print(my_list.pop())
print(my_list)

for element in my_list:
    print(element)

a = [1, 2, 3]
b = a
print(a)
print(b)
print(id(a), id(b))
print(a is b)

"""El problema de hacer esto es que se igualan las listas"""
c = [a, b]
print(c)

a.append(5)
print(c)
