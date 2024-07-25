# Las excepciones son un mecanismo que permite gestionar errores y situaciones
# inesperadas de manera controlada durante la ejecución de un programa. En lugar de detener el programa 
# cuando ocurre un error, el manejo de excepciones permite "atrapar" estos errores y ejecutar código especial para manejarlos.


# try :  codigo que puede generar una excepcion, o que tenga errores 
try:
    numero = int(input("INGRESA UN NUMERO CUALQUIERA: "))
    resultado = 50 // numero
    print(f"50 / {numero} = ", resultado)


# except:  codigo para maanejar la excepcion
except ValueError as ve:
    print(f"Se debe ingresar numeros enteros y no letras - ERROR PY - {ve}")


except ZeroDivisionError as zde:
    print(f"No se puede dividir para cero - ERROR PY - {zde} ")


except Exception as e:
    print(f"Operacion no valida : {e}")


# else : este codigo se ejecuta cunado no hay excepciones
else:
    print(f"else: - Operacion exitosa, el resultado es : {resultado}")
    

# finally se ejecuta siempre sin importar que el progarmas este bien o con errores
finally:
    print("finally - Fin del programa")

# ----------------------------------------------------------------------------------------------------------------   

# raise 
# excepciones personalizadas

# arquitectura hexagonal 

# mvc:  crear un modelo vista controlador, pequeño ejemplo, todo orientado a objetos, sin ningun framwork, sql lite
# investigar pip, libreria de python