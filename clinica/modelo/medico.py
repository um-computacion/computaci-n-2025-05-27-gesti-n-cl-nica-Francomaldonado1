from modelo.excepciones import (
    NombreInvalidoException,
    MatriculaInvalidaException,
    DiaInvalidoException,
    EspecialidadDuplicadaException
)
from modelo.especialidad import Especialidad

class Medico:
    def __init__(self, nombre: str, matricula: str, especialidades: list = None):
        if not nombre or not isinstance(nombre, str) or nombre.strip() == "":
            raise NombreInvalidoException()
        
        if len(nombre.strip().split()) < 2:
            raise NombreInvalidoException("Debe ingresar nombre completo (nombre y apellido).")

        # Normaliza el nombre: capitaliza cada palabra
        nombre = " ".join(palabra.capitalize() for palabra in nombre.strip().split())

        if not matricula or not isinstance(matricula, str) or matricula.strip() == "":
            raise MatriculaInvalidaException()

        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades = especialidades if especialidades else []

    def agregar_especialidad(self, especialidad):
        dias_validos = {"lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"}
        
        # Mapeo alternativo para aceptar sin tilde
        equivalencias = {
            "miercoles": "miércoles",
            "sabado": "sábado"
        }

        dias_normalizados = []
        for dia in especialidad.dias:
            dia = dia.strip().lower()
            dia = equivalencias.get(dia, dia)  # corrige si estaba sin tilde
            if dia not in dias_validos:
                raise DiaInvalidoException("Algunos días ingresados no son válidos. Use días como 'lunes', 'martes', etc.")
            dias_normalizados.append(dia)

        for esp in self.__especialidades:
            if esp.nombre.lower() == especialidad.nombre.lower():
                raise EspecialidadDuplicadaException()

        self.__especialidades.append(especialidad)


    def obtener_especialidades(self) -> list[Especialidad]:
        return self.__especialidades

    def obtener_matricula(self) -> str:
        return self.__matricula

    def obtener_nombre(self) -> str:
        return self.__nombre

    def obtener_especialidad_para_dia(self, dia: str) -> str | None:
        for especialidad in self.__especialidades:
            if dia.lower() in [d.lower() for d in especialidad.dias]:
                return especialidad.nombre
        return None

    def __str__(self) -> str:
        especialidades_str = ", ".join([
            f"{e.nombre} ({'/'.join(e.dias)})"
            for e in self.__especialidades
        ])
        return f"Médico: {self.__nombre} - Matrícula: {self.__matricula} - Especialidades: {especialidades_str}"

