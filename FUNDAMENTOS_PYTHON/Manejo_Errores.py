# SINTAXIS 
try:
    edad= int(input("Ingresa tu edad: "))
    
    if 0 < edad and edad > 130:
        print("Edad no validad")
    else:
        print(f"Edad registrada {edad} años")
    
except ValueError:
    print("⚠️ Ingresa solo números.")
    
try:
    num1 = int(input("Ingresa un número: "))
    num2 = int(input("Ingresa otro número: "))
    print(f"El resultado de tu división es: {num1 / num2}")

#MANEJO DE CEROS
except ZeroDivisionError:
    print("No se puede dividir entre 0.")
#MANEJO NORMAL DE ERRORES
except ValueError:
    print("Debes ingresar números válidos.")
    
    
#Aqui estamos trabajando con errores de archivos.
while True:
    try:
        nombre = input("Ingresa el nombre del archivo: ")
        with open(nombre, "r") as archivo:  # abre en modo lectura
            contenido = archivo.read()
        print("\n--- Contenido del archivo ---")
        print(contenido)
        break  # Si todo va bien, salimos del bucle
    except FileNotFoundError:
        print("❌ Archivo no encontrado. Verifica el nombre e inténtalo otra vez.")
    except Exception as e:
        print(f"⚠️ Ocurrió un error inesperado: {e}")

    
#try: “Intenta ejecutar este código… puede fallar”.
#except: “Si falla, atrapo el error y lo manejo”.
#raise: “Lanza un error a propósito si ocurre algo que no quiero permitir”.