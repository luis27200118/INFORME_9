"""Lista circular:
-Agregar ultimo
- Eliminar ultimo.
- Lista Vacía
- Agregar Inicio
- Eliminar Inicio
- Mostrar Lista"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig  = None
    
class ListaCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def agregarInicio(self, dato):
        if len(self) == 0:
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.sig = self.primero
        else:
            aux = Nodo(dato)
            aux.sig = self.primero
            self.primero = aux
            self.ultimo.sig = self.primero
    
    def agregarUltimo(self, dato):
        if len(self) == 0:
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.sig = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.sig = Nodo(dato)
            self.ultimo.sig = self.primero
    
    def buscarNodo(self, dato):
        aux = self.primero
        existe = False
        while aux:
            if aux.dato == dato:
                existe = True
                break
            
            aux = aux.sig
            if aux.sig == self.primero.sig:
                break
        return existe
    
    def reemplazarNodo(self, datoAnt, newData):
        if self.buscarNodo(datoAnt):
            aux = self.primero 
            while aux:
                if aux.dato == datoAnt:
                    aux.dato = newData
                    break
                aux = aux.sig
                if aux.sig == self.primero.sig:
                    break
        else:
            raise Exception ("El dato a reemplazar no existe en la lista")
    
    def eliminarNodo(self, dato):
        if self.buscarNodo(dato):
            actual   = self.primero
            anterior = self.primero
            while actual:
                if len(self) == 1:
                    self.primero = None
                    self.ultimo.sig = self.primero
                    break
                if actual.dato == dato:
                    if actual == self.primero:
                        self.primero = self.primero.sig
                        self.ultimo.sig = self.primero
                        
                    else:
                        anterior.sig = actual.sig
                    return
                anterior = actual
                actual = actual.sig
        else:
            raise Exception ("El Nodo no puede se eliminado por tratarse de un dato inexistente.")
    def eliminarPrimero(self,lista):
        datoEliminar = lista[0]
        self.eliminarNodo(datoEliminar)
    
    def eliminarUltimo(self,lista):
        nDatos = len(lista)
        datoEliminar = lista[nDatos-1]
        self.eliminarNodo(datoEliminar)

    def __str__(self) -> str:
        aux = self.primero
        datos = ""
        while aux:
            datos += str(aux.dato) + "  "
            aux = aux.sig
            if aux.sig == self.primero.sig:
                break
        return datos

    def __len__(self):
        aux = self.primero
        count = 0
        while aux:
            count += 1
            aux = aux.sig
            if aux.sig == self.primero.sig:
                break
        return count
    
    def __getitem__(self, index):
        if index >= 0 and index < len(self):
            actual = self.primero
            for i in range(index):
                actual = actual.sig
            return actual.dato
        else:
            raise IndexError ("Indice fuera de rango")

if __name__ == "__main__":
    lc = ListaCircular() #instanciando Clase listaCircular
    lc.agregarInicio(3) # agrega al inicio [3]x
    lc.agregarUltimo(2) # agrega al final [3, 2]
    lc.agregarInicio(1) # agrega al inicio [1, 3, 2]
    lc.agregarInicio(54)
    lc.agregarInicio(48)
    
    print("Mostrando datos añadidos")
    print(lc) #imprimiendo datos de la lista circular

    print("Eliminando el primer dato")
    lc.eliminarPrimero(lc)
    print(lc)
    print("Eliminar el ultimo dato")
    lc.eliminarUltimo(lc)
    print(lc)