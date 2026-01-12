class Cuenta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        
    def depositar(self, monto):
        if monto <= 0:
            return "Monto Invalido" 
        self.saldo += monto   
        return f"Deposito Exitoso! | Saldo: {self.saldo}"
    
    def retirar(self, monto):
        if monto <= 0:
            return "Monto Invalido"
        
        if monto > self.saldo:
            return "Fondos Insuficientes"
        
        self.saldo -= monto
        return f"Retiro Exitoso de {monto}"
    
    def mostrar_saldo(self):
        return f"Titular: {self. titular} | Saldo: {self.saldo}"
    
c1 = Cuenta("Lupi")    
print(c1.depositar(2200))
print(c1.retirar(400))
print(c1.mostrar_saldo())