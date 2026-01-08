# Exercício - Adiando execução de funções
def soma(x):
    def s(y):
        return x + y
    return(s)


def multiplica(x):
    def m(y):
        return x * y
    return (m)


def criar_funcao(funcao, *args):
    return funcao(*args)


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)



print(soma_com_cinco(7))
print(multiplica_por_dez(7))
