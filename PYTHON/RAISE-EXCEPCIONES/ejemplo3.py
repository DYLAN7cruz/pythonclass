class ExcepcionCreada(Exception):
    """Excepción personalizada para indicar que se ha ingresado texto en lugar de un número."""
    def __init__(self, mensaje, entrada):
        self.mensaje = mensaje
        self.entrada = entrada
        super().__init__(self.mensaje)
    
    def __str__(self):
        return f"{self.mensaje} -> Entrada no válida: {self.entrada}"

def obtener_edad():
    try:
        entrada = input("¿Qué edad tienes? : ")
        
        # Verificar si la entrada es un número
        if not entrada.isdigit():
            # Asegúrate de pasar ambos argumentos al crear la excepción
            raise ExcepcionCreada("Se ingresó texto en lugar de un número", entrada)
        
        edad = int(entrada)
        print(f"Tu edad es: {edad}")
        
        if edad <= 0 or edad > 80:
            raise ValueError(f"La edad {edad} no cumple con el rango requerido (1-80).")
    
    except ExcepcionCreada as ec:
        print(f"Error: {ec}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    
    else:
        print(f"Tu edad: {edad}, cumplió con el rango de edad")

# Llamar a la función para obtener la edad
obtener_edad()
