# es la logica del la aplicacion , almaceno los datos o interactua con una base

class Usuario:
    def __init__(self, nombre, edad):
       
        self.nombre = nombre
        self.edad = edad

class GestionUsuarios:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)  #append es un metodo que se utiliza para add un elemento al final de una lista

    def obtener_usuarios(self):
        return self.usuarios
