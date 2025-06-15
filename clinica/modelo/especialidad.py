from modelo.excepciones import (
    TipoEspecialidadInvalidoException,
    DiasEspecialidadInvalidosException,
    DiaInvalidoException
)

class Especialidad:
    def __init__(self, tipo: str, dias: list[str]):
        self.__validar_tipo(tipo)
        self.__tipo = tipo
        self.dias = dias  # Usa el setter para validar y asignar

    def __validar_tipo(self, tipo: str):
        if not tipo or not isinstance(tipo, str):
            raise TipoEspecialidadInvalidoException()

    def __validar_dias(self, dias: list[str]) -> list[str]:
     dias_validos = {
        "lunes": "lunes",
        "martes": "martes",
        "miercoles": "miércoles",  # ← permitimos sin tilde
        "miércoles": "miércoles",
        "jueves": "jueves",
        "viernes": "viernes",
        "sabado": "sábado",        # ← permitimos sin tilde
        "sábado": "sábado",
        "domingo": "domingo"
    }

     if not dias or not isinstance(dias, list) or not all(isinstance(d, str) for d in dias):
        raise DiasEspecialidadInvalidosException()

     dias_normalizados = []
     for d in dias:
        clave = d.strip().lower()
        if clave not in dias_validos:
            raise DiaInvalidoException()
        dias_normalizados.append(dias_validos[clave])

     return dias_normalizados


    def obtener_especialidad(self) -> str:
        return self.__tipo

    def obtener_dias(self) -> list[str]:
        return self.__dias

    @property
    def nombre(self) -> str:
        return self.__tipo

    @property
    def dias(self) -> list[str]:
        return self.__dias

    @dias.setter
    def dias(self, nuevos_dias: list[str]):
        self.__dias = self.__validar_dias(nuevos_dias)

    def verificar_dia(self, dia: str) -> bool:
        if not isinstance(dia, str):
            return False
        return dia.lower() in self.__dias

    def __str__(self) -> str:
        dias_legibles = ", ".join(self.__dias).capitalize()
        return f"Especialidad: {self.__tipo} | Días de atención: {dias_legibles}"



