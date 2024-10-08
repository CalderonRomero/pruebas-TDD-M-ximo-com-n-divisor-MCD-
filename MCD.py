import unittest

#Función que calcula el MCD de dos números
def mcd_dos_numeros(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

#Función que calcula el MCD de cuatro números
def mcd_cuatro_numeros(n1, n2, n3, n4):
    return mcd_dos_numeros(mcd_dos_numeros(n1, n2), mcd_dos_numeros(n3, n4))

#Clase de pruebas unitarias
class TestMCD(unittest.TestCase):
    def test_mcd_dos_numeros(self):
        # Pruebas de MCD de dos números
        self.assertEqual(mcd_dos_numeros(8, 12), 4)
        self.assertEqual(mcd_dos_numeros(15, 5), 5)
        self.assertEqual(mcd_dos_numeros(7, 13), 1)
        self.assertEqual(mcd_dos_numeros(9, 6), 3)

    def test_mcd_cuatro_numeros(self):
        # Pruebas de MCD de cuatro números
        self.assertEqual(mcd_cuatro_numeros(8, 12, 16, 32), 4)
        self.assertEqual(mcd_cuatro_numeros(9, 27, 81, 3), 3)
        self.assertEqual(mcd_cuatro_numeros(5, 10, 15, 20), 5)
        self.assertEqual(mcd_cuatro_numeros(18, 24, 36, 48), 6)

if __name__ == "__main__":
    unittest.main()
