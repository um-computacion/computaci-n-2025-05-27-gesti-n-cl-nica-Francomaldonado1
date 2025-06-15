from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.historiaclinica import HistoriaClinica
from modelo.turno import Turno
from modelo.receta import Receta
from modelo.excepciones import *
import calendar

class Clinica:
    def __init__(self):
        self.__pacientes = {}
        self.__medicos = {}
        self.__turnos = []
        self.__historias_clinicas = {}


    # Métodos de Registro y Acceso


    def agregar_paciente(self, paciente: Paciente) -> str:
        if not isinstance(paciente, Paciente):
            raise PacienteNoEncontradoException("Debe ingresar un paciente válido.")
        dni = paciente.obtener_dni()
        if dni in self.__pacientes:
            raise PacienteYaRegistradoException(f"El paciente con DNI {dni} ya está registrado.")
        self.__pacientes[dni] = paciente
        self.__historias_clinicas[dni] = HistoriaClinica(paciente)
        return f"Paciente con DNI {dni} registrado correctamente."

    def agregar_medico(self, medico: Medico) -> str:
        if not isinstance(medico, Medico):
            raise TypeError("Debe ingresar un médico válido.")
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos:
            raise MedicoYaRegistradoException(f"El médico con matrícula {matricula} ya está registrado.")
        self.__medicos[matricula] = medico
        return f"Médico con matrícula {matricula} registrado correctamente."

    def obtener_pacientes(self) -> list[Paciente]:
        """Devuelve la lista de todos los pacientes registrados."""
        return list(self.__pacientes.values())

    def obtener_medicos(self) -> list[Medico]:
        """Devuelve la lista de todos los médicos registrados."""
        return list(self.__medicos.values())

    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
        """Busca y devuelve un médico por su matrícula."""
        if matricula not in self.__medicos:
            raise MedicoNoEncontradoException(f"No se encontró un médico con la matrícula {matricula}.")
        return self.__medicos[matricula]
 

    # Métodos de Turnos

    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime) -> str:
        if dni not in self.__pacientes:
           raise PacienteNoEncontradoException(f"No se encontró un paciente con DNI {dni}.")
        if matricula not in self.__medicos:
           raise MedicoNoEncontradoException(f"No se encontró un médico con matrícula {matricula}.")

        medico = self.__medicos[matricula]
        paciente = self.__pacientes[dni]

        if not self.validar_turno_no_duplicado(matricula, fecha_hora):
          raise TurnoOcupadoException(f"Ya existe un turno para el médico con matrícula {matricula} en esa fecha y hora.")

        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)

        if not self.validar_especialidad_en_dia(medico, especialidad, dia_semana):
          raise MedicoNoDisponibleException(f"El médico con matrícula {matricula} no atiende {especialidad} los días {dia_semana}.")

        try:
          nuevo_turno = Turno(paciente, medico, fecha_hora, especialidad)
        except ValueError as e:
          raise EspecialidadInvalidaException(str(e))

        self.__turnos.append(nuevo_turno)
        self.__historias_clinicas[dni].agregar_turno(nuevo_turno)

        return f"Turno agendado para {paciente.obtener_nombre()} con el médico {medico.obtener_nombre()} el {fecha_hora.strftime('%d/%m/%Y %H:%M')}."


    def obtener_turnos(self) -> list[Turno]:
        """Devuelve la lista de todos los turnos agendados."""
        return self.__turnos.copy()
 

    # Métodos de Recetas e Historia Clínica


    def emitir_receta(self, dni: str, matricula: str, medicamentos: list[str]) -> str:
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException(f"No se encontró un paciente con DNI {dni}.")
        if matricula not in self.__medicos:
            raise MedicoNoEncontradoException(f"No se encontró un médico con matrícula {matricula}.")

        if not medicamentos or not all(isinstance(med, str) for med in medicamentos):
            raise MedicamentosInvalidosException()

        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]

        receta = Receta(paciente, medico, medicamentos)
        self.__historias_clinicas[dni].agregar_receta(receta)

        return f"Receta emitida para {paciente.obtener_nombre()} por el médico {medico.obtener_nombre()}."

    def obtener_historia_clinica(self, dni: str) -> HistoriaClinica:
        if dni not in self.__historias_clinicas:
            raise HistoriaClinicaNoEncontradaException(f"No se encontró historia clínica para el paciente con DNI {dni}.")
        return self.__historias_clinicas[dni]


    # Métodos de Validaciones y Utilidades


    def validar_existencia_paciente(self, dni: str) -> bool:
        return dni in self.__pacientes

    def validar_existencia_medico(self, matricula: str) -> bool:
        return matricula in self.__medicos

    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime) -> bool:
        for turno in self.__turnos:
            if (turno.obtener_medico().obtener_matricula() == matricula and
                turno.obtener_fecha_hora() == fecha_hora):
                return False
        return True

    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime) -> str:
        dias_semana = {
            "Monday": "lunes",
            "Tuesday": "martes",
            "Wednesday": "miércoles",
            "Thursday": "jueves",
            "Friday": "viernes",
            "Saturday": "sábado",
            "Sunday": "domingo"
        }
        dia_ingles = calendar.day_name[fecha_hora.weekday()]
        return dias_semana.get(dia_ingles, "día desconocido")

    def obtener_especialidad_disponible(self, medico: Medico, dia_semana: str) -> str | None:
        for especialidad in medico.obtener_especialidades():
            if dia_semana.lower() in (d.lower() for d in especialidad.obtener_dias()):
                return especialidad.obtener_especialidad()
        return None

    def validar_especialidad_en_dia(self, medico: Medico, especialidad_solicitada: str, dia_semana: str) -> bool:
        for especialidad in medico.obtener_especialidades():
          if (especialidad.obtener_especialidad().lower() == especialidad_solicitada.lower() and
              dia_semana.lower() in [d.lower() for d in especialidad.obtener_dias()]):
           return True
        return False

