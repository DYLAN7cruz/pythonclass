
class Gato():
    def sonido(self):#METODO-
        return "MIAUUUUU"     #-
                                #----tienen el mismo metodo, por eso es polimorfismo
class Perro():                #-
    def sonido(self):#METODO-
        return "GUAUUUUU"
    
def hacer_sonido(animal):
    print(animal.sonido())
    

perro = Perro()
gato = Gato()

print(gato.sonido())

hacer_sonido(perro)