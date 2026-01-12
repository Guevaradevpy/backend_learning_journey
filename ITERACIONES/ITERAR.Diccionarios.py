datos = {
    "Nombre" : "Jorge",
    "Apellido" : "Guevara",
    "Edad" : 22,
    "Cargo" : "Patron"   
}

#Mostar solo claves.
for n in datos.keys():
    print(n)

#Mostrar solo valores
for n in datos.values():
    print(n)
print()
    
#Mostar claves y valores con un desempaquetado.    
for key, values in datos.items():
    print(f"Dato: {key} | Valor: {values}")
print()    

#TU EJERCICIO ..
estudiantes = {
    "Ana": 4.5,
    "Pedro": 1.0,
    "Laura": 4.2,
    "Carlos": 2.9,
    "Lucía": 3.5
}

promedio_total = 0
superior_cuatro = 0

for nombre, notas in estudiantes.items():
    print(f"{nombre} tiene un promedio de: {notas}")
    promedio_total += notas
    if notas > 4.0:   
        superior_cuatro += 1

cantidad_estudiantes = len(estudiantes)
promedio_general = promedio_total / cantidad_estudiantes

print(f"\nEl Promedio Total del Grupo es: {promedio_general:.2f}")
print(f"Cantidad de estudiantes con promedio superior a 4.0 es: {superior_cuatro}")

#Otra forma de desempaqueatdo
frutas = ["🍎", "🍌", "🍇", "🍍"]

manzana, banano, uvas, piña = frutas

print(manzana)
print(banano)
print(uvas)
print(piña)

#Con resto (*) llamar lo demas
print()
frutas = ["🍎", "🍌", "🍇", "🍍", "🥭", "🍑"]
manzana, banana, *otras = frutas

print(manzana)
print(banana)
print(otras) 
    