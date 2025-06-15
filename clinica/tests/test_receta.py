import unittest
from datetime import datetime
from modelo.receta import Receta
from modelo.paciente import Paciente
from modelo.medico import Medico

class TestReceta(unittest.TestCase):

    def setUp(self):
        # Pacientes
        self.paciente1 = Paciente("Lucía Gómez", "98765432", "15/03/1985")
        self.paciente2 = Paciente("Carlos Díaz", "45678901", "10/10/1975")
        self.paciente3 = Paciente("Valeria Suárez", "12312312", "22/07/1990")

        # Médicos
        self.medico1 = Medico("Dr. Roberto Pérez", "AB1234")
        self.medico2 = Medico("Dra. Mariana Torres", "CD5678")
        self.medico3 = Medico("Dr. Andrés López", "EF9012")

        # Medicamentos
        self.medicamentos1 = ["Ibuprofeno 600mg", "Paracetamol 500mg"]
        self.medicamentos2 = ["Amoxicilina 875mg", "Clonazepam 0.5mg"]
        self.medicamentos3 = ["Omeprazol 20mg"]

    def test_receta_valida_paciente1_medico1(self):
        receta = Receta(self.paciente1, self.medico1, self.medicamentos1)
        self.assertIsInstance(receta, Receta)
        self.assertIn("Ibuprofeno", str(receta))

    def test_receta_valida_paciente2_medico2(self):
        receta = Receta(self.paciente2, self.medico2, self.medicamentos2)
        self.assertIn("Clonazepam", str(receta))
        self.assertIn("Carlos", str(receta))
        self.assertIn("Mariana", str(receta))

    def test_receta_valida_paciente3_medico3(self):
        receta = Receta(self.paciente3, self.medico3, self.medicamentos3)
        self.assertIn("Omeprazol", str(receta))
        self.assertIn("Valeria", str(receta))
        self.assertIn("Andrés", str(receta))

    def test_error_paciente_invalido(self):
        with self.assertRaises(TypeError):
            Receta(None, self.medico1, self.medicamentos1)

    def test_error_medico_invalido(self):
        with self.assertRaises(TypeError):
            Receta(self.paciente1, None, self.medicamentos1)

    def test_error_medicamentos_vacios(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente1, self.medico1, [])

    def test_error_medicamentos_invalidos(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente1, self.medico1, ["", 123, None])

    def test_error_lista_no_es_lista(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente2, self.medico2, "Paracetamol")

if __name__ == "__main__":
    unittest.main()
