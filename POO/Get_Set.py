# def get_nombre(self):  return self._nombre  (Protegido) "SIRVE PARA
# def get__edad(self): return self.__edad  (Privado)       AMBAS" 

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre # Protegido.
        self.__edad = edad # Privado.
        
    #Esta es la forma correcta de acceder (PROTEGIDO). Con return self._ejemplo asi accedemos.    
    def get_nombre(self):
        return self._nombre      
    #Esta es la forma correcta de acceder (PRIVADO)  
    def get_edad(self):
        return self.__edad
    
    #Modificar este atributo.
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
        
            
#Objeto / Uso    
persona = Persona("Lupi", 21)

#Variable que accede a la funcion get_nombre de la clase persona.       
nombre = persona.get_nombre()
print(nombre)
#Variable que accede a la funcion get__edad de la clase persona.  
edad = persona.get_edad()
print(edad)

#variable / uso de Set
persona.set_nombre("Jorge") #La modificacion
nombre = persona.get_nombre() #Para mostrar el nuevo cambio
print(nombre)

#print(persona._nombre) #Para acceder, aunque no es optimo.        