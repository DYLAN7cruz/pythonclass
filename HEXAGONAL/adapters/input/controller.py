from application.services import UserService
from exceptions import InvalidUserError, UserNotFoundError

# Adaptador de entrada que maneja la lógica de la aplicación y la vista
class Controller:
    def __init__(self, user_service: UserService, view):
        self.user_service = user_service
        self.view = view

    def add_user(self):
        """ Maneja la lógica para agregar un usuario """
        try:
            name, age = self.view.get_user_data()
            self.user_service.add_user(name, age)
            self.view.show_message("Usuario agregado exitosamente.")
        except InvalidUserError as e:
            self.view.show_message(f"Error: {e}")

    def show_users(self):
        """ Maneja la lógica para mostrar todos los usuarios """
        try:
            users = self.user_service.get_users()
            self.view.show_users(users)
        except UserNotFoundError as e:
            self.view.show_message(f"Error: {e}")
