# Gestión de Notas de Estudiantes

Este proyecto es una aplicación sencilla en Python que permite registrar los nombres y las notas de estudiantes, y guardar esta información en un archivo Excel (`ejercicio1.xlsx`) utilizando la biblioteca `openpyxl`.

## Descripción

El programa realiza las siguientes tareas:
1. Solicita al usuario ingresar los nombres y las notas de tres estudiantes.
2. Almacena esta información en un diccionario.
3. Crea un archivo Excel con dos columnas: "Estudiante" y "Nota".
4. Escribe los datos ingresados en el archivo Excel.
5. Guarda el archivo como `ejercicio1.xlsx` en el directorio actual.

## Requisitos

Antes de ejecutar el programa, asegúrate de tener instalado lo siguiente:

- Python 3.7 o superior
- Las bibliotecas listadas en el archivo `requirements.txt`:
  - `openpyxl==3.1.5`
  - `et_xmlfile==2.0.0`

## Instalación

1. Abre la terminal y clona este repositorio o descarga los archivos en tu máquina local.
   ```bash
   git clone https://github.com/CarlosQuiroz25/evaluacion_semana6.git
   
2. Navega al directorio del proyecto y activa el entorno virtual.
   ```bash
    venv\Scripts\Activate.ps1
   
3. Instala las dependencias ejecutando el siguiente comando:

   ```bash
   pip install -r requirements.txt

## Uso

1. Ejecuta el programa con el siguiente comando en la terminal:

   ```bash
   python main.py

2. Ingresa los nombres y las notas de tres estudiantes cuando se te solicite.

3. Una vez completada la entrada de datos, el programa generará un archivo Excel llamado ejercicio1.xlsx en el directorio actual.

4. Abre el archivo Excel para ver los datos ingresados.

## Notas
Asegúrate de tener permisos de escritura en el directorio donde se ejecuta el programa, ya que el archivo Excel se guardará allí.
Si deseas cambiar el número de estudiantes, puedes modificar el rango del ciclo for en el archivo main.py.
