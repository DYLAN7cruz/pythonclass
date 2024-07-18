
#ATRIBUTOS
class Persona():
    def __init__(self, nombre, altura, peso):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso

    def llamar(self):
        print(f"estas haciendo una llamado desde un: {self.nombre}")

    def cortar(self):
        print(f"cortaste la llamada de: {self.nombre}")

persona1 = Persona("Dylan", "160", "70")
persona1.llamar()
persona1.cortar()
          