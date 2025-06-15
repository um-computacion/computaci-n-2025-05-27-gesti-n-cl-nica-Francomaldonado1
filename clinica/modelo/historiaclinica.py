from modelo.paciente import Paciente
from modelo.turno import Turno
from modelo.receta import Receta

class HistoriaClinica:
    def __init__(self, paciente: Paciente):
        if not isinstance(paciente, Paciente):
            raise TypeError("Debe proporcionar un paciente válido.")
        
        self.__paciente = paciente
        self.__turnos = []
        self.__recetas = []

    def agregar_turno(self, turno: Turno):
        if not isinstance(turno, Turno):
            raise TypeError("Debe proporcionar un turno válido.")
        self.__turnos.append(turno)

    def agregar_receta(self, receta: Receta):
        if not isinstance(receta, Receta):
            raise TypeError("Debe proporcionar una receta válida.")
        self.__recetas.append(receta)

    def obtener_turnos(self) -> list[Turno]:
        return self.__turnos.copy()

    def obtener_recetas(self) -> list[Receta]:
        return self.__recetas.copy()

    def __str__(self) -> str:
        historial = f"Historial médico de {self.__paciente}\n{'='*40}\n"
        historial += f"{self.__paciente}\n\n"

        historial += "Turnos agendados:\n"
        if self.__turnos:
         for i, turno in enumerate(self.__turnos, 1):
            historial += f"\n[{i}] {turno}"
        else:
            historial += "No hay turnos registrados.\n"

        historial += "\n\n Recetas médicas:\n"
        if self.__recetas:
         for i, receta in enumerate(self.__recetas, 1):
            historial += f"\n[{i}] {receta}\n"
        else:
            historial += "No hay recetas registradas.\n"

        return historial
