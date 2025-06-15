from datetime import datetime
from modelo.excepciones import FechaInvalidaException, DatoInvalidoException

class Paciente:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        if not nombre or nombre.strip() == "":
            raise DatoInvalidoException("El nombre no puede estar vacío.")
        if not dni or dni.strip() == "":
            raise DatoInvalidoException("El DNI no puede estar vacío.")

        self.__nombre = nombre
        self.__dni = dni
        self.__fecha_nacimiento = fecha_nacimiento

    def obtener_nombre(self):
        return self.__nombre

    def obtener_dni(self):
        return self.__dni

    def obtener_fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    """ def __validar_fecha(self, fecha: str) -> str:
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            return fecha
        except ValueError:
            raise FechaInvalidaException()
            Lo dejo por las dudas de que necesitemos usarlo en un futuro a esta validacion interna."""

    def __str__(self):
        return f"Paciente: {self.__nombre} - DNI: {self.__dni} - Fecha de nacimiento: {self.__fecha_nacimiento}"


  
