JEFES = {"patron8491", "lupillo00"}

while True:
    nombre = input("Dame tu nombre (o 'salir'): ").strip().lower()

    if nombre == "salir":
        print("Hasta la proxima.")
        break

    if nombre in JEFES:
        print(f"Bienvenido, jefe {nombre.title()}. Acceso inmediato. A disfrutar de las putas")
        continue

    # Edad
    try:
        edad = int(input("Dame tu edad: ").strip())
    except ValueError:
        print("La edad debe ser un número.")
        continue
    
    # Validación de edad
    if edad < 18:
        print(f"Lo siento {nombre.title()}, eres menor de edad.")
        continue    
    
    # Cédula
    cc = input("Dame tu número de identificación: ").strip()

    # Debe ser numérica
    if not cc.isdigit():
        print("La identificación debe ser numérica.")
        continue

    # Debe tener entre 6 y 10 dígitos
    if not (6 <= len(cc) <= 10):
        print("Identificación inválida. Debe tener entre 6 y 10 dígitos.")
        continue

    print(f"Hola {nombre.title()}, puedes ingresar. Disfruta de las putas.")

    continuar = input("Deseas continuar? SI/NO: ").strip().upper()
    if continuar == "NO":
        print("Muchas Gracias! Somos Burdel 74")
        break
