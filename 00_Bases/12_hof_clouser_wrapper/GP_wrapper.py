print("GPT - WRAPPER")
print()
print("Exercício 01")
print()

def dizer_oi() -> None:
    print("Oi!")

def wrapper() -> None:
    print("Antes da função")
    dizer_oi()

wrapper()

###############################################################################
print()
print("=" * 60)
print("Exercício 02")
print()

from typing import Callable

def mostrar_mensagem() -> None:
    print("Executando a função")

def wrapper() -> None:
    print("Antes da função")
    mostrar_mensagem()
    print("Depois da função")

wrapper()

###############################################################################
print()
print("=" * 60)
print("Exercício 03")
print()

def somar() -> int:
    return 2 + 3

def wrapper() -> int:
    print("Chamando função...")
    resultado = somar()
    print(f"Resultado interno: {resultado}")
    return resultado

valor = wrapper()
print(f"Resultado fora do wrapper: {valor}")

###############################################################################
print()
print("=" * 60)
print("Exercício 04")
print()

def saudar() -> str:
    return "Olá, Pablo!"

def wrapper() -> str:
    print("Preparando saudação...")
    mensagem = saudar()
    print("Saudação pronta.")
    return mensagem

texto = wrapper()
print(texto)

###############################################################################
print()
print("=" * 60)
print("Exercício 05")
print()

from typing import Callable

def adicionar_aviso(funcao: Callable[[], None]) -> Callable[[], None]:
    def wrapper() -> None:
        print("Executando função...")
        funcao()

    return wrapper

@adicionar_aviso
def exibir() -> None:
    print("Conteúdo exibido")
#
#exibir()
#print(adicionar_aviso(exibir)())
#print('-')
#aviso = adicionar_aviso(exibir)
#aviso()
