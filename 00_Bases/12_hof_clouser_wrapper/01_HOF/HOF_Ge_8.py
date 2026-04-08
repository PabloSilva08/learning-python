#  - Gemini
print("Gemini = Nivel 04\n\n")

from typing import Callable, List

def dobrar(n: int) -> int:
    return n * 2

def somar_um(n: int) -> int:
    return n + 1

def ao_quadrado(n: int) -> int:
    return n ** 2

lista_funcoes: List[Callable[[int], int]] = [
    dobrar,
    somar_um,
    ao_quadrado
]

def executar_pipeline(numero: int, lista_de_funcoes: List[Callable[[int], int]]) -> int:
    for funcao in lista_de_funcoes:
        numero = funcao(numero)
    return numero


resultado = executar_pipeline(5, lista_funcoes)
print(resultado) # 121
