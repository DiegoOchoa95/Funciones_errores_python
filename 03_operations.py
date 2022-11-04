#Operaciones con conjuntos.
set_a={"Perú","Colombia","Brasil","Argentina"}
set_b={"Perú","Chile", "Venezuela"}

#Union de dos conjuntos, 2 maneras de unir.
set_c=set_a.union(set_b) #Aqui unimos mediante un metodo.
print(set_c)
print(set_a | set_b) #Aquí unimos mediante un signo |.

#Intersection de dos conjuntos, 2 maneras de intersectar.
set_c=set_a.intersection(set_b) #Aquí intersectamos mediante un metodo.
print(set_c)
print(set_a & set_b) #Aquí intersectamos mediante un signo &.

#Diferencia de dos conjuntos, 2 maneras de restar conjuntos.
set_c=set_a.difference(set_b) #Aquí restamos mediante un método.
print(set_c)
print(set_a - set_b) #Aquí restamos mediante un signo -.

#Diferencia simétrica de dos conjuntos, 2 maneras de realizar esta diferencia.
set_c=set_a.symmetric_difference(set_b)#Aquí restamos los valores que se interceptan mediante un metodo.
print(set_c)
print(set_a ^ set_b)#Aquí restamos mediante un signo ^(para sacar ese signo presionamos alt+94)