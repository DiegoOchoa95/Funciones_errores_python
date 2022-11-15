price=100 # variable global
def increment():
    price=200 # esta variable no es global, solo funciona en la funcion, por eso no afecta a la global
    price=price+10
    print(price)
    return price

print(price)
resultado=increment()
print(resultado)
