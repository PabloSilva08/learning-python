# 1 - GPT
print("GPT = Nivel 01\n\n")

from typing import Callable, Any

def triplicar(numb: int) -> int:
    return (numb * 3)

def aplicar(func: Callable, n: int) -> Any:
    return(func(n))

print(aplicar(triplicar, 4))

print()
print("*" * 10)
print()

######################################################

def saudar(string: str) -> str:
    return(f'Olá, {string}!')

def executar(func: Callable[[str], str], s: str) -> str:
    return func(s)

print(executar(saudar, "Pablo"))

print()
print("*" * 10)
print()

######################################################
######################################################
# 2
print("GPT = Nivel 02\n\n")

def somar(numero1: int, numero2: int) -> int:
    return numero1 + numero2

def multiplicar(numero1: int, numero2: int) -> int:
    return numero1 * numero2

def calcular(funcao: Callable[[int, int], int], numero1: int, numero2: int) -> int:
    return funcao(numero1, numero2)

print(calcular(somar, 2, 3))
print(calcular(multiplicar, 2, 3))

######################################################
print()
print("*" * 10)
print()

lista_de_nome = ["Ana", "Beatriz", "Caio", "Daniel"]

def tamanho_nome(string: str) -> int:
    return len(string)

lista_ordenada = sorted(lista_de_nome, key=tamanho_nome)
print(lista_ordenada)

######################################################
print()
print("*" * 10)
print()

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

def eh_par(numero: int) -> bool:
    if numero % 2 == 0:
        return True
    else:
        return False

print(list(filter(eh_par, numeros)))

print()
print("*" * 10)
print()

######################################################
######################################################
#3 
print("GPT = Nivel 03\n\n")

def dobrar(numero: int) -> int:
    return numero * 2

def aplicar_em_lista(funcao: Callable[[int], int], lista_de_inteiro: list[int]) -> list[int]:
    nova_lista: list[int] = []
    for i in lista_de_inteiro:
        nova_lista.append(funcao(i))
    return nova_lista

print(aplicar_em_lista(dobrar, [1, 2, 3, 4]))

######################################################
print()
print("*" * 10)
print()

def somar(a: int, b: int) -> int:
    return a+b

def subtrair(a: int, b: int) -> int:
    return a-b

def operacao_nao_encontrada(a: int, b: int) -> int:
    print("Operacao nao encontrada.")
    return 0

def escolher_operacao(nome: str) -> Callable[[int, int], int]:
    if nome == "soma":
        return somar
    elif nome == "subtracao":
        return subtrair
    else:
        return operacao_nao_encontrada

operacao = escolher_operacao("soma")
print(operacao(10, 3))

operacao = escolher_operacao("subtracao")
print(operacao(10, 3))

operacao = escolher_operacao("s")
print(operacao(10, 3))
