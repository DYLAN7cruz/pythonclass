# una clase abstracta , es una clase que no se puede instanciar

from abc import ABC, abstractclassmethod   # es una decorador que nos permite usar un metodo abstracto

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre}, y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre,edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"actualemnte estoy estudiando: {self.actividad}")

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre,edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"actualmente yo soy : {self.actividad}")


dylan = Estudiante("dylan", 23, "masculino", "desarrollo de software")

erick = Trabajador("erick", 13, "masculino", "vago")

dylan.presentarse()
dylan.hacer_actividad()
erick.presentarse()
erick.hacer_actividad()