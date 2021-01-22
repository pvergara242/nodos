from nodo import Nodo

class listaEnlazada:
    def __init__(self):
        #la cabeza se refiere al primer nodo de la lista
        self.cabeza = None

    #comprueba si la cabeza de la lista es una referencia a None
    def estaVacia(self):
        return self.cabeza == None


    def agregar(self, item):
        #crea un nuevo nodo
        temp = Nodo(item)
        #cambia la referencia siguiente del nuevo nodo
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp
        return temp


    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()

        return contador

    def buscar(self, item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()

        return encontrado

    def remover(self, item):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()

        if previo == None:
            self.cabeza = actual.obtenerSiguiente()
        else:
            previo.asignarSiguiente(actual.obtenerSiguiente())




milista = listaEnlazada()
print(milista.agregar(31))
print(milista.agregar(77))
print(milista.agregar(17))
print(milista.agregar(93))
print(milista.agregar(26))
print(milista.agregar(54))

print(milista)
print(milista.buscar(17))
print(milista.remover(17))







