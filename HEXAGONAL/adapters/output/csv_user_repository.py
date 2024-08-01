import csv
from domain.ports import UserRepository
from domain.models import User

# Adaptador de salida que interactúa con un archivo CSV
class CSVUserRepository(UserRepository):
    def __init__(self, file_path):
        self.file_path = file_path    # aqui se almacenaran los datos del usuario
        self._initialize_file()    # verifica que el archivo existe y tiene el fomrato correcto

    def _initialize_file(self):
        """ Inicializa el archivo CSV si no existe """
        try:
            with open(self.file_path, mode='r', newline='') as file: # 
                pass  # El archivo ya existe, no se necesita hacer nada
        except FileNotFoundError:
            # Si el archivo no existe, lo crea con los encabezados
            with open(self.file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Age'])  # Escribe los encabezados en el archivo

    def add_user(self, user: User):
        """ Agrega un usuario al archivo CSV """
        with open(self.file_path, mode='a', newline='') as file:   # el a, hace referencia a que permite add datos, sin escribirlo en el archivo
            writer = csv.writer(file)
            writer.writerow([user.name, user.age])  # Escribe los datos del usuario en una nueva fila

    def get_users(self):
        """ Obtiene todos los usuarios del archivo CSV """
        users = []
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Salta el encabezado
            for row in reader:
                name, age = row
                users.append(User(name, int(age)))  # Crea un objeto User y lo agrega a la lista
        return users



#crear un repositorio(adpater) que utilice un texto plano (csv) para add y obtener usuarios
# de donde voy a meter y sacar datos
# meter y sacar usuarios en csv