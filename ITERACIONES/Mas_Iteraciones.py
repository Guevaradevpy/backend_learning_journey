frutas = ["Manzana", "Durazno", "Banano", "Sandia", "Melon", "Papaya"]
print(frutas)

gustos =[]

#Codigo para solo escoger una opcion
for fruta in frutas:
    if not fruta == "Manzana": 
        continue
    print(f"Me Gustan Todas las frutas menos la {fruta}")
    
#Codigo para solo mostar todo menos la opcion en IF, y en una sola linea .. CON JOIN ..

for fruta in frutas:
    if fruta != "Manzana":
        gustos.append(fruta)

print(f"Por ejemplo, me gustan: {', '.join(gustos)}") 