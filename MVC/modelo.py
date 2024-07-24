# es la logica del la aplicacion , almaceno los datos o interactua con una base
from excepciones import UsuarioInvalidoError, UsuarioError, UsuarioNoEncontradoError

class Usuario:
    def __init__(self, nombre, edad):
        # if not nombre or edad < 0:
        #     raise UsuarioInvalidoError("Nombre no puede estar vacío y edad debe ser positiva.")
        self.nombre = nombre
        self.edad = edad

class GestionUsuarios:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)  #append es un metodo que se utiliza para add un elemento al final de una lista

    def obtener_usuarios(self):
        return self.usuarios
