#ABC significa clase base abstracta
from abc import ABC, abstractmethod

#Esta clase está hecha para que otras clases la tomen como modelo o molde.
#La clase abtracta no se puede instanciar es decir crear un objeto.
class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad =  edad
        self.sexo = sexo 
        self.actividad = actividad
        
    @abstractmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad) 
        
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self. actividad}")           
        
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad) 
        
    def hacer_actividad(self):
        print(f"Estoy trabajando en el rubro de: {self. actividad}")          

#Solo creamks objetos de las clases que heredan.        
lupi = Estudiante("Lupi", 21, "Masculino", "Programacion")
jorge = Trabajador("Jorge", 21, "Masculino", "Programacion")        


jorge.presentarse()
jorge.hacer_actividad()
lupi.presentarse()
lupi.hacer_actividad()

#Mi Ejemplo
from abc import ABC, abstractmethod

class Moto(ABC):
    @abstractmethod
    def __init__(self, modelo, CC, precio, funcionar):
        self.modelo = modelo
        self.CC = CC
        self.precio = precio
        self.funcionar = funcionar
    
    @abstractmethod
    def funcion(self):
        pass
        
    def presentarse(self):
        print(f"Soy una {self.modelo} y mi precio es de {self.precio}.") 

class Naked(Moto):
    def __init__(self, modelo, CC, precio, funcionar):
        super(). __init__(modelo, CC, precio, funcionar)
        
    def funcion(self):    
        print(f"Mi funcion es: {self.funcionar}")
        
class Turismo(Moto):
    def __init__(self, modelo, CC, precio, funcionar):
        super(). __init__(modelo, CC, precio, funcionar)
        
    def funcion(self):    
        print(f"Mi funcion es: {self.funcionar}")     
        
naked = Naked("S1000RM", 1000, "USD-25000", "Velocidad")
turismo = Turismo("GAS_GAS", 750, "USD-15000", "Torque")

naked.presentarse()
naked.funcion()
turismo.presentarse()
turismo.funcion()        



#EJENPLO DIDACTICO
#El plano dice: “toda casa debe tener puertas, ventanas y un techo”.
# Pero el plano no es una casa real (no puedes vivir en el plano).
# Lo que haces es crear casas concretas (Casa de madera, Casa de ladrillo) que sí cumplen con el plano, pero cada una a su manera.
# La clase abstracta = el plano.
# Las clases hijas = las casas construidas.
