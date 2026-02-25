# Clase base: Habitacion
class Habitacion:
    def __init__(self, numero, precio_base):
        self.numero = numero
        self.precio_base = precio_base
        self.reservada = False
    def descripcion(self):
        return f"Habitación estándar con precio base de {self.precio_base}€"
    def calcular_precio_final(self):
        return self.precio_base
    def reservar(self):
        if not self.reservada:
            self.reservada = True
            return f"Habitación {self.numero} reservada con éxito."
        else:
            return f"Habitación {self.numero} ya está reservada."
# Clase hija: Suite
class Suite(Habitacion):
    def __init__(self, numero, precio_base, tiene_jacuzzi):
        super().__init__(numero, precio_base)
        self.tiene_jacuzzi = tiene_jacuzzi
def descripcion(self):
        jacuzzi = "Sí" if self.tiene_jacuzzi else "No"
        return f"Suite con jacuzzi: {jacuzzi}. Precio base: {self.precio_base}€"
def calcular_precio_final(self):
        return self.precio_base * 1.5
# Clase hija: HabitacionFamiliar
class HabitacionFamiliar(Habitacion):
    def __init__(self, numero, precio_base, capacidad_personas):
        super().__init__(numero, precio_base)
        self.capacidad_personas = capacidad_personas
    def descripcion(self):
        return f"Habitación familiar para {self.capacidad_personas} personas. Precio base: {self.precio_base}€"
    def calcular_precio_final(self):
        return self.precio_base * 1.2
# Clase Hotel
class Hotel:
    def __init__(self):
        self.habitaciones = []
    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
    def mostrar_disponibles(self):
        disponibles = [h for h in self.habitaciones if not h.reservada]
        print("Habitaciones disponibles:")
        for h in disponibles:
            print(f" - {h.numero}: {h.descripcion()} | Precio final: {h.calcular_precio_final()}€")
    def mostrar_todas(self):
        print("Información de todas las habitaciones:")
        for h in self.habitaciones:
            estado = "Reservada" if h.reservada else "Disponible"
            print(f" - {h.numero}: {h.descripcion()} | Precio final: {h.calcular_precio_final()}€ | Estado: {estado}")
    def reservar_habitacion(self, numero):
        for h in self.habitaciones:
            if h.numero == numero:
                print(h.reservar())
                return
                print(f"No se encontró la habitación {numero}.")
# Clase Entrada
class Entrada:
    def ejecutar():
        hotel = Hotel()
        # Crear y agregar habitaciones
        h1 = Habitacion(101, 80)
        h2 = Suite(202, 150, True)
        h3 = HabitacionFamiliar(303, 120, 4)
        hotel.agregar_habitacion(h1)
        hotel.agregar_habitacion(h2)
        hotel.agregar_habitacion(h3)
        # Reservar habitaciones
        hotel.reservar_habitacion(101)
        hotel.reservar_habitacion(202)
        # Mostrar información de todas las habitaciones
        print("\n--- TODAS LAS HABITACIONES ---")
        hotel.mostrar_todas()
        # Mostrar solo las disponibles
        print("\n--- HABITACIONES DISPONIBLES ---")
        hotel.mostrar_disponibles()
        # Ejecutar el programa desde la clase Entrada
Entrada.ejecutar()