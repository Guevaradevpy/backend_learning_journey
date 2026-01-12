#Polimorfismo por duck typing (paramétrico)
#Creamos las clases.
class Gato():
    def sonido(self):
        return "Miau"
    
class Perro():
    def sonido(self):
        return  "Guau"

#Hacemos la funcion, con argumento animal, despues la llamamos con la clase de gato a perro.
def hacer_sonido(animal):
    print(animal.sonido())
 
#Creamos el objecto    
gato = Gato()
perro = Perro()

print(gato.sonido())

#La llame con gato.
hacer_sonido(gato)        


#Polimorfismo de sobreescritura (Overriding) → cuando heredas y redefinís métodos.
# Mi ejemplo
class Naked():
    def funcion(self):
        return "Torque"
    
class Turismo():
    def funcion(self):
        return "Comodidad"
    
class Deportiva():
    def funcion(self): 
        return "Velocidad"      
     
     
def tipo_funcion(bike):
    return bike.funcion()

#Lista de objetos.
motos = [Naked(), Turismo(), Deportiva()]            
for moto in motos:
    print(moto.funcion())

#Objeto indivifual.
naked = Naked()
turismo = Turismo()
deportiva = Deportiva()

#Se llama la funcion con la variable en este caso en (naked) -NO- (Naked)    
print(f"La funcion de la naked es: {tipo_funcion(naked)}")
print(f"La funcion de la turismo es:{tipo_funcion(turismo)}")
print(f"La funcion de la deportiva es: {tipo_funcion(deportiva)}")

# Tener en cuenta la funcion de print y return en un metodo(DEF).