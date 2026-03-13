from crud import (
    crear_tabla,
    insertar_socios,
    mostrar_socios,
    actualizar_socio,
    eliminar_socio
)

def mostrar_menu():
    """Imprime el menú por pantalla"""
    print("\n====== GESTIÓN DE SOCIO ======")
    print("1. Crear tabla")
    print("2. Insertar socio")
    print("3. Mostrar socios")
    print("4. Actualizar socio")
    print("5. Eliminar socio")
    print("6. Salir")


    def main():
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_tabla()
        elif opcion == "2":
            insertar_socios()
        elif opcion == "3":
            mostrar_socios()
        elif opcion == "4":
            actualizar_socio()
        elif opcion == "5":
            eliminar_socio()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
