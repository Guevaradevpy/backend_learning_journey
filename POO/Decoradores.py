#ANTES DURANTE Y DESPUES, Asi funciona.
def sumar(func):
    def suma(a, b):
        print(f"Sumando {a} + {b}")
        resultado = func(a, b)
        print(f"Resultado = {resultado}")
        return resultado
    return suma

@sumar
def operacion(a, b):
    print("Realizando .....")
    return a + b

operacion(7, 5)

#Otro Ejercicio
def mayusculas(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)   
        return resultado.upper()            
    return wrapper

@mayusculas
def saludar(nombre):
    return f"Hola {nombre}"

print(saludar("Lupi"))   


def resta(funcion):
    def rest(a,b):
        print(f"La resta es: {a} - {b}.")
        resultado = funcion(a, b)
        print(f"Resultado: {resultado}")
        return resultado
    return rest    
    
@resta
def operacion(a, b):
    print("Realizando....")
    return a - b

x = int(input("Ingresa el primer número: "))
y = int(input("Ingresa el segundo número: "))

operacion(x,y)

#*args **kwargs
# def ejemplo(*args, **kwargs):
#     print("args =", args)
#     print("kwargs =", kwargs)

# ejemplo(1, 2, 3, nombre="Lupi", edad=21)
# 👉 args = (1, 2, 3) #Convierte en tupla
# 👉 kwargs = {'nombre': 'Lupi', 'edad': 21} #Convierte en diccionario