class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad


class Empleado(Persona):
    pass

dylan = Persona("dylan", 32, "ecuatoriano")

print(f" el nombre es: {dylan.nombre}")
print(dylan.edad)
print(dylan.nacionalidad)

        
