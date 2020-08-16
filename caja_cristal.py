import unittest

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False


class PruebaDeCristalTest(unittest.TestCase):

    def test_es_mayor_de_edad(self):
        resultado = es_mayor_de_edad(20)

        self.assertTrue(resultado)

    def test_es_menor_de_edad(self):
        resultado = es_mayor_de_edad(15)

        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()