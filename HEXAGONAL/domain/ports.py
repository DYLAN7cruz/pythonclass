from abc import ABC, abstractmethod

# Puerto de salida (interfaz) para el repositorio de usuarios
class UserRepository(ABC):
    @abstractmethod
    def add_user(self, user):
        """ Método abstracto para agregar un usuario al repositorio """
        pass

    @abstractmethod
    def get_users(self):
        """ Método abstracto para obtener todos los usuarios del repositorio """
        pass
