#Tener en cuenta Jerarquia todo va de Arriba hacia Abajo.
#Si la clase D hereda de clase F, F debe de estar arriba de D.

class A:
    def hablar(self):
        print("Hablo desde A")
        
class F:
    def hablar(self):
        print("Hablo desde F")                        
                
class B(A):
    def hablar(self):
        print("Hablo desde C")
           
class C(B, A):
    def hablar(self):
        print("Hablo desde C")

class D(F):
    def hablar(self):
        print("Hablo desde D")

class E(C):
    def hablar(self):
        print("Hablo desde E")
        
a = A()
a.hablar() 

#Paso a Paso de como se ejecutan las clases
print(D.mro())