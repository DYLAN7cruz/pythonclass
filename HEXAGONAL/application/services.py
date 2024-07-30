from domain.ports import UserRepository
from domain.models import User
#CASOS DE USO
# Servicio que utiliza el repositorio para manejar la lógica de negocio
class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def add_user(self, name, age):
        """ Crea un usuario y lo agrega al repositorio """
        user = User(name, age)
        self.user_repository.add_user(user)

    def get_users(self):
        """ Obtiene todos los usuarios del repositorio """
        return self.user_repository.get_users()
