from usuarios import Cliente, Entrenador 
from actividades import ClaseColectiva, EntrenamientoPersonal
from reservas import Reserva
from excepciones import PlazasAgotadasError

# DATOS INICIALES PRECARGADOS

# Creamos clientes, entrenadores y actividades iniciales para no empezar desde cero
clientes = [
    Cliente("Ana López", "ana@gmail.com"),
    Cliente("Miguel Torres", "miguel@gmail.com"),
    Cliente("Sofía Martínez", "sofia@gmail.com")
]

entrenadores = [
    Entrenador("Gema Rodríguez", "gema@fitlife.com", "Fitness"),
    Entrenador("Carlos Gómez", "carlos@fitlife.com", "Yoga"),
    Entrenador("Enzo Rodríguez", "enzo@fitlife.com", "Pilates")
]

actividades = [
    ClaseColectiva("Yoga", 10.0, 5),
    ClaseColectiva("Spinning", 12.0, 4),
    EntrenamientoPersonal("Crossfit Personal", 20.0, 2, 25),
    EntrenamientoPersonal("Pilates Personal", 18.0, 1, 20)
]


# FUNCIONES DE LISTADO

def listar_clientes():
    """
    Muestra todos los clientes disponibles con numeración.
    """
    for i, c in enumerate(clientes):
        print(f"{i + 1}. {c.get_nombre()}")

def listar_actividades():
    """
    Muestra todas las actividades disponibles con su nombre y estado de ocupación.
    """
    for i, a in enumerate(actividades):
        print(f"{i + 1}. {a.get_nombre()} ({a.get_estado_ocupacion()})")


# FUNCIÓN PARA CREAR CLIENTE

def crear_cliente():
    """
    Solicita datos para crear un nuevo cliente, lo añade a la lista de clientes
    y devuelve el objeto Cliente creado.
    """
    nombre = input("Nombre: ")
    email = input("Email: ")
    nuevo = Cliente(nombre, email)
    clientes.append(nuevo)
    print(f"Cliente {nombre} creado correctamente.")
    return nuevo


# FUNCIÓN DE RESERVA

def realizar_reserva(cliente_actual=None):
    """
    Permite realizar una reserva de actividad.
    Si cliente_actual está definido, se usa ese cliente automáticamente.
    Si no, se pide seleccionar uno de los clientes existentes o crear uno nuevo.
    """
    if not clientes or not actividades:
        print("Debe haber clientes y actividades.")
        return

    # Selección de cliente
    if cliente_actual:
        c = cliente_actual
    else:
        while True:
            print("\nClientes disponibles:")
            listar_clientes()
            print(f"{len(clientes)+1}. Añadir nuevo cliente")
            try:
                seleccion = int(input("Seleccione cliente: "))
                if seleccion == len(clientes)+1:
                    c = crear_cliente()
                else:
                    c = clientes[seleccion - 1]
                break
            except (IndexError, ValueError):
                print("Cliente no válido, vuelve a intentarlo.")

    # Selección de actividad
    listar_actividades()
    try:
        a = actividades[int(input("Seleccione actividad: ")) - 1]
    except (IndexError, ValueError):
        print("Actividad no válida")
        return

    # Intentar reservar y manejar posibles errores
    try:
        Reserva(c, a)
        print(f"Reserva realizada correctamente para {c.get_nombre()}.")
    except PlazasAgotadasError as e:
        print("ERROR:", e)


# MENÚ CLIENTE

def menu_cliente(cliente_actual=None):
    """
    Menú específico para clientes.
    Permite ver actividades, realizar reservas o consultar reservas propias.
    """
    while True:
        print("\n--- MENÚ CLIENTE ---")
        print("1. Ver actividades disponibles")
        print("2. Realizar reserva")
        print("3. Ver mis reservas")
        print("4. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            listar_actividades()
        elif opcion == "2":
            realizar_reserva(cliente_actual)
        elif opcion == "3":
            # Mostrar reservas del cliente actual si existe
            if cliente_actual:
                cliente_actual.mostrar_reservas()
            else:
                listar_clientes()
                try:
                    c = clientes[int(input("Selecciona tu número de cliente: ")) - 1]
                    c.mostrar_reservas()
                except (IndexError, ValueError):
                    print("Cliente no válido")
        elif opcion == "4":
            break
        else:
            print("Opción no válida")


# MENÚ ENTRENADOR

def menu_entrenador():
    """
    Menú específico para entrenadores.
    Permite ver entrenadores registrados y las actividades con su ocupación.
    """
    while True:
        print("\n--- MENÚ ENTRENADOR ---")
        print("1. Ver entrenadores registrados")
        print("2. Ver actividades y ocupación")
        print("3. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            for e in entrenadores:
                print(f"{e.get_nombre()} - Especialidad: {e.get_especialidad()}")
        elif opcion == "2":
            listar_actividades()
        elif opcion == "3":
            break
        else:
            print("Opción no válida")

# INICIO DEL SISTEMA

def iniciar_sesion():
    """
    Pantalla de bienvenida y selección de tipo de usuario.
    Dependiendo de la elección, se dirige al menú cliente o entrenador.
    """
    print("\n=== BIENVENIDO A FITLIFE CENTER ===")
    tipo = input("Eres cliente o entrenador? (cliente/entrenador): ").strip().lower()

    if tipo == "cliente":
        # Pregunta si es cliente nuevo o registrado
        respuesta = input("¿Eres un cliente registrado o nuevo? (registrado/nuevo): ").strip().lower()
        if respuesta == "nuevo":
            nuevo_cliente = crear_cliente()
            menu_cliente(cliente_actual=nuevo_cliente)
        elif respuesta == "registrado":
            menu_cliente()
        else:
            print("Opción no válida, vuelve a intentarlo.")
            iniciar_sesion()
    elif tipo == "entrenador":
        menu_entrenador()
    else:
        print("Opción no válida, vuelve a intentarlo.")
        iniciar_sesion()

# BUCLE PRINCIPAL

def main():
    """
    Bucle principal del programa.
    Permite iniciar sesión repetidamente hasta que el usuario decida salir.
    """
    while True:
        iniciar_sesion()
        # Pregunta final de salida
        salir = input("\n¿Deseas salir del sistema? (s/n): ").strip().lower()
        if salir == "s":
            print("Gracias por usar FitLife Center. ¡Hasta pronto!")
            break

# Punto de entrada del programa
if __name__ == "__main__":
    main()
