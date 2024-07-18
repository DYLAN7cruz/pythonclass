# los deocradores coge una funcion y le agrega funcionalidad, antes o despues de ejecutarla.


def decorador(funcion): # creamos una funcion llamada decorador, que nos pide como parametro funcion
    def funcion_modificada():
        print("antes de llamar a la funcion")
        funcion() # ejecutamos la funcion
        print("despues de la funcion xde")
    return funcion_modificada

# def saludo():
#     print("aqui llamamos la funcion decorador, por eso se pone entre los dos prints")
#     print("HOLA DYLANXDE")

# saludo_modificado = decorador(saludo)  #saludo_modificado es una variable
# saludo_modificado()


@decorador   # este es el decorador de la funcion que creamos
def saludo():
    print("holaaa dylan xde")

saludo()