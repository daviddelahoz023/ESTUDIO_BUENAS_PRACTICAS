from listas_enlazadas import *

#Creacion instancia
lista_01 = ListaSimple()

print("Lista:",lista_01)
print("Esta Vacia:",lista_01.estaVacia())

#Adicion elementos
lista_01.adicionarAlInicio(1)
lista_01.adicionarAlInicio(2)
lista_01.adicionarAlInicio(3)
print("Lista:",lista_01)
print("Esta Vacia:",lista_01.estaVacia())

#Buscar elementos
print("Buscar 01:",lista_01.buscar(5))
print("Buscar 02:",lista_01.buscar(1))

#Eliminar elementos
print("Eliminar 01:",lista_01.eliminarAlInicio())
print("Lista:",lista_01)