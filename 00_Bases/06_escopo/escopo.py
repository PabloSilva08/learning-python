x = 1
y = 2
z = 3

def escopo():
    global x
    x = 10
    y = 20
    print("----Antes----")
    print("escopo --> x = ", x, "ID => ", id(x))
    print("escopo --> y = ", y, "ID => ", id(y))
    print("escopo --> z = ", z, "ID => ", id(z))
    outra_funcao()
    print("----Depois----")
    print("escopo --> x = ", x, "ID => ", id(x))
    print("escopo --> y = ", y, "ID => ", id(y))
    print("escopo --> z = ", z, "ID => ", id(z))


def outra_funcao():
    global y 
    x = 100
    y = 200 
    print("--------Dentro de outra funcao--------")
    print("outra funcao --> x = ", x, "ID => ", id(x))
    print("outra funcao --> y = ", y, "ID => ", id(y))
    print("outra funcao --> z = ", z, "ID => ", id(z))
    print("--------Dentro de outra funcao--------")

print("Fora de tudo --> x = ", x, "ID => ", id(x))
print("Fora de tudo --> y = ", y, "ID => ", id(y))
print("Fora de tudo --> z = ", z, "ID => ", id(z))
print("-------------------")
escopo()
print("-------------------")
print("Fora de tudo --> x = ", x, "ID => ", id(x))
print("Fora de tudo --> y = ", y, "ID => ", id(y))
print("Fora de tudo --> z = ", z, "ID => ", id(z))
