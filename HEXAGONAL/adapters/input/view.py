from exceptions import InvalidUserError

# Adaptador de entrada que maneja la interfaz con el usuario
class View:
    def __init__(self, controller):
        self.controller = controller  # El controlador que maneja la lógica

    def show_users(self, users):
        """ Muestra todos los usuarios """
        if not users:
            print("No hay usuarios registrados.")
        else:
            print("Lista de usuarios:")
            for user in users:
                print(f"Name: {user.name}, Age: {user.age}")

    def get_user_data(self):
        """ Obtiene los datos del usuario desde la entrada del usuario """
        try:
            name = input("Enter the user's name: ")
            age = int(input("Enter the user's age: "))
            if not name or age < 0:
                raise InvalidUserError("Nombre no puede estar vacío y edad debe ser positivaaaaaaaaaaa.")
            return name, age
        except ValueError:
            raise InvalidUserError("Edad debe ser un número entero.")
    
    def show_message(self, message):
        """ Muestra un mensaje en la consola """
        print(message)
