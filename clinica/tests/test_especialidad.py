import unittest
from modelo.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):

    def setUp(self):
        self.esp = Especialidad("Pediatría", ["lunes", "miércoles", "viernes"])

    def test_obtener_especialidad(self):
        self.assertEqual(self.esp.obtener_especialidad(), "Pediatría")

    def test_verificar_dia_valido_minuscula(self):
        self.assertTrue(self.esp.verificar_dia("lunes"))
        self.assertTrue(self.esp.verificar_dia("viernes"))

    def test_verificar_dia_valido_mayuscula(self):
        self.assertTrue(self.esp.verificar_dia("Miércoles")) 

    def test_verificar_dia_invalido(self):
        self.assertFalse(self.esp.verificar_dia("domingo"))
        self.assertFalse(self.esp.verificar_dia(""))

    def test_str_representacion(self):
        esp = Especialidad("Pediatría", ["lunes", "miércoles", "viernes"])
        expected = "Especialidad: Pediatría | Días de atención: Lunes, miércoles, viernes"
        self.assertEqual(str(esp), expected)


    def test_dias_son_convertidos_a_minuscula(self):
        esp2 = Especialidad("Cardiología", ["Lunes", "MARTES", "MiérCoLeS"])
        self.assertTrue(esp2.verificar_dia("lunes"))
        self.assertTrue(esp2.verificar_dia("martes"))
        self.assertTrue(esp2.verificar_dia("miércoles"))

if __name__ == "__main__":
    unittest.main()
