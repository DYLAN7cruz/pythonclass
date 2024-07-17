class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Mi nombre es: {self.nombre}, y mi edad es: {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self):
        print(f"{super().mostrar_datos()}, mi grado es: {self.grado}")

persona1 = Estudiante("dylan", 23, "10mo")

persona1.mostrar_grado()