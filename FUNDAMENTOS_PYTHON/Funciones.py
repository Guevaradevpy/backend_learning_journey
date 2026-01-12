#Conteo de Palabras ... 
def contar_palabras(texto):
    palabras = texto.lower().split() # Todo en Minuscula y Quitando espacios y los crea a lista.
    contador = {} 
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1 #SI YA EXISTE LE SUMA UNA
        else:
            contador[palabra] = 1 # SI NO LA CREA Y GUARDA
    return contador

# Prueba
print(contar_palabras("Hola hola mundo mundo mundo")) #ESTA ES LA PRUEBA DEl EJERCICIO .
# Output: {'hola': 2, 'mundo': 3}

def pares(lista):
    suma = 0 # Contador
    for n in lista:
        if n %2 == 0:
            suma += n    
    return suma        

par = pares([2,3,43,56,76]) #En parentesis para poderla invocar.
print(f"La suma de los numeros pares es: {par}")

#Variable Tradicional.
def saludar(nombre):
    print("Hola Como estas, " + nombre)
saludar("Jorge")
saludar("Mario")

def palabras(texto):
    palabras = texto.lower().split() 
    return palabras
print(palabras("Lupi Sos Un Bandido"))       

def suma(a,b):
    return a + b
resultado = suma(3,4)
print(resultado)

def es_mayor_de_edad(edad):
    if edad >= 18:
        return "Eres mayor de edad"
    else:
        return "Eres menor de edad"
 
resultado = es_mayor_de_edad(15)
print(resultado)

resultado = es_mayor_de_edad(19)
print(resultado)

#OTROS EJEMPLOS

# Una opcion mas moderna con pocas lineas.. mas elegante
def numeros_pares(lista):
    return sum(n for n in lista if n % 2 == 0)

def numeros_impares(lista):
    return sum(n for n in lista if n % 2 != 0)
    
numeros = [2, 44, 56, 21, 13, 72, 73]
print(f"La suma de los numeros pares es: {numeros_pares(numeros)}")
print(f"La suma de los numeros inpares es: {numeros_impares(numeros)}")

# Vemos en una sola linea pueden haber dos variables .. 
def sumar_pares_impares(lista):
    suma_p, suma_i = 0, 0
    for n in lista:
        if n % 2 == 0:
            suma_p += n
        else:
            suma_i += n
    return suma_p, suma_i

numeros = [2, 44, 56, 21, 13, 72, 73]
pares, impares = sumar_pares_impares(numeros)
print(f"La suma de los pares es: {pares}")
print(f"La suma de los impares es: {impares}")

def muestra_p(lista):
    for n in lista:
        if n %2 == 0:
            print(n)
muestra_p ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

o = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(o)

def pir(lista):
    pares = [] # Lista vacia para guardar valores reales
    for n in lista:
        if n %2 == 0:
            pares.append(n)   # => Para guardar cada dato que cumple con la condicion.
    return pares         
look = pir([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Los numeros pares son: ", look)

def palindromo(texto):
    text = texto.lower().split()
    # 2) Filtrar: quedarnos solo con letras y números
    limpio = "".join(ch for ch in texto if ch.isalnum())
    # 3) Comparar con su inverso
    return limpio == limpio[::-1]

print(palindromo("radar"))

def cuadrado(n):
    return n ** 2
print(cuadrado(4))

#Con un INPUT.
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

num = int(input("Ingresa un número: "))
print(es_par(num))

# Un poco dificil pero no pienso en rendirme nunca, lo logro por que lo logro --- 