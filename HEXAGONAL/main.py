from adapters.output.memory_user_repository import MemoryUserRepository
from adapters.output.csv_user_repository import CSVUserRepository
from application.services import UserService
from adapters.input.view import View
from adapters.input.controller import Controller

# Inicialización de los componentes
file_path = 'HEXAGONAL/adapters/output/users.csv'  # Ruta del archivo CSV
repository = CSVUserRepository(file_path)
service = UserService(repository)
repository = MemoryUserRepository()
view = View(None)  # Inicializa la vista con controlador después
controller = Controller(service, view)
view.controller = controller  # Establece el controlador en la vista

# Ejemplo de uso
while True:
    print("\nOptions:")
    print("1. Add user")
    print("2. Show users")
    print("3. Exit")

    option = input("Select an option: ")

    if option == '1':
        controller.add_user()
    elif option == '2':
        controller.show_users()
    elif option == '3':
        break
    else:
        print("Invalid option. Try again.")




