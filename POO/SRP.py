# CLASE TANQUE DE COMBUSTIBLE

class TanqueDeCombustible:
    def __init__(self):
        # El tanque arranca con 100 unidades de combustible (ESTATICO).
        self.combustible = 100                       
    
    def agregar_combustible(self, cantidad):
        # Agrega cierta cantidad de combustible al tanque
        self.combustible += cantidad
        return self.combustible
        
    def obtener_combustible(self):
        # Devuelve cuánta gasolina queda en el tanque
        return self.combustible
    
    def usar_combustible(self, cantidad):
        # Resta la cantidad de gasolina usada
        self.combustible -= cantidad


# CLASE AUTO

class Auto:
    def __init__(self, tanque):
        # El auto arranca en la posición 0 (kilómetro 0) (ESTATICA)
        self.posicion = 0
        # El auto recibe un tanque de combustible (inyectamos la dependencia)
        self.tanque = tanque
        
    def mover(self, distancia):
        # Antes de moverse, revisa si hay suficiente combustible:
        # La regla es: por cada 2 km necesita 1 de combustible
        if self.tanque.obtener_combustible() >= distancia / 2:
            # Si alcanza la gasolina, avanza esa distancia
            self.posicion += distancia
            # Consume el combustible proporcional a la distancia
            self.tanque.usar_combustible(distancia / 2)
            print("Has movido el auto exitosamente.")
        else:
            # Si no alcanza la gasolina, no se mueve
            print("No hay suficiente combustible.")

    def obtener_posicion(self):
        # Devuelve la posición actual del auto
        return self.posicion
        
# PROGRAMA PRINCIPAL

# Creamos tanuqe, creamos auto y le pasamos el tanque como dependencia
tanque = TanqueDeCombustible()
auto = Auto(tanque)
print(auto.obtener_posicion())
auto.mover(5)
print(auto.obtener_posicion())
auto.mover(10)  
print(auto.obtener_posicion())
auto.mover(20) 
print(auto.obtener_posicion())
auto.mover(25)          
print(auto.obtener_posicion())

# Finalmente, mostramos cuánto combustible queda en el tanque
print(f"\nTe queda: {tanque.obtener_combustible()} de combustible.")
print(f"Haz agregado combustible ahora tienes: {tanque.agregar_combustible(70)}.")
print(f"Tu actual posicio es: {auto.obtener_posicion()}")