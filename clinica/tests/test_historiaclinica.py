import unittest
from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.turno import Turno
from modelo.receta import Receta
from modelo.historiaclinica import HistoriaClinica

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
       # Pacientes
       self.paciente1 = Paciente("Juan Pérez", "12345678", "01/01/1980")
       self.paciente2 = Paciente("María Gómez", "87654321", "15/05/1990")

       # Médicos 
       self.medico1 = Medico("Dr. González", "12345")
       self.medico2 = Medico("Dra. Suárez", "78901")

       # Especialidades y días
       self.especialidad1 = Especialidad("Cardiología", ["martes", "jueves"])
       self.especialidad2 = Especialidad("Pediatría", ["lunes", "miércoles", "viernes"])

       self.medico1.agregar_especialidad(self.especialidad1)
       self.medico2.agregar_especialidad(self.especialidad2)

       # Turnos
       self.turno1 = Turno(self.paciente1, self.medico1, datetime(2025, 6, 10, 10, 0), "Cardiología")
       self.turno2 = Turno(self.paciente1, self.medico1, datetime(2025, 6, 12, 9, 0), "Cardiología")
       self.turno3 = Turno(self.paciente2, self.medico2, datetime(2025, 6, 11, 11, 0), "Pediatría")

       # Recetas
       self.receta1 = Receta(self.paciente1, self.medico1, ["Ibuprofeno", "Aspirina", "Enalapril"])
       self.receta2 = Receta(self.paciente1, self.medico1, ["Paracetamol"])
       self.receta3 = Receta(self.paciente2, self.medico2, ["Amoxicilina"])

       self.historia1 = HistoriaClinica(self.paciente1)
       self.historia2 = HistoriaClinica(self.paciente2)



    def test_agregar_turnos_y_recetas_paciente1(self):
       self.historia1.agregar_turno(self.turno1)
       self.historia1.agregar_turno(self.turno2)
       self.historia1.agregar_receta(self.receta1)
       self.historia1.agregar_receta(self.receta2)

       turnos = self.historia1.obtener_turnos()
       recetas = self.historia1.obtener_recetas()

       self.assertEqual(len(turnos), 2)
       self.assertEqual(turnos[0], self.turno1)
       self.assertEqual(turnos[1], self.turno2)

       self.assertEqual(len(recetas), 2)
       self.assertEqual(recetas[0], self.receta1)
       self.assertEqual(recetas[1], self.receta2)

    def test_agregar_turnos_y_recetas_paciente2(self):
       self.historia2.agregar_turno(self.turno3)
       self.historia2.agregar_receta(self.receta3)

       turnos = self.historia2.obtener_turnos()
       recetas = self.historia2.obtener_recetas()

       self.assertEqual(len(turnos), 1)
       self.assertEqual(turnos[0], self.turno3)

       self.assertEqual(len(recetas), 1)
       self.assertEqual(recetas[0], self.receta3)

    def test_representacion_historia_clinica(self):
       self.historia1.agregar_turno(self.turno1)
       self.historia1.agregar_receta(self.receta1)

       texto = str(self.historia1)
       self.assertIn("Historial médico de", texto)
       self.assertIn("Turnos agendados:", texto)
       self.assertIn("Recetas médicas:", texto)
       self.assertIn("Ibuprofeno", texto)
       self.assertIn("Cardiología", texto)

if __name__ == "__main__":
    unittest.main()
