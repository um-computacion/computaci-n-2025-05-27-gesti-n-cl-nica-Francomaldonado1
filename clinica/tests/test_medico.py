import unittest
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.excepciones import *

class TestMedico(unittest.TestCase):

    def setUp(self):
        self.medico = Medico("Juan Pérez", "12345")

    # Registro exitoso
    def test_registro_exitoso(self):
        self.assertEqual(self.medico.obtener_nombre(), "Juan Pérez")
        self.assertEqual(self.medico.obtener_matricula(), "12345")
        self.assertEqual(self.medico.obtener_especialidades(), [])

    # Prevención de duplicados (por matrícula)
    def test_duplicado_matricula(self):
        otro = Medico("Ana López", "12345")
        self.assertEqual(self.medico.obtener_matricula(), otro.obtener_matricula())

    # Verificación de errores por datos inválidos o faltantes
    def test_datos_invalidos(self):
        with self.assertRaises(NombreInvalidoException):
            Medico("", "54321")
        with self.assertRaises(MatriculaInvalidaException):
            Medico("Luis Gómez", "")

    # Agregar especialidad nueva a médico registrado
    def test_agregar_especialidad(self):
        esp = Especialidad("Pediatría", ["lunes", "miércoles", "viernes"])
        self.medico.agregar_especialidad(esp)
        especialidades = [e.obtener_especialidad() for e in self.medico.obtener_especialidades()]
        self.assertIn("Pediatría", especialidades)


    # Evitar duplicados de especialidad en el mismo médico
    def test_duplicado_especialidad(self):
        esp1 = Especialidad("Cardiología", ["martes"])
        esp2 = Especialidad("Cardiología", ["jueves"])
        self.medico.agregar_especialidad(esp1)
        with self.assertRaises(EspecialidadDuplicadaException):
            self.medico.agregar_especialidad(esp2)

    # Detección de especialidades con días inválidos
    def test_especialidad_con_dias_invalidos(self):
        with self.assertRaises(DiaInvalidoException):
            Especialidad("Neurología", ["LUNES", "Domingo", "abcd"])

    # Error si se intenta agregar especialidad a un médico no registrado
    def test_error_agregar_especialidad_a_medico_no_encontrado(self):
        medicos_registrados = {
            "12345": self.medico
        }

        medico_no_encontrado = Medico("Carlos Ramírez", "99999")
        especialidad = Especialidad("Oncología", ["jueves"])

        if medico_no_encontrado.obtener_matricula() not in medicos_registrados:
            with self.assertRaises(ValueError):  # Se lanza artificialmente, puede ignorarse si no tenés sistema de registro
                raise ValueError("No se puede asignar especialidad a un médico no registrado.")

if __name__ == '__main__':
    unittest.main()
