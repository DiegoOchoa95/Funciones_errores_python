#Agregamos elementos a una lista con for.(Lists comprehensions)
#Primera forma
numbers=[]
for element in range(1,11):
    numbers.append(element)   
    
print(numbers)
print("***********************")
numbers_v1=[]
for element in range(1,11):  
    numbers_v1.append(element*2) #Aqui agregamos los elementos multiplicado x 2.

print(numbers_v1)

print("***********************")
#Segunda forma
numbers_v2=[element for element in range(1,11)]
print(numbers_v2)
print("***********************")

numbers_v3=[element*2 for element in range(1,11)]
print(numbers_v3)#Aqui agregamos los elementos multiplicado x 2.