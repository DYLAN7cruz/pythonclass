class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("hola, estoy hablando xde")

class Empleado(Persona):
    def __init__(self,nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

class Estudiante(Persona):
    def __init__(self,nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad
        

dylan = Empleado("dylan", 32, "ecuatoriano", "empacador", 200)

print(dylan.salario)
#print(f" el nombre es: {dylan.nombre}")
#print(dylan.edad)
#print(dylan.nacionalidad)

        
