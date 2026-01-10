# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
#def mult(num):
#    return(num * multiplicador)

def multiplicar(multiplicador) -> float:
    def mult(num):
        return(num * multiplicador)
    return(mult)

duplicar = multiplicar(2)
triplicar = multiplicar(3)
quadriplicar = multiplicar(4)

print(duplicar(2))
print(duplicar(3))
print(duplicar(4))


