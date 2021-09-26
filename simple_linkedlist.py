class Node:
    valor = None
    siguiente = None

    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

    def enlazarSiguiente(self, siguiente): self.siguiente = siguiente

    def getSiguiente(self): return self.siguiente
    
    def getValor(self): return self.valor

class LinkedList():
    cabeza = None
    cola = None
    size = 0

    def addLast(self, nodo):
        if self.cabeza is None:
            self.cabeza = Node(nodo)
            self.cola = self.cabeza
        else:
            temp = self.cola
            nuevoNodo = Node(nodo)
            temp.enlazarSiguiente(nuevoNodo)
            self.cola = nuevoNodo
        self.size += 1
    
    def addFirst(self, nodo):
        if self.cabeza is None:
            self.cabeza = Node(nodo)
            self.cola = self.cabeza
        else:
            temp = self.cabeza
            nuevoNodo = Node(nodo)
            nuevoNodo.enlazarSiguiente(temp)
            self.cabeza = nuevoNodo
        self.size += 1

    def getValor(self, index):
        contador = 0
        temp = self.cabeza
        while (contador < index):
            temp = temp.getSiguiente()
            contador += 1
        return temp.getValor()
    
    def getSize(self):
        return self.size
    
    def estaVacia(self) -> bool:
        return True if self.cabeza == None else False
        
def main():
    linkedList1 = LinkedList()
    print(f'Esta vacia: {linkedList1.estaVacia()}')

    linkedList1.addFirst("cheerios")
    linkedList1.addFirst("fruitloops")
    linkedList1.addFirst("lucky charms")

    print(linkedList1.getValor(0))
    print(linkedList1.getValor(2))
    print(linkedList1.getValor(1))
    
    print(f'Cola: {linkedList1.cola.getValor()}')

    linkedList1.addLast("quacker")

    print(linkedList1.getValor(linkedList1.getSize() - 1))

    print(f'Cola: {linkedList1.cola.getValor()}')


if __name__ == "__main__":
    main()
