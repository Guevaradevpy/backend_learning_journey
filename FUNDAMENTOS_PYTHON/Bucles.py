# Un bucle sirve para repetir lógica sin copiar código.
# BUCLE While.
#Imprime del 1 al 10 menos el 6.
contador = 1
while contador <= 10:
    if contador != 6:
        print(contador)
    contador +=1         

#Adivinar el numero hasta que sea el correcto. Bucle while.
print("🎲 Adivina el número del 1 al 10")
num_secreto = 5

while True:
    try:
        adivinar = int(input("Ingresa un número: "))
        
        # Validar rango
        if adivinar < 1 or adivinar > 10:
            print("Debe ser un número entre 1 y 10")
            continue

        # Comparar con el secreto
        if adivinar == num_secreto:
            print("¡HAZ ADIVINADO!")
            break
        else:
            print("INCORRECTO, intenta de nuevo.")
    
    except ValueError:
        print("Eso no es un número válido.")


#introducir una opcion.

while True:
    print("1. Saludar")
    print("2. Decir Edad")
    print("3. Salir")
    
    try:
        opcion = int(input("Ingresa una opción: "))
    except ValueError:
        print("⚠️ Ingresa solo números.")
        continue

    if opcion == 1:
        print("👋 ¡Hola Lupi!")
    elif opcion == 2:
        print("🎂 Tienes 23 años")
    elif opcion == 3:
        print("👋 ¡Hasta luego!")
        break
    else:
        print("❌ Opción no válida.")
    
    repetir = input("DESEAS VOLVER A PROBAR EL MENU? SI/NO. ").upper()
    if repetir != "SI":
        print("Hasta la Proxima")    
    break


contar = 2
suma = 0
while contar <= 20:
    suma += contar
    contar += 2
print("La suma de los pares del 2 al 20 es:", suma)

contar = 2
suma = []
while contar <= 20:
    suma.append(contar)
    contar += 2
print(f"Los multiplos de 2 hasta el 20 son: {suma}")

#BUSCAR ELEMENTOS (FOR con ELSE)
def encuentra(lista, busca):
    for l in lista:
        if l == busca:
            print(f"{busca} se encontró")
            break
    else:
        print(f"{busca} NO se encontró")
            
N = [1,2,3,4,5,6]
encuentra(N, 3)
encuentra(N, 7)            