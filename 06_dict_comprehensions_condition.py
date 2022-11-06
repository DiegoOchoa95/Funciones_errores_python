#Dict comprehensions with conditions
#estructura: x={key:value for.......... if......}
def run():
    import random
    countries=['peru','brasil','colombia','chile','ecuardo','argentina','uruguay']
    population={i:random.randint(1,100) for i in countries}
    print(population)

    result={countries:population for (countries,population) in population.items() if population>50}
    print(result)#mostrara los mayores de 50


    print("*"*20)
    #Otro ejemplo, vamos a iterar un text
    #convirtiendo a diccionario con los valores en mayusculas
    #solo vocales del texto
    text="Hola mi nombre es diego ochoa orellana"
    dict={i: i.upper() for i in text if i in 'aeiou'}
    print(dict)

    print("*"*20)
    #Otro ejemplo, vamos a iterar un text ingresado por el usuario
    #mostrando los valores en mayusculas, solo vocales
    frase=input("Ingrese una frase: ")
    c=0
    dict2={i:i.upper() for i in frase if i in 'aeiou'}
    print(dict2)






if __name__=='__main__':
    run()