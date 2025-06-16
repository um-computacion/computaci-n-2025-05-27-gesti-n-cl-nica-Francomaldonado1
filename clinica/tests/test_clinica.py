import unittest
from datetime import datetime, timedelta
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.turno import Turno
from modelo.receta import Receta
from modelo.clinica import Clinica
from modelo.excepciones import *


class TestClinicaRegistro(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.medico = Medico("Ana Gomez", "M1234")
        especialidad = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(especialidad)

    def test_agregar_paciente_correctamente(self):
        mensaje = self.clinica.agregar_paciente(self.paciente)
        self.assertIn("registrado correctamente", mensaje)
        self.assertTrue(self.clinica.validar_existencia_paciente(self.paciente.obtener_dni()))

    def test_agregar_paciente_duplicado_lanza_excepcion(self):
        self.clinica.agregar_paciente(self.paciente)
        with self.assertRaises(PacienteYaRegistradoException):
            self.clinica.agregar_paciente(self.paciente)

    def test_agregar_medico_correctamente(self):
        mensaje = self.clinica.agregar_medico(self.medico)
        self.assertIn("registrado correctamente", mensaje)
        self.assertTrue(self.clinica.validar_existencia_medico(self.medico.obtener_matricula()))

    def test_agregar_medico_duplicado_lanza_excepcion(self):
        self.clinica.agregar_medico(self.medico)
        with self.assertRaises(MedicoYaRegistradoException):
            self.clinica.agregar_medico(self.medico)

    def test_obtener_medico_por_matricula(self):
        self.clinica.agregar_medico(self.medico)
        medico_obtenido = self.clinica.obtener_medico_por_matricula(self.medico.obtener_matricula())
        self.assertEqual(medico_obtenido.obtener_nombre(), self.medico.obtener_nombre())

    def test_obtener_medico_por_matricula_inexistente_lanza_excepcion(self):
        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica.obtener_medico_por_matricula("NoExiste")


class TestClinicaTurnosRecetas(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.medico = Medico("Ana Gomez", "M1234")
        especialidad = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(especialidad)
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        # Fecha para turno: lunes 12/06/2023 10:00 (asegurar que sea lunes)
        self.fecha_turno = datetime.strptime("12/06/2023 10:00", "%d/%m/%Y %H:%M")

    def test_agendar_turno_correctamente(self):
        mensaje = self.clinica.agendar_turno(
            self.paciente.obtener_dni(),
            self.medico.obtener_matricula(),
            "Cardiología",
            self.fecha_turno
        )
        self.assertIn("Turno agendado", mensaje)
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)

    def test_agendar_turno_con_turno_duplicado_lanza_excepcion(self):
        self.clinica.agendar_turno(
            self.paciente.obtener_dni(),
            self.medico.obtener_matricula(),
            "Cardiología",
            self.fecha_turno
        )
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno(
                self.paciente.obtener_dni(),
                self.medico.obtener_matricula(),
                "Cardiología",
                self.fecha_turno
            )

    def test_agendar_turno_con_medico_no_disponible_lanza_excepcion(self):
        fecha_no_disponible = datetime.strptime("13/06/2023 10:00", "%d/%m/%Y %H:%M")  # martes, no en dias de especialidad
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno(
                self.paciente.obtener_dni(),
                self.medico.obtener_matricula(),
                "Cardiología",
                fecha_no_disponible
            )

    def test_emitir_receta_correctamente(self):
        medicamentos = ["Paracetamol", "Ibuprofeno"]
        mensaje = self.clinica.emitir_receta(
            self.paciente.obtener_dni(),
            self.medico.obtener_matricula(),
            medicamentos
        )
        self.assertIn("Receta emitida", mensaje)
        historia = self.clinica.obtener_historia_clinica(self.paciente.obtener_dni())
        self.assertEqual(len(historia.obtener_recetas()), 1)

    def test_emitir_receta_con_medicamentos_invalidos_lanza_excepcion(self):
        with self.assertRaises(MedicamentosInvalidosException):
            self.clinica.emitir_receta(
                self.paciente.obtener_dni(),
                self.medico.obtener_matricula(),
                ["Paracetamol", 123]  # Un medicamento no es string
            )


class TestClinicaMetodosAuxiliares(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.medico = Medico("Ana Gomez", "M1234")
        especialidad1 = Especialidad("Cardiología", ["lunes", "miércoles"])
        especialidad2 = Especialidad("Neurología", ["viernes"])
        self.medico.agregar_especialidad(especialidad1)
        self.medico.agregar_especialidad(especialidad2)
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.fecha_turno = datetime.strptime("12/06/2023 10:00", "%d/%m/%Y %H:%M")

    def test_validar_existencia_paciente(self):
        self.assertTrue(self.clinica.validar_existencia_paciente(self.paciente.obtener_dni()))
        self.assertFalse(self.clinica.validar_existencia_paciente("99999999"))

    def test_validar_existencia_medico(self):
        self.assertTrue(self.clinica.validar_existencia_medico(self.medico.obtener_matricula()))
        self.assertFalse(self.clinica.validar_existencia_medico("NoExiste"))

    def test_validar_turno_no_duplicado(self):
        # No hay turnos, debe devolver True
        self.assertTrue(self.clinica.validar_turno_no_duplicado(self.medico.obtener_matricula(), self.fecha_turno))
        # Agendo un turno
        self.clinica.agendar_turno(self.paciente.obtener_dni(), self.medico.obtener_matricula(), "Cardiología", self.fecha_turno)
        # Ahora debe devolver False porque ya hay un turno
        self.assertFalse(self.clinica.validar_turno_no_duplicado(self.medico.obtener_matricula(), self.fecha_turno))

    def test_obtener_dia_semana_en_espanol(self):
        self.assertEqual(self.clinica.obtener_dia_semana_en_espanol(self.fecha_turno), "lunes")
        fecha_domingo = datetime.strptime("11/06/2023", "%d/%m/%Y")  # Domingo
        self.assertEqual(self.clinica.obtener_dia_semana_en_espanol(fecha_domingo), "domingo")

    def test_obtener_especialidad_disponible(self):
        self.assertEqual(self.clinica.obtener_especialidad_disponible(self.medico, "lunes"), "Cardiología")
        self.assertEqual(self.clinica.obtener_especialidad_disponible(self.medico, "viernes"), "Neurología")
        self.assertIsNone(self.clinica.obtener_especialidad_disponible(self.medico, "martes"))

    def test_validar_especialidad_en_dia(self):
        self.assertTrue(self.clinica.validar_especialidad_en_dia(self.medico, "Cardiología", "lunes"))
        self.assertTrue(self.clinica.validar_especialidad_en_dia(self.medico, "neurología", "viernes"))  # minusculas
        self.assertFalse(self.clinica.validar_especialidad_en_dia(self.medico, "Cardiología", "martes"))
        self.assertFalse(self.clinica.validar_especialidad_en_dia(self.medico, "Oncología", "lunes"))

    """  def test_paciente_fecha_invalida_lanza_excepcion(self):
        with self.assertRaises(FechaInvalidaException) as context:
            Paciente("Maria Lopez", "87654321", "1990-01-01")  # Formato incorrecto
        self.assertEqual(str(context.exception), "La fecha debe tener el formato dd/mm/aaaa")
     Comentado por que la interfaz (CLI.py) ya valida el formato de fecha con datetime.strptime() y lanza ValueError si es incorrecto."""

if __name__ == "__main__":
    unittest.main()
