from smartphone import Smartphone
from portatil import Portatil

def main():
    # Creamos una lista que almacenará tanto Smartphones como Portátiles
    dispositivos = []

    # Añadimos 2 smartphones
    dispositivos.append(Smartphone("Samsung", "Galaxy S21", 1, 3))
    dispositivos.append(Smartphone("Apple", "iPhone 13", 2, 2))

    # Añadimos 2 portátiles
    dispositivos.append(Portatil("HP", "Pavilion", 1, 6))
    dispositivos.append(Portatil("Dell", "XPS 15", 3, 8))

    # Actualizamos firmware de todos
    for dispositivo in dispositivos:
        dispositivo.actualizar_firmware()

    # Mostramos los datos de todos los dispositivos
    print("Datos actuales de los dispositivos:")
    for dispositivo in dispositivos:
        print(dispositivo)

if __name__ == "__main__":
    main()