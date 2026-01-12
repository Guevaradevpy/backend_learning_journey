class Persona:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre          # público
        self._edad = edad             # protegido
        self.__salario = salario      # privado

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self._edad}, Salario: {self.__salario}"

    # método público para acceder al privado
    def get_salario(self):
        return self.__salario

    # Para moficar el atributo salario
    def set_salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print("El salario debe ser positivo.")

# Uso
persona = Persona("Lupi", 25, 3000)
print(persona.nombre)        # ✅ público
print(persona._edad)         # ⚠️ se puede, pero no deberías
# print(persona.__salario)   # ❌ Error: AttributeError

print(persona.get_salario()) # ✅ forma correcta, Si solo queremos acceder
persona.set_salario(4000)    # ✅ Aqui modificamos
print(persona.get_salario()) # ✅ Imprime nuevo valor
