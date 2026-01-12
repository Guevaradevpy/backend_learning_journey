# Creando conjunto con SET
conjunto = set(['Dalto', 'Gay'])

conjunto1 = frozenset(["Dato1", "Dato2"])
conjunto2 = {conjunto1, "Dato3"}

print(conjunto2)

#Ejemplo de set, para no repetidos.
nombres = ["Lupi", "Lupi", "Juan", "Pedro", "Pedro"]
sin_repetidos = set(nombres)

print(sin_repetidos)

#Para mutar un String
nombre = "Lupi"
nuevo = "X" + nombre[1:]
print(nuevo)  # Xupi


#Teoria de Conjuntos
conjun1 = {1, 3, 5, 7}
conjun2 = {2, 4, 6, 8}

resultado = conjun2.issubset(conjun1)
# resultado = conjun2 <= conjun1 .... > IsSuperSet, <= IsSubSet.

#Para mirar si son distintos, Si lo son Devuelve True. "Nada puede ser igual"
resultado = conjun2.isdisjoint(conjun1) 
print(resultado)



#DESEMPAQUETADO
datos_tupla = ("Jorge", "Guevara", "21") # << Es un tupla, tambien funciona con Listas.
datos_lista =  ["Lupi", "Bandido", "22"]
NombreL, ApellidoL, EdadL = datos_lista
NombreT, ApellidoT, EdadT = datos_tupla
print(NombreL) #
print(NombreT)

#Desempaquetado de solo una lista normal en FOR
datos_tupla = ("Kawasaki", "2024", "H2R", "50000")
Empresa, Modelo, Referencia, Precio = datos_tupla

for moto in datos_tupla:
    print(moto)
    
Motos = [
    ("Kawasaki", "2024", "H2R", "50000"),
    ("Yamaha", "2022", "R1", "40000")
]

for Empresa, Modelo, Referencia, Precio in Motos:
    print(f"Empresa: {Empresa} - Modelo: {Modelo} - Ref: {Referencia} - Precio: {Precio}")



    
#DICCIONARIOS
#Creando Diccionario con DICT()
diccionario = dict(Nombre = "Jorge", Apellido = "Guevara")

#Las listas no pueden ser claves y usamos fronzenset para meter conjuntos
dicci = {frozenset(["Dalto", "chupon"]) : "JaJaJa"}

#Creando diccionario con fromkeys()
dicc = dict.fromkeys(["Nombre", "Apellido"], "Lupi")

print(dicc["Apellido"]) # Aqui nos va a mostrar el valor de apellido
print(dicc) # Imprime clave y valor
    