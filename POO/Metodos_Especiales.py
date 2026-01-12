#VAMOS CON CONSRUCTOR

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'

    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'
    
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevo_valor)
   
lupi = Persona("lupi", 21)
juan = Persona("Juan", 12)
jorge = Persona("Jorge", 47)

nuevo_valor = lupi + juan + jorge
print(nuevo_valor.edad)    

#Ejemplo practico
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        # Representación bonita para el usuario
        return f'{self.nombre}, {self.edad} años'

    def __repr__(self):
        # Representación más técnica (debug)
        return f'Persona("{self.nombre}", {self.edad})'

    def __add__(self, otra):
        # Combinar dos personas (como si fueran "amigos")
        nuevo_nombre = self.nombre + "-" + otra.nombre
        nueva_edad = (self.edad + otra.edad) // 2  # promedio de edades
        return Persona(nuevo_nombre, nueva_edad)

# Crear personas
lupi = Persona("Lupi", 22)
ana = Persona("Ana", 20)
juan = Persona("Juan", 25)

# 1. __str__ (print bonito)
print(lupi)  
# 👉 Lupi, 22 años

# 2. __repr__ (debug)
print(repr(ana))  
# Persona("Ana", 20)

# 3. __add__ (sumar personas = crear "amistad")
nuevo = lupi + ana
print(nuevo)  
# Lupi-Ana, 21 años


