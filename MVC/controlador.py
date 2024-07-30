# controller.py
from modelo import Usuario, GestionUsuarios
from vista import Vista
from excepciones import UsuarioInvalidoError, UsuarioNoEncontradoError
  
class Controlador:
    def __init__(self):
        self.modelo = GestionUsuarios()
        self.vista = Vista()

    def agregar_usuario(self):
        try:
            nombre, edad = self.vista.obtener_datos_usuario()
            usuario = Usuario(nombre, edad)
            self.modelo.agregar_usuario(usuario)
            self.vista.mostrar_mensaje("Usuario agregado exitosamente.")
        except UsuarioInvalidoError as e:
            self.vista.mostrar_mensaje(f"Error: {e}")


    def mostrar_usuarios(self):
        try:
            usuarios = self.modelo.obtener_usuarios()
            self.vista.mostrar_usuarios(usuarios)
        except UsuarioNoEncontradoError as e:
            self.vista.mostrar_mensaje(f"Error: {e}")

            
