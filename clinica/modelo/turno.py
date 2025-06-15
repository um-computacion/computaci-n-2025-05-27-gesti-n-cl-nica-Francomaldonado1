from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico

class Turno:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
     if not isinstance(paciente, Paciente):
        raise TypeError("El dato del paciente ingresado no es válido. Por favor, verifique la información.")
     if not isinstance(medico, Medico):
        raise TypeError("El dato del médico ingresado no es válido. Por favor, verifique la información.")
     if not isinstance(fecha_hora, datetime):
        raise TypeError("La fecha y hora del turno no son correctas. Asegúrese de ingresar una fecha y hora válidas.")
     if not isinstance(especialidad, str) or not especialidad.strip():
        raise ValueError("La especialidad del turno es obligatoria y debe estar correctamente escrita.")
    
     especialidades_medico = [esp.obtener_especialidad().lower() for esp in medico.obtener_especialidades()]
     if especialidad.lower() not in especialidades_medico:
        raise ValueError("La especialidad no coincide con las especialidades del médico.")
    
     self.__paciente = paciente
     self.__medico = medico
     self.__fecha_hora = fecha_hora
     self.__especialidad = especialidad



    def obtener_medico(self) -> Medico:
        return self.__medico

    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora

    def __str__(self) -> str:
        return (f"Turno para {self.__paciente} con el Dr. {self.__medico} "
                f"en la especialidad {self.__especialidad} el {self.__fecha_hora.strftime('%d/%m/%Y %H:%M')}")
