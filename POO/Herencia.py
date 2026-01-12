class Persona:
    def __init__(self, nombre, edad, nacionalidad):
       self.nombre = nombre
       self.edad = edad
       self.nacionalidad  = nacionalidad

#Vamos a crear herencia.
class Empleado(Persona):
    #volvemos a traer todos lo de persona y los nuevos atributos.
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        #Para heredar solo una clase
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
    
    #Funciona para cuando lo llamemos imprima todos sus datos.
    def __str__(self):
        return f"Empleado: {self.nombre}, {self.edad} años, {self.nacionalidad}, Cargo: {self.trabajo}, Salario: {self.salario}"    
    
class Estudiante(Persona): 
    def __init__(self, nombre, edad, nacionalidad, notas, curso):
        super().__init__(nombre, edad, nacionalidad)       
        self.notas = notas
        self.curso = curso
        
class Profesor(Persona):
    def __init__(self, nombre, edad, nacionalidad, saber, area):
        super().__init__(nombre, edad, nacionalidad)       
        self.saber = saber
        self.area = area
        
         
#Estatico con las propiedades de CLASS_Persona.
persona = Persona("Pablo", 21, "Arabe")
empleado = Empleado("Cuco", 30, "colombiano", "Empleado", "US.13")
estudiante = Estudiante("Juan", 16, "colombiano","4.5", "9no")
profesor = Profesor("Jorge", 25, "colombiano","Sistemas", "Ingenieria")

print(persona.nombre)
print(empleado)
print(estudiante.nombre)
print(profesor.nombre)

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def descripcion(self):
        return f"Nombre: {self.nombre} | Edad: {self.edad}"    

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    def descripcion(self):
        base = super().descripcion() #Va hacia la clase padre y coje todo
        return f"{base} | Carrera: {self.carrera}"
    

p1 = Persona("Lupi", 22)
e1 = Estudiante("Lupillo", 22, "Bandidaje")
print(e1.descripcion())
print(p1.descripcion())