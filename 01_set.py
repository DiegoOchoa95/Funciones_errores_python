#conjuntos
def run():
    paises={'Perú','Colombia','Chile','Brasil','Argentina','Ecuador','Bolivia','Paraguay','Perú'}
    print(paises) #fijate que al momento de ejecutar solo muestra un Perú, osea en un conjunto no hay elementos repetidos.
    print(type(paises))


    conjunto_numeros={1,2,3,4,5,6,7,8,9,2,1,8,78,12,41,15,96}
    print(conjunto_numeros)

    conjunto_tipos={1,'hola',12.12,"Diego Ochoa",7}
    print(conjunto_tipos)

    conjunto_string=set("HOLA") #set sirve para separar los string.
    print(conjunto_string)

    conjunto_tuplas=set(('abc','cbv','av','abc'))
    print(conjunto_tuplas)

    #lista a conjunto...
    numeros=[1,2,3,4,5,1,2,3,4,5]
    c_numeros=set(numeros)
    print(c_numeros)
    #de conjunto a una lista
    unicos=list(c_numeros)
    print(unicos)



if __name__=='__main__':
    run()