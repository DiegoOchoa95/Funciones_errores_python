#Funciones en Python
#Con def definimos una funcion, dentro de los () podemos colocar
# una variable, debajo colocamos la accion a ejecutar, y mas abajo
# llamamos a la funcion para que se ejecute por ejemplo...
def my_print(text):
    print(text*2)

my_print('Diego') #Aqui llamo a la funcion my_print, y ejecuta lo indicado.
my_print('Eduardo')#Aqui llamo a la funcion my_print, y ejecuta lo indicado.

print("*"*20)
#Otro ejemplo
def suma(a,b):
    print(a+b)

suma(1,5)#Aqui llamo a la funciona suma
suma(2,8)#Aqui llamo a la funciona suma

print("*"*20)
#Se puede fusionar funciones tambien...por ejemplo...
#fusiono la funcion my_print con la funcion suma...
def suma(a,b):
    my_print(a+b)

suma(3,7)
suma(25,10)


