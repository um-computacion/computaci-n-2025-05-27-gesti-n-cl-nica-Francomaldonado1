from modelo.clinica import Clinica
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from datetime import datetime
from modelo.excepciones import *

clinica = Clinica()

def mostrar_menu():
    print("\nMenú Principal")
    print("1. Agregar paciente")
    print("2. Agregar médico")
    print("3. Agendar turno")
    print("4. Agregar especialidad a médico")
    print("5. Emitir receta")
    print("6. Ver historia clínica")
    print("7. Ver todos los turnos")
    print("8. Ver todos los pacientes")
    print("9. Ver todos los médicos")
    print("0. Salir")

def agregar_paciente():
    try:
        nombre = input("Introduzca el nombre completo (nombre y apellido): ").strip()
        if len(nombre.split()) < 2:
            print("Error: Debe ingresar al menos nombre y apellido.")
            return
        nombre = " ".join(nombre.split())  # Limpia espacios múltiples
        nombre = nombre.title()  # Formatea correctamente el nombre

        dni = input("DNI del paciente: ").strip()
        fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ").strip()
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        
        paciente = Paciente(nombre, dni, fecha_nacimiento)
        mensaje = clinica.agregar_paciente(paciente)
        print(mensaje)
    except PacienteYaRegistradoException as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Formato de fecha inválido. Use dd/mm/aaaa.")
    except Exception as e:
        print(f"Error inesperado: {e}")


def agregar_medico():
    try:
        nombre = input("Nombre del médico: ").strip()
        matricula = input("Matrícula del médico: ").strip()
        medico = Medico(nombre, matricula)

        while True:
            nombre_especialidad = input("Nombre de la especialidad (o enter para terminar): ").strip()
            if not nombre_especialidad:
                break

            dias = input("Días de atención (separados por coma): ").strip()
            dias_lista = [dia.strip().capitalize() for dia in dias.split(",") if dia.strip()]

            especialidad = Especialidad(nombre_especialidad, dias_lista)
            medico.agregar_especialidad(especialidad)

        mensaje = clinica.agregar_medico(medico)
        print(mensaje)

    except MedicoYaRegistradoException as e:
        print(f"Error: {e}")
    except DatoInvalidoException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


def agendar_turno():
    try:
        dni = input("DNI del paciente: ").strip()
        matricula = input("Matrícula del médico: ").strip()
        especialidad = input("Especialidad: ").strip()
        fecha_hora = input("Fecha y hora del turno (dd/mm/aaaa HH:MM): ").strip()
        fecha_hora = datetime.strptime(fecha_hora, "%d/%m/%Y %H:%M")
        mensaje = clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
        print(mensaje)
    except (PacienteNoEncontradoException, MedicoNoEncontradoException, TurnoOcupadoException, MedicoNoDisponibleException) as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Formato de fecha y hora inválido. Use dd/mm/aaaa HH:MM.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def agregar_especialidad_medico():
    try:
        matricula = input("Matrícula del médico: ").strip()
        nombre_especialidad = input("Nombre de la especialidad: ").strip()
        dias = input("Días de atención (separados por coma): ").strip().split(",")
        dias = [d.strip().lower() for d in dias]
        especialidad = Especialidad(nombre_especialidad, dias)
        medico = clinica.obtener_medico_por_matricula(matricula)
        medico.agregar_especialidad(especialidad)
        print(f"Especialidad agregada correctamente al médico {medico.obtener_nombre()}.")
    except MedicoNoEncontradoException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def emitir_receta():
    try:
        dni = input("DNI del paciente: ").strip()
        matricula = input("Matrícula del médico: ").strip()
        medicamentos = input("Ingrese medicamentos separados por coma: ").strip().split(",")
        medicamentos = [m.strip() for m in medicamentos if m.strip()]
        mensaje = clinica.emitir_receta(dni, matricula, medicamentos)
        print(mensaje)
    except (PacienteNoEncontradoException, MedicoNoEncontradoException, RecetaInvalidaException) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def ver_historia_clinica():
    try:
        dni = input("DNI del paciente: ").strip()
        historia = clinica.obtener_historia_clinica(dni)
        print(historia)
    except HistoriaClinicaNoEncontradaException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def ver_todos_los_turnos():
    turnos = clinica.obtener_turnos()
    if not turnos:
        print("No hay turnos registrados.")
    else:
        for turno in turnos:
            print(turno)

def ver_todos_los_pacientes():
    pacientes = clinica.obtener_pacientes()
    if not pacientes:
        print("No hay pacientes registrados.")
    else:
        for paciente in pacientes:
            print(paciente)

def ver_todos_los_medicos():
    medicos = clinica.obtener_medicos()
    if not medicos:
        print("No hay médicos registrados.")
    else:
        for medico in medicos:
            print(medico)

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            agregar_paciente()
        elif opcion == "2":
            agregar_medico()
        elif opcion == "3":
            agendar_turno()
        elif opcion == "4":
            agregar_especialidad_medico()
        elif opcion == "5":
            emitir_receta()
        elif opcion == "6":
            ver_historia_clinica()
        elif opcion == "7":
            ver_todos_los_turnos()
        elif opcion == "8":
            ver_todos_los_pacientes()
        elif opcion == "9":
            ver_todos_los_medicos()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    mostrar_menu()
