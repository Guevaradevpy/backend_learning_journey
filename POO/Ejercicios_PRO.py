class Personaje:
    #Nuestro Molde
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre =  nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    #Tarjeta de presentacion del objeto
    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    
    #Con esto creamos a nuestro nuevo personaje
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = ((self.fuerza+otro_pj.fuerza)/2)**2
        nueva_velocidad = ((self.velocidad+otro_pj.velocidad)/2)**2
        #Importante guardar las variables dentro de la clase
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

#Creamos un diccionario para guardar los resultados de los inputs.
personajes = {}

while True:
    print("\n1. Crear personaje.")
    print("2. Fusionar personaje. ")
    print("3. Peersonajes creados")
    print("4. Salir. ")
    
    #Manejo de errores
    try:
        opcion = input("Ingresa tu opcion: ")
        
        if opcion == "1":
            nombre = input("Ingresa nombre: ").lower()
            fuerza =  int(input("Ingresa fuerza: "))
            velocidad =int(input("Ingresa velocidad: "))
            personajes[nombre] = Personaje(nombre, fuerza, velocidad)
            print(f"{nombre} Creado con exito.")
            
        elif opcion == "2":
            fu1 = input("Ingrese nombre primer personaje: ").lower()
            fu2 = input("Ingrese nombre del segundo personaje: ").lower()
            #Busca en personajes el fu1 y fu2
            if fu1 in personajes and fu2 in personajes:
                resultado = personajes[fu1] + personajes[fu2] 
                print("Resultado de la fusion: ", resultado)
                #Guarda el nombre + todo lo de la variable resultado
                personajes[resultado.nombre] = resultado
            else:
                print("Alguno de los personajes no existe")    
        
        elif opcion == "3":
            print("\n Personajes creados: ")
            for p in personajes.values():
                print("-", p) 
        
        elif opcion == "4":
            print("Hasta Luego")
            break
        
        else:
            print("Opcion no valida")            
    
    except ValueError:
        print("Ingresa solo numeros")        