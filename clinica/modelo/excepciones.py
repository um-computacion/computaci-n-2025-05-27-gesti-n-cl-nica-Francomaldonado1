
class PacienteNoEncontradoException(Exception):
    pass

class PacienteYaRegistradoException(Exception):
    pass

class MedicoNoDisponibleException(Exception):
    pass

class MedicoYaRegistradoException(Exception):
    pass

class MedicoNoEncontradoException(Exception):
    pass

class MedicamentosInvalidosException(Exception):
    pass

class TurnoOcupadoException(Exception):
    pass

class HistoriaClinicaNoEncontradaException(Exception):
    pass

class FechaInvalidaException(Exception):
    def __init__(self, mensaje="La fecha debe tener el formato dd/mm/aaaa"):
        super().__init__(mensaje)

class NombreInvalidoException(Exception):
    def __init__(self, mensaje="El nombre completo no puede estar vacío."):
        super().__init__(mensaje)

class MatriculaInvalidaException(Exception):
    def __init__(self, mensaje="La matrícula no puede estar vacía."):
        super().__init__(mensaje)

class MatriculaInvalidaException(Exception):
    def __init__(self, mensaje="La matrícula no puede estar vacía."):
        super().__init__(mensaje)

class EspecialidadDuplicadaException(Exception):
    def __init__(self, mensaje="Especialidad duplicada para este médico."):
        super().__init__(mensaje)

class DatoInvalidoException(Exception):
    pass

class TipoEspecialidadInvalidoException(Exception):
    def __init__(self, mensaje="Debe indicar el nombre de la especialidad (por ejemplo: Cardiología)."):
        super().__init__(mensaje)

class EspecialidadNoDisponibleException(Exception):
    pass

class EspecialidadInvalidaException(Exception):
    def __init__(self, mensaje="La especialidad no coincide con las especialidades del médico."):
        super().__init__(mensaje)

class DiasEspecialidadInvalidosException(Exception):
    def __init__(self, mensaje="Debe proporcionar una lista de días válidos (por ejemplo: ['lunes', 'miércoles'])."):
        super().__init__(mensaje)

class DiaInvalidoException(Exception):
    def __init__(self, mensaje="Algunos días ingresados no son válidos. Use días como 'lunes', 'martes', etc."):
        super().__init__(mensaje)

class RecetaInvalidaException(Exception):
    pass


