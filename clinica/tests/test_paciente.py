import unittest
from modelo.paciente import Paciente
from modelo.excepciones import FechaInvalidaException, DatoInvalidoException

class TestPaciente(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Juan Perez", "123456789", "01/01/1980")
        self.paciente2 = Paciente("Pedro Lopez", "987654321", "02/02/1990")
        self.paciente3 = Paciente("Ana Puga", "234567890", "03/05/1983")
        self.paciente4 = Paciente("Carlos Ramirez", "876543210", "04/06/1984")
        self.paciente5 = Paciente("Luis Gomez", "345678901", "05/07/1985")

    def test_obtener_dni(self):
        self.assertEqual(self.paciente.obtener_dni(), "123456789")

    def test_representacion(self):
        expected = "Paciente: Juan Perez - DNI: 123456789 - Fecha de nacimiento: 01/01/1980"
        self.assertEqual(str(self.paciente), expected)

    def test_inicializacion_atributos(self):
        self.assertEqual(self.paciente._Paciente__nombre, "Juan Perez")
        self.assertEqual(self.paciente._Paciente__dni, "123456789")
        self.assertEqual(self.paciente._Paciente__fecha_nacimiento, "01/01/1980")

    """  def test_fecha_nacimiento_invalida(self):
        with self.assertRaises(FechaInvalidaException) as contexto:
            Paciente("Juan Pérez", "12345678", "1980/01/01")  # Formato incorrecto
        self.assertIn("formato dd/mm/aaaa", str(contexto.exception))
        Lo mismo con el test de clinica, ya queda verificado por el datetime.strptime() de la interfaz (CLI.py)"""

    def test_nombre_vacio_lanza_error(self):
        with self.assertRaises(DatoInvalidoException) as contexto:
            Paciente("", "12345678", "01/01/2000")
        self.assertIn("nombre no puede estar vacío", str(contexto.exception))

    def test_dni_vacio_lanza_error(self):
        with self.assertRaises(DatoInvalidoException) as contexto:
            Paciente("Juan Pérez", "", "01/01/2000")
        self.assertIn("DNI no puede estar vacío", str(contexto.exception))
if __name__ == '__main__':
    unittest.main()
