class ExcepcionCreada(Exception):
    """Excepción personalizada para indicar que se ha ingresado texto en lugar de un número."""
    pass

try:
    entrada = input("¿Qué edad tienes? : ")

    # Verificar si la entrada es un número
    if not entrada.isdigit():
        raise ExcepcionCreada(f"Se ingresó texto en lugar de un número: {entrada}")

    edad = int(entrada)
    print(f"Tu edad es: {edad}")

    if edad <= 0 or edad > 80:
        raise ValueError(f"La edad {edad} no cumple con el rango requerido :)")

except ExcepcionCreada as te:
    print(f"{te}")
    print("Funcionó la excepción personalizada para texto ingresado")

except ValueError as va:
    print(f"{va}")
    print("Funcionó la excepción personalizada para rango de edad")

else:
    print(f"Tu edad: {edad}, cumplió con el rango de edad")
