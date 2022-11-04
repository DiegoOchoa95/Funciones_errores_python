#CRUD en conjuntos.
paises={'Perú','Colombia','Chile','Bolivia','Brasil','Argentina'}
tamaño=len(paises)#tamaño del conjunto, te muestra la cantidad de valores del conjunto.
print(tamaño)
print('Perú' in paises) #preguntamos si peru esta en el conjunto.

#Add, agregar un valor a un conjunto.
paises.add("Venezuela")
print(paises) #cabe indicar si agregas 2 veces el mmismo elemento, el conjunto solo te mostrara uno.

#Update, agregamos mas valores.
paises.update({"Paraguay","Uruguay","Ecuador","Perú"})
print(paises)

#Remove, eliminar valores de un conjunto.
paises.remove("Chile")
print(paises)

#Discard, elimina un elemento, pero si no lo encuentra no arroja error ni nada.
paises.discard("PERÚ")
print(paises)

#Clear, eliminamos todos los valores de un conjunto.
paises.clear()
print(paises) # Nos arroja un conjunto vacio. 
print(len(paises))





