def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, f'No puede estar vacío'

        primeras_letras.append(palabra[0])

    return primeras_letras

print(primera_letra(['', 'tt']))