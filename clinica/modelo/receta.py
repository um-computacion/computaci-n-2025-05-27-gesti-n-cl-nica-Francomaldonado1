from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: list[str]):
        if not isinstance(paciente, Paciente):
            raise TypeError("Debe ingresar un paciente válido.")
        if not isinstance(medico, Medico):
            raise TypeError("Debe ingresar un médico válido.")
        if not isinstance(medicamentos, list) or not medicamentos or not all(isinstance(m, str) and m.strip() for m in medicamentos):
            raise ValueError("Debe ingresar al menos un medicamento con un nombre válido.")

        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()

    def __str__(self) -> str:
        medicamentos_listado = "\n  - " + "\n  - ".join(self.__medicamentos)
        return (
            f"RECETA MÉDICA\n"
            f"Fecha de emisión: {self.__fecha.strftime('%d/%m/%Y %H:%M')}\n\n"
            f"Paciente:\n  {self.__paciente}\n\n"
            f"Médico:\n  {self.__medico}\n\n"
            f"Medicamentos recetados:{medicamentos_listado}"
        )
