def funcion1(un_arg, una_funcion):
    def funcion2(otro_arg):
        return otro_arg * 2

    valor = funcion2(un_arg)
    return una_funcion

un_arg = 1

def cualquier_funcion(cualquier_arg):
    return cualquier_arg + 5


funcion1(un_arg, cualquier_funcion)