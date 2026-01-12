class Persona:
    def __init__(self, nombre, edad, nacionalidad):
       self.nombre = nombre
       self.edad = edad
       self.nacionalidad  = nacionalidad

    def hablar(self):
        return "estoy practicando POO."
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
        
class Empleado_Artista(Persona, Artista): 
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        #Herencia de dos clases diferentes.
        Persona.__init__(self, nombre, edad, nacionalidad)       
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa     
     
    def presentarse(self):
        print (f"Hola soy {self.nombre}, {self.mostrar_habilidad()} y gano {self.salario} al año.")
        #return f"{super().mostrar_habilidad()}" #LLamar clase padre.
    
empleado_artista = Empleado_Artista("Jorge", 22, "Colombiano", "programar", "US.46000", "LupiCash")
#Cuando la funcion esta en su misma clase solo la llamamos.
empleado_artista.presentarse()

#Cuando esta en otra clase la imprimimos
print(empleado_artista.hablar()) #Clase persona
print(empleado_artista.mostrar_habilidad()) #Clase artista

#Observar cual heriencia pertence e instancia(OBJETO).
instancia = isinstance(empleado_artista, Empleado_Artista)
herencia = issubclass(Empleado_Artista, Artista)
print(herencia)
print(instancia)