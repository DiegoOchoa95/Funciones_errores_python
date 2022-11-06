def run():
    #diccionario comprehensions
    #agregamos valores al diccionario con un for
    dict={}
    for i in range(1,11):
        dict[i]=i
    print(dict)


    print("******************")
    #agregamos valores al diccionario multiplicado *2
    dict2={}
    for i in range(1,11):
        dict2[i]=i*2
    print(dict2)

    #Forma comprimida de dict2
    dict3={i:i*2 for i in range(1,11) }
    print(dict3)

    print("******************")
    #generamos un diccionario a partir de una lista
    #paises y su poblacion
    import random #importamos para generar numeros aleatorios
    countries=["peru","chile","brasil","argentina","bolivia","ecuador"]
    population={}
    for i in countries:
        population[i]=random.randint(1,100)
    print(population)

    #forma comprimida para el diccionario poblacion
    population_v2={i:random.randint(1,100) for i in countries }
    print(population_v2)


    print("******************")
    #ahora vamos a iterar 2 listas y generar 1 diccionario
    #pero antes debemos saber como fusionar 2 listas de la sgte manera...
    list_1=['jose','andres','eugenia','felix','virginia']
    list_2=[25,30,56,60,92]
    print(list(zip(list_1,list_2))) #con la funcion zip fusionamos 2 listas el resultado nos muestra una lista de tuplas

    #forma comprimida en una linea, observa el resultado
    new_dict={list_1:list_2 for (list_1,list_2) in zip(list_1,list_2)}
    print(new_dict)








if __name__=='__main__':
    run()