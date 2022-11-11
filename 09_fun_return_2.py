
#declaramos una funcion con 3 parametros
#retornamos los parametros multiplicandolos
def find_volume(length,width,depth):
    return length*width*depth

result=find_volume(4,5,6)#llamamos la funcion iguala a una variable
print(result)#mostramos el resultado

print("*"*20)
#declaramos otra funcion
def run(a=30,b=10,c=27):
    return a+b+c

result=run()
print(result)

print("*"*20)
#declaramos otra funcion
def kakaroto():
    transformacion=input("Ingrese la fase: ")
    return "Super sayayin fase "+str(transformacion)

resultado=kakaroto()
print(resultado)


print("*"*20)
#declaramos otra funcion
def numbers():
    a=int(input("Primer número: "))
    b=int(input("Segundo número: "))
    c=int(input("Tercer número: "))
    suma=a+b+c
    return suma

respuesta=numbers()
print(respuesta)


print("*"*20)
#declaramos otra funcion
def runrun():
    tupla=(1,2,3,4,5,6)
    posicion=int(input("Ingrese la posicion de la tupla: "))
    return tupla[posicion]

r=runrun()
print(r)
