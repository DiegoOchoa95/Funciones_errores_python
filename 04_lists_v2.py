#listas comprehensions
#agregamos numeros a una lista, solo siendo pares
numbers=[]
for i in range(1,11):
    if i%2==0:
        numbers.append(i)
print(numbers)        

print("************************")
#agregamos numeros a una lista, solo siendo pares y multiplicamos *2
numbers_v2=[]
for i in range(1,11):
    if i%2==0:
        numbers_v2.append(i*2)
print(numbers_v2)

print("************************")
#Con una comprehension resumida en una linea seria asi...
numbers_v3=[i*2 for i in range(1,11) if i%2==0 ]
print(numbers_v3)