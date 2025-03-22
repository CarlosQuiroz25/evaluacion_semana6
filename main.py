import openpyxl

# PARTE 1: Crear diccionario y entrada de datos
# Crea un diccionario vacío llamado 'estudiantes'
estudiantes = {}
# Usa un ciclo for para pedir 3 nombres y notas (convierte la nota a float)
for i in range(3):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    estudiantes[nombre] = nota

# PARTE 2: Crear archivo Excel
# Crea un nuevo libro de trabajo con openpyxl.Workbook()
libro = openpyxl.Workbook()
# Obtén la hoja activa
hoja = libro.active

# PARTE 3: Escribir encabezados
# Escribe "Estudiante" en A1 y "Nota" en B1
hoja["A1"] = "Estudiante"
hoja["B1"] = "Nota"

# PARTE 4: Escribir datos con ciclo
fila = 2
# Usa un ciclo for para recorrer el diccionario
# Escribe el nombre en la columna A y la nota en la columna B
for nombre, nota in estudiantes.items():
    hoja[f"A{fila}"] = nombre
    hoja[f"B{fila}"] = nota
    fila += 1

# PARTE 5: Guardar archivo
# Guarda el archivo como "ejercicio1.xlsx"
libro.save("ejercicio1.xlsx")
print("¡Ejercicio 1 guardado en ejercicio1.xlsx!")