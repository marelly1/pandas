miLista=["Maria","Pepe","Martha","Antonio"]

#para agregar un nuevo elemento al final de la lista
miLista.append("Sandra")

#para agragar un elemento en un lugar determinado de la lista
miLista.insert(2,"Mario")

#para adicionar otra lista a la lista original
miLista.extend(["Jorge,","Carmen"])

#para saber en qué posicion de indice esta un determinado elemento
print(miLista.index("Carmen"))

#para cuando haya 2 elementos iguales y quiero saber el indice del primero
#En python siempre va imprimir el prime.r elemento
print(miLista.index("Maria "))

#para saber si se encuentra un elemento en la lista
print("Pepe" in miLista)

#para eliminar elementos
miLista.remove("Martha")

#para eliminar el último elemento de la lista
miLista.pop()

print(miLista[:])

#para unir 2 lista diferentes y crear 3 listas
miLista2=["Roberto",5,True,78.35]

miLista3=miLista+miLista2

print (miLista3[:])
"""
