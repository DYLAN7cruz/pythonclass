

try:
    edad = int(input("que edad tienes ? : "))
    print(f"Tu edad es: {edad}")

    if edad <= 0 or edad > 80:
        raise ValueError(f"la edad {edad}, no cumple con el rango requerido :)")
    

    

except ValueError as va:
    print(f"{va}")
    print("funciono la excepcion personalizada")

else:
    print(f"tu edad: {edad}, cumplio con el rango de edad")