# 1 - Gemini
print("Gemini = Nivel 01\n\n")

def chamar_funcao(func: callable, texto: str) -> None:
    return (func(texto))

def f(x: str) -> None:
    print(f'Eu estou executando: {x}')

f("Eita Porra...")

print()
print("*" * 10)
print()

######################################################

from typing import Callable

def calcular(operacao: Callable[[int, int], int], n1, n2) -> int:
    return operacao(n1, n2)

def soma(a: int, b: int) -> int:
    return(a+b)

print(calcular(soma, 5, 3))

######################################################
######################################################
#2

print()
print("*" * 10)
print()

print("Gemini = Nivel 02\n\n")

def aplicar_multiplicador(lista_numerica: list[int], funcao: Callable[[int], int]) -> list[int]:
    lista2 = [funcao(x) for x in lista_numerica]
    return lista2

def potencia_quadrada(x: int) -> int:
    return x**2

lista_natural = [1, 2, 3, 4, 5, 6]

print(aplicar_multiplicador(lista_natural, potencia_quadrada))

print()
print("*" * 10)
print()

######################################################

def filtrar_dados(lista: list[str], funcao: Callable[[str], bool]) -> list[str]:
    return [l for l in lista if funcao(l)]


nomes = ["Ana", "Bento", "Beatriz", "Caio"]
# Função de critério: começa com 'B'
so_com_b = filtrar_dados(nomes, lambda nome: nome.startswith("B"))
# Resultado: ["Bento", "Beatriz"]

print(so_com_b)

print()
print("*" * 10)
print()

######################################################


def ordenar_por_tamanho(lista_nomes: list[str]) -> list[str]:
    return sorted(lista_nomes, key=len)

print(ordenar_por_tamanho(nomes))

######################################################
######################################################
#3

print()
print("*" * 10)
print()

print("Gemini = Nivel 03\n\n")

def gerar_exponenciador(expoente: int) -> Callable[[int], int]:
    def potencia(base: int) -> int:
        return base**expoente
    return potencia 


quadrado = gerar_exponenciador(2)
cubo = gerar_exponenciador(3)

print(quadrado(4)) # Deve imprimir 16 (4^2)
print(cubo(2))     # Deve imprimir 8  (2^3)

print()
print("*" * 10)
print()

######################################################

print()
print("*" * 10)
print()

def somar(numero1: float, numero2: float) -> float:
    return numero1 + numero2

def subtrair(numero1: float, numero2: float) -> float:
    return numero1 - numero2

def multiplicar(numero1: float, numero2: float) -> float:
    return numero1 * numero2

def dividir(numero1: float, numero2: float) -> float:
    try:
        resultado = numero1 / numero2
        return resultado
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
        return 0.0 

def operacao_nao_encontrada(numero1: float, numero2: float) -> float:
    print("Operacao nao encontrada.")
    return 0

def obter_calculadora(nome_operacao: str) -> Callable[[float, float], float]:
    operacoes = {
        "somar": somar,
        "subtrair": subtrair,
        "multiplicar": multiplicar,
        "dividir": dividir,
        "outros": operacao_nao_encontrada,
    }

    if nome_operacao in operacoes:
        return operacoes[nome_operacao]
    else:
        return operacoes["outros"]

calc = obter_calculadora("somar")
print(calc(10, 5)) # Deve imprimir 15

calc = obter_calculadora("dividir")
print(calc(10, 0)) # Deve imprimir 15
