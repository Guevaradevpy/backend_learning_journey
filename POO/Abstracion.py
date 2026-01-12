class Auto():
    #Siempre va a iniciar apagado
    def __init__(self):
        self._estado = "Apagado"
    
    #Metodo para encenderlo    
    def encender(self):
        self._estado = "Encendido"
        print("El auto esta encendido")
    
    #Comprueba que este apagado, lo enciende, y lo conduce.        
    def conducir(self):
        if self._estado == "Apagado":
            self.encender()
        print("Conduciendo el auto")        
        
auto = Auto()
auto.conducir()        
#auto.encender()