lista = ["Lupi", 22, "Esteban"]
numeros = [12,24,75,89]
nombre = "Jorge Guevara"

#Metodos de lista.

#LEN, Para variables o listas, CUENTA LOS CADA CARACTER.
lento = len(nombre) 
# Guarda, Agrega un Valor -> lista.append((APODO, EDAD, APELLIDO))
lista.append("Rodriguez") 
#Se agrega un elemento en un indice especifico
lista.insert(2, "Bamdi")  
#Agrega elementos a la lista, Ej: I,N,G,E,N,I,E,R,O
lista.extend(["Ingeniero", "Bilingue"]) 
#Elimina elemento dado por indice, eliminando hacia atras es con menos -1 -2 etc.
lista.pop(0) 
#Elimina tal cual el valor que le asignemos
lista.remove(22) 
#Elimina todo
lista.clear() 
#Parametro que ordena al reves, y este metodo es solo para listas
#lista.sort(reverse=true) 

#Ordena de Mayor a Menor
lista.reverse() 

print(lista)
