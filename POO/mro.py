#MRO ES EL METODO DE RESOLUCION DE ORDEN EN PYTHON
#EL ORDEN EN EL QUE PYTHON BUSCA METODOS Y ATRIBUTOS

class A:
    def hablar(self):
        print("hola desde A")

class F(A):
    def hablar(self):
        print("hola desde F")

class B(A):
    def hablar(self):
        print("hola desde B")

class C(A):
    def hablar(self):
        print("hola desde C")

class D(B,C):
    def hablar(self): 
        print("hola desde D")

d = D()


d.hablar()
F.hablar(d)