#Construimos una clase, Estatica y de un solo valor.
class Celular():
    #Atributos
    marca = "Apple"
    Modelo = "16 Pro Max"
    camara = "48mp"

#Construimos un objecto. (Instancia de Clase)
celular1 = Celular()    
print(celular1.marca) #Para acceder a un objeto


#METODO CONSTRUCTOR.
print("METODO CONSTRUCTOR")
class Phone:
    #Creamos constructor con __init__(self, ATRIBUTOS)
    def __init__(self, marca, modelo, camara):
        #Creando propiedad de self.
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    #Creamos otra funcion para la misma clase dentro del constructor.    
    def llamar(self):
        print(f"Estas llamando desde un: {self.modelo}")
    def cortar(self):
        print(f"Estas cortando desde un: {self.modelo}")        
        
#Creamos el objecto de esta clase
celu1 = Phone("Samsung", "S24 Ultra", "100MP")
celu2 = Phone("Apple", "16 Pro Max", "50MP")

#Imprimimos el objecto
print(celu2.marca)
#LLamar la definicion.
celu2.llamar()


#Definimos Clase
class Estudiante:
    #Creamos constructor
    def __init__(self, nombre, grado, edad):
        self.nombre = nombre
        self.grado = grado
        self.edad = edad
    
    #Creamos metodo estudiar    
    def estudiar(self):
        print("Perfecto estas Estudiando.")  
         
#Entrada de datos        
nombre = input("Ingresa tun nombre: ")
grado = input("Ingresa tu grado: ")
edad = input("Ingresa tu edad: ")        

#Creamos objecto            
Student = Estudiante(nombre, grado, edad)    
print(f"Datos del estudiante: {nombre} esta cursando un grado {grado}, con {edad} años")

#Bucle True
while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        Student.estudiar()        
        break