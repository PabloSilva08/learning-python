x = 1

print("01 - Valor x = ", x)
def escopo():
    global x
    x = 10
    print("11 - Valor x = ", x)


    def outra_funcao():
        global x
#        print("21 - Valor x = ", x)
        x = 11
        print("22 - Valor x = ", x)

    outra_funcao()
    print("12 - Valor x = ", x)

print("02 - Valor x = ", x)

escopo()
print("03 - Valor x = ", x)
