# 📄 Documentación del Sistema de Gestión Clínica

Este archivo contiene la información necesaria para ejecutar el sistema, correr las pruebas unitarias y entender su diseño general.

## ✅ Cómo ejecutar el sistema

Desde la raíz del proyecto, utilizar los siguientes comandos:

cd clinica
python3 -m interfaz.CLI

## ✅ Cómo ejecutar las pruebas unitarias

Desde la raíz del proyecto, utilizar los siguientes comandos:

python3 -m unittest discover tests  #Para ejecutar todas las pruebas unitarias
python3 -m unittest tests.test_(clase que quiera probar) #Para ejecutar una prueba unitaria en particular

Ejemplos de uso: 

python3 -m unittest tests.test_paciente
python3 -m unittest tests.test_medico
python3 -m unittest tests.test_historiaclinica

## ✅ Explicación del diseño general

El sistema está estructurado en tres componentes principales, siguiendo una arquitectura clara para facilitar la organización y el mantenimiento del código:

1. Carpeta modelo/

Contiene las clases principales del sistema:

Paciente, Medico, Turno, Especialidad, Clinica, etc.

Cada clase está implementada en su propio archivo .py.

También incluye el archivo excepciones.py, donde se definen las excepciones personalizadas utilizadas para validar entradas y estados del sistema.

2. Carpeta interfaz/

Incluye la interfaz de línea de comandos:

El archivo CLI.py contiene el menú principal con 10 opciones numeradas (del 0 al 9).

Este archivo captura excepciones y muestra mensajes claros y comprensibles para el usuario final.

La interfaz es el único punto de entrada para el usuario.

3. Carpeta tests/

Incluye los tests unitarios desarrollados con unittest:

Cada clase del sistema tiene su archivo de pruebas correspondiente (ej. test_paciente.py, test_medico.py, etc.).

Se testean tanto los casos normales como los errores esperados, lanzando y atrapando excepciones personalizadas cuando corresponde.

