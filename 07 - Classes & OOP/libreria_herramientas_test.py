import unittest
import libreria_herramientas as h

class Prueba_Errores(unittest.TestCase):
    def test_crear_objeto2(self):
        param = [1,2,2,5]
        h1 = h.herramientas(param)
        self.assertEqual(h1.lista, param)
    def objeto_incorrecto(self):
        self.assertRaises(ValueError, h.herramientas,'2')