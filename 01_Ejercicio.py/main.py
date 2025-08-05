from registroVehiculo import RegistroVehiculo
from exception import LongitudMatriculaNoValidaException, FormatoMatriculaNoValidoException

def mostrar_menu():
    print("\n--- MENÚ DE REGISTRO DE VEHÍCULOS ---")
    print("1. Introducir matrícula")
    print("2. Introducir marca")
    print("3. Introducir año de matriculación")
    print("4. Salir")
 
def main():
    vehiculo = RegistroVehiculo()

    while True:
        mostrar_menu()

        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Error: Debes introducir un número.")
            continue

        if opcion == 1:
            matricula = input("Introduce la matrícula (ej. 1234ABC): ")
            try:
                vehiculo.matricula = matricula
                print("Matrícula registrada correctamente.")
            except (LongitudMatriculaNoValidaException, FormatoMatriculaNoValidoException) as e:
                print(f"Error: {e}")

        elif opcion == 2:
            marca = input("Introduce la marca del vehículo: ")
            try:
                vehiculo.marca = marca
                print("Marca registrada correctamente.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == 3:
            anio_str = input("Introduce el año de matriculación: ")
            if anio_str.isdigit():
                try:
                    vehiculo.anio = int(anio_str)
                    print("Año registrado correctamente.")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Error: Debes introducir un número válido para el año.")

        elif opcion == 4:
            if vehiculo.esta_completo():
                print("\n Registro completado correctamente.")
                print(f"Matrícula: {vehiculo.matricula}")
                print(f"Marca: {vehiculo.marca}")
                print(f"Año: {vehiculo.anio}")
                break
            else:
                vehiculo.mostrar_campos_faltantes()
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
