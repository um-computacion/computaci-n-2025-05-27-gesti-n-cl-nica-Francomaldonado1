import unittest
from datetime import datetime
from modelo.turno import Turno
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad

class TestAgendamientoTurnos(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Juan Pérez", "12345678", "02/02/2000")
        self.medico = Medico("Ana García", "12345")
        self.fecha_hora = datetime(2025, 6, 10, 10, 0)  # Martes

        # Crear y asignar especialidad válida al médico
        self.especialidad = "Cardiología"
        especialidad_obj = Especialidad(self.especialidad, ["martes", "jueves"])
        self.medico.agregar_especialidad(especialidad_obj)

    def test_agendamiento_correcto(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora, self.especialidad)
        self.assertEqual(turno.obtener_medico(), self.medico)
        self.assertEqual(turno.obtener_fecha_hora(), self.fecha_hora)

        # Confirmar que aparecen partes del string esperado
        str_turno = str(turno)
        self.assertIn("Paciente: Juan", str_turno)
        self.assertIn("DNI: 12345678", str_turno)
        self.assertIn("Dr. Médico: Ana", str_turno)
        self.assertIn("Matrícula: 12345", str_turno)
        self.assertIn("especialidad Cardiología", str_turno)

    def test_error_especialidad_incorrecta(self):
        # Esta especialidad no fue asignada al médico
        with self.assertRaises(ValueError):
            Turno(self.paciente, self.medico, self.fecha_hora, "Pediatría")

    def test_error_paciente_no_existente(self):
        with self.assertRaises(TypeError):
            Turno(None, self.medico, self.fecha_hora, self.especialidad)

    def test_error_medico_no_existente(self):
        with self.assertRaises(TypeError):
            Turno(self.paciente, None, self.fecha_hora, self.especialidad)

if __name__ == "__main__":
    unittest.main()
