my_dict = {
    'David': 35,
    'Erika': 20,
    'Jaime': 10
}

print(my_dict)
print(my_dict['David'])
"""Si no existe el valor, devuelve default"""
print(my_dict.get('Erik', 22))
print(my_dict.get('Jaime', 22))

my_dict['Jaime'] = 100
my_dict['Pedro'] = 80
print(my_dict)

"""Borramos elemento"""
del my_dict['Jaime']
print(my_dict)

for llave in my_dict.keys():
    print (llave)

for llave, value in my_dict.items():
    print (f'la llave es {llave} y su valor es {value}')

print('David' in my_dict)
print('Pako' in my_dict)
