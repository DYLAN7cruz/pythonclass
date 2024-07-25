# main.py
from controlador import Controlador

def main():
    controlador = Controlador()
    while True:
        print("\n1. Agregar usuario")
        print("2. Mostrar usuarios")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        try:
            if opcion == "1":
                controlador.agregar_usuario()
            elif opcion == "2":
                controlador.mostrar_usuarios()
            elif opcion == "3":
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()


# arquitectura hexagonal.
# como usar las excepciones en una arquitectura hexagonal.
