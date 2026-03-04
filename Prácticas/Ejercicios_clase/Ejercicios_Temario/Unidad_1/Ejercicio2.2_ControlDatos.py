# CONTROL DE DATOS

""" Crea una aplicación que permita gestionar los proyectos de una empresa. Para
ello sigue estos pasos:
o Pregunta al usuario cuantos proyectos va a registrar.
o Por cada proyecto, pide el código, nombre, responsable y presupuesto del
proyecto.
o Guarda la información de todos los proyectos en un diccionario (puedes
utilizar el código como la clave y como valor puedes utilizar otro diccionario
o lista.
o Muestra por consola solo el nombre y presupuesto de cada uno de los
proyectos.
 
"""

print("--- PROYECTO EMPRESA ---")

num_proyectos_str = input("¿Cuántos proyectos vas a registrar? ")

# Compruebo si el texto introducido NO son solo dígitos
if not num_proyectos_str.isdigit():
    print("Error: Debes introducir un número entero (ej: 3).")
    exit() # Salimos del programa si la entrada no es un número


# Si el código llega aquí, es un número válido. Lo convertimos.
total_proyectos = int(num_proyectos_str)


# Guardo la información en un diccionario
proyectos_db = {} 

print(f"\nPerfecto, vamos a registrar {total_proyectos} proyectos.")

# Por cada proyecto, pide los datos...
# (Usamos un bucle 'for' que se repite 'total_proyectos')
for i in range(total_proyectos):
    print(f"\n--- Datos del Proyecto {i + 1} ---")
    
    codigo = input("Introduce el CÓDIGO del proyecto: ")
    nombre = input("Introduce el NOMBRE del proyecto: ")
    responsable = input("Introduce el RESPONSABLE: ")
    
    # Validamos también el presupuesto
    presupuesto_str = input("Introduce el PRESUPUESTO (ej: 5000): ")
    if not presupuesto_str.isdigit():
        print("Valor no numérico. Se guardará presupuesto como 0.")
        presupuesto = 0
    else:
        presupuesto = int(presupuesto_str)

    # 1. Creamos el diccionario "valor" (con la info)
    info_proyecto = {
        "nombre": nombre,
        "responsable": responsable,
        "presupuesto": presupuesto
    }
    
    # 2. Añadimos al diccionario "principal"
    proyectos_db[codigo] = info_proyecto

print("\n...Registro de proyectos finalizado.")

print("\n--- RESUMEN DE PROYECTOS REGISTRADOS ---")

# Iteramos sobre el diccionario principal (proyectos_db)
# .items() nos da la clave (codigo) y el valor (info) en cada vuelta
for codigo, info in proyectos_db.items():
    
    # 'info' es el diccionario interno
    nombre_proyecto = info["nombre"]
    presupuesto_proyecto = info["presupuesto"]
    
    print(f"Proyecto: {nombre_proyecto} | Presupuesto: {presupuesto_proyecto}€")



