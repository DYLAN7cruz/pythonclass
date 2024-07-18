class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("hola, estoy hablando xde")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return(f"mi habilidad es ser: {self.habilidad}")
        
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    

    def presentarse(self):
        print (f'Hola, yo soy {self.nombre},  {self.mostrar_habilidad()} y trabajo en {self.empresa}')


#dylan = Empleado("dylan", 32, "ecuatoriano", "empacador", 200)
empleado = EmpleadoArtista("dylan", 32, "ecuatoriano", "disciplinado", 2000, "tepcol")
#print(empleado.empresa)
empleado.presentarse()

        
