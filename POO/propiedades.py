# propiedades son property, que quieren decir que nos permite definir setteres y getteres

  # cuando se pone _ en python quiere decir que es privado y cunado estan dos __ es que es muy privado

# los getteres y setteres son metodos que se ultilizan para acceder a propiedade
#privadas que tiene python
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre # el _ es que es privado,
        self._edad  = edad


    @property   # es un decorador reservado
    def get_nombre(self):   # el get es para acceder a la propiedad privada en este caso el nombre
        return self._nombre
    

    @get_nombre.setter
    def get_nombre(self, new_nombre): # con los setteres modificamos la propiedad v
        self._nombre = new_nombre

    @get_nombre.deleter
    def get_nombre(self): # con los setteres modificamos la propiedad v
        del self._nombre

    
dylan = Persona("dylan", 19)

nombre = dylan.get_nombre    # no hace falta usar los dos () , en el get_nombre, porque ya estamos usando @property
print(nombre)

nombre = dylan = "juan xde"    # modificamos el nombre gracias a los setteres
print(nombre)



