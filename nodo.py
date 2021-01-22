class Nodo:
    def __init__(self,value):
        #valor inicial del nodo
        self.dato = value
        #no hay nodo siguiente
        self.siguiente = None

    #obtengo el nodo se creo al inicio
    def obtenerDato(self):
        return self.dato

    #obtengo el valor siguiente
    def obtenerSiguiente(self):
        return self.siguiente

    #y le asigno ese nuevo nodo a la lista
    def asignarDatos(self,Nuevodato):
        self.dato = Nuevodato

    #y paso al siguiente para asignarlo
    def asignarSiguiente(self,Nuevosiguiente):
        self.siguiente = Nuevosiguiente


temp = Nodo(93)
temp.obtenerDato()
print(temp)


