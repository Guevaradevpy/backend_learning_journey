# Definimos dos cadenas de texto
cadena1 = "Millonario Mundial"
cadena2 = "Lupi "

# Concatenamos las dos cadenas → "Lupi Millonario Mundial"
exito = cadena2 + cadena1

# dir(cadena1) nos muestra todos los métodos y atributos disponibles para strings en Python
print(dir(cadena1))

# Métodos comunes de strings:

# print(exito.upper())       # Convierte todo a MAYÚSCULAS
# print(exito.lower())       # Convierte todo a minúsculas
# print(exito.capitalize())  # Solo la primera letra en mayúscula

# print(cadena1.find("Millonario"))  # Devuelve la posición de la palabra, o -1 si no está
# print(cadena1.index("M"))          # Igual que find, pero si no encuentra → ERROR

# print(cadena1.isnumeric())  # True si SOLO tiene números, si no → False
# print(cadena1.isalpha())    # True si SOLO tiene letras (sin espacios ni números)

# print(cadena1.count("i"))   # Cuenta cuántas veces aparece un carácter

# print(cadena1.endswith("o"))   # Verifica si termina en "o"
# print(cadena1.startswith("M")) # Verifica si inicia con "M"

# print(cadena1.replace("rio", "ria"))  # Reemplaza parte del texto

# print(cadena1.split())  # Convierte la cadena en lista (separa por espacios)



