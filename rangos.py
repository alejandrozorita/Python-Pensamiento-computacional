""" range(comienzo, fin, pasos) """

my_range = range(1,5)

print(type(my_range))

for i in my_range:
    print(i)

my_range_2 = range(0, 7, 2)
my_range_3 = range(0, 8, 2)

print(my_range_2 == my_range_3)
for i in my_range_2:
    print(i)
print('-------')
for i in my_range_3:
    print(i)

print(id(my_range_2))
print(id(my_range_3))
print(my_range_2 is my_range_3)

for i in range(0,101,2):
    print(i)