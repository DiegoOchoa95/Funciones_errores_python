def suma_rango(a,b): #declaro una funcion
    print("***",a,b,"***") #mostramos los 2 valores
    sum=0
    for i in range(a,b):
        sum=sum+i
    ###print(sum) #ahora en vez de mostrar un print de la suma, usamos un return
    return sum #para regresar un resultado, ejemplo lineas abajo...
    

###suma_rango(10,30)
###suma_rango(5,20)
###suma_rango(1,100) #llamo a la funcion, sin estar repitiendo el codigo


#Usamos el return 
result=suma_rango(10,20)
print(result)
result_2=suma_rango(result,result+10)
print(result_2)

