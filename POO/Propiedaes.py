# Con propiedad definimos (GET/SET/DELETE) de un atributo
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self.__edad = edad  # name mangling

    # GETTERS
    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self.__edad

    # SETTERS
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @edad.setter
    def edad(self, nueva_edad):
        self.__edad = nueva_edad

    # DELETERS
    @edad.deleter
    def edad(self):
        print("Eliminando edad...")
        del self.__edad

#Pruebas
persona = Persona("Lupi", 21)

print(persona.nombre)  # Lupi

persona.nombre = "Jorge"
print(persona.nombre)  # Jorge

del persona.edad       # elimina _Persona__edad

# print(persona.edad)  #    AttributeError si descomentas esto (ya no existe)

persona.edad = 23      # recrea mediante setter
print(persona.edad)    # 23

