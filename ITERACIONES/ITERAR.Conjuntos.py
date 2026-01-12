#BUCLE FOR ... Funciona Para Conjuntos, Listas Y Tuplas

#Conjuntos
animales = {"Gato", "Perro", "Loro", "Cocodrilo"}
nenas = {"Valentina", "Marcela", "Paula", "Sofia"}
numeros = {12,45,98,34}


for animal in animales: #SINTAXIS
    print(f"Ahora la Variable animal es: {animal}")
for numero in numeros:
    resultado = numero * 10
    print(resultado)    
    
# Recorriendo Listas con ZIP -> Unirlas --- Para hacerlo debemos tener los mismos datos en cada lista
for numero, animal,girl in zip(numeros,animales, nenas): #SINTAXIS
    print(f"Lista Numeros: {numero}")
    print(f"Lista Animales: {animal}")     
    print(f"Lista Nenas: {girl}")  
    
#Aqui hay una tupla, Muestra el Indice y el Valor del Indice.    
for num in enumerate(numeros): 
    print(num)    
    
#FOR con ELSE.
# # Con range le damos un parametro de inicio y final, "Recordar (12, 17) da los numeros del 12 al 16"
for num in range(12, 17): 
    print(num)
else:
    print("Fin del Bucle..")        