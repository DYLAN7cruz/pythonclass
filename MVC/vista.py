# view.py
from excepciones import UsuarioInvalidoError

class Vista:
    def mostrar_usuarios(self, usuarios):
        if not usuarios:
            print("No hay usuarios registrados.")
        else:
            print("Lista de usuarios:")
            for usuario in usuarios:
                print(f"Nombre: {usuario.nombre}, Edad: {usuario.edad}")

    def obtener_datos_usuario(self):
        try:
            nombre = input("Ingrese el nombre del usuario: ")
            edad = int(input("Ingrese la edad del usuario: "))
            if not nombre or edad < 0:
                raise UsuarioInvalidoError("Nombre no puede estar vacío y edad debe ser positivaaaaaaaaaaa.")
            return nombre, edad
        except ValueError:
            raise UsuarioInvalidoError("Edad debe ser un número entero.")
    

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
