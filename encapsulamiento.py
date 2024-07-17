  # cuando se pone _ en python quiere decir que es privado y cunado estan dos __ es que es muy privado

# los getteres y setteres son metodos que se ultilizan para acceder a propiedade
#privadas que tiene python
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre # el _ es que es privado,
        self._edad  = edad

    def get_nombre(self):   # el get es para acceder a la propiedad privada en este caso el nombre
        return self._nombre
    
    def set_nombre(self, new_nombre):   # el set es para definir
        self._nombre = new_nombre





    
dylan = Persona("dylan", 19)

nombre = dylan.get_nombre()
print(nombre)

dylan.set_nombre("pepeeeee xde")

nombre = dylan.get_nombre()
print(nombre)

