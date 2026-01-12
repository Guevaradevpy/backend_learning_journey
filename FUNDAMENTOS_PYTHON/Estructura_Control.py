# Valor de cambio
tasa_cop_usd = 4000

#definimos operacion de cop to usd
def cop_usd(cop):
    print("convertire COP a USD")
    return cop / tasa_cop_usd

#definimos operacion de cop to usd
def usd_cop(usd):   
    print("convertire de USD a COP")
    return usd * tasa_cop_usd

#MENU
while True:
    print(" --Conversor de Monedas-- ")
    print("1: Convertir de pesos colombianos a dólares")
    print("2: Convertir de dólares a pesos colombianos")
    print("3: Salir")
    
    #Manejo de Errores
    try:
        opcion = int(input("Ingresa opcion: "))
        if opcion == 1:
            try:
                colombia = int(input("Ingresa valor en COP: "))
                conver1 = cop_usd(colombia)
                print(f"{colombia} COP son {conver1:.2f} USD")                    
            except ZeroDivisionError:
                print("Ingresa un valor diferente a 0")
    
        elif opcion == 2:
            try:
                dolares = int(input("Ingresa el valor en USD:  "))
                conver2 = usd_cop(dolares)
                print(f"{dolares} USD son {conver2:.2f} COP")
            except ZeroDivisionError:
                print("Ingresa un valor diferente a 0")
        
        elif opcion == 3:
            print("Hasta Luego")
            break
        
        else:
            print("Ingresa opcion valida")
        
    except ValueError:    
        print("Ingresa solo Numeros")
        
        
#Operador WALRUS.
a = [1, 2, 3]
if (n := len(a)) < 10:
    print(f"Tiene pocos elementos: {n}")        
    
    
    
# Match -> Similar al (IF,ELIF,ELSE)
hora = 8
match hora:
    case 8:
        print("Desayuno")
    case 14:
        print("Comida")
    case 21:
        print("Cena")
    case _:
        print("No toca comer")    
        
#Match, Donde | es como OR.
mes = 4
match mes:
    case 12 | 1 | 2: print("Invierno")
    case 3 | 4 | 5: print("Primavera")
    case 6 | 7 | 8: print("Verano")
    case 9 | 10 | 11: print("Otoño")
    case _: print("Error")        
        