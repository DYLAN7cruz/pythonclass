from domain.ports import UserRepository
from domain.models import User
#ADAPTADOR DE SALIDA: interactua con compenente externos
# Implementación en memoria del repositorio de usuarios
class MemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = []  # Lista en memoria para almacenar usuarios

    def add_user(self, user: User):
        """ Agrega un usuario a la lista en memoria """
        self.users.append(user)

    def get_users(self):
        """ Obtiene todos los usuarios de la lista en memoria """
        return self.users
