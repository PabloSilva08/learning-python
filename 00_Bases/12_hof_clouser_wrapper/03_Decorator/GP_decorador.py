print("Exercício 01")
print()

from typing import Callable

def mostrar_antes(funcao: Callable[[], None]) -> Callable[[], None]:
    def wrapper() -> None:
        print("Antes da função")
        funcao()

    return wrapper

def dizer_oi() -> None:
    print("Oi!")

dizer_oi = mostrar_antes(dizer_oi)
dizer_oi()

###############################################################################
print()
print("=" * 60)
print("Exercício 02")
print()

from typing import Callable

def mostrar_antes_e_depois(funcao: Callable[[], None]) -> Callable[[], None]:
    def wrapper() -> None:
        print("Antes da função")
        funcao()
        print("Depois da função")

    return wrapper

def mostrar_mensagem() -> None:
    print("Executando a função")

mostrar_mensagem = mostrar_antes_e_depois(mostrar_mensagem)
mostrar_mensagem()

###############################################################################
print()
print("=" * 60)
print("Exercício 03")
print()

from typing import Callable

def avisar_execucao(funcao: Callable[[], None]) -> Callable[[], None]:
    def wrapper() -> None:
        print("Executando...")
        funcao()

    return wrapper

def saudar() -> None:
    print("Olá, mundo!")

saudar = avisar_execucao(saudar)
saudar()

###############################################################################
print()
print("=" * 60)
print("Exercício 04")
print()

from typing import Callable

def mostrar_inicio(funcao: Callable[[], None]) -> Callable[[], None]:
    def wrapper() -> None:
        print("Iniciando operação...")
        funcao()

    return wrapper

def mostrar_soma() -> None:
    print(2 + 3)

mostrar_soma = mostrar_inicio(mostrar_soma)
mostrar_soma()

###############################################################################
print()
print("=" * 60)
print("Exercício 05")
print()

from typing import Callable

def mostrar_antes(funcao: Callable[[], None]) -> Callable[[], None]:
    def wrapper() -> None:
        print("Antes da execução")
        funcao()

    return wrapper

@mostrar_antes
def falar() -> None:
    print("Estou falando")

falar()

###############################################################################
print()
print("=" * 60)
print("Exercício 06")
print()

from typing import Callable

def repetir_duas_vezes(funcao: Callable[[], None]) -> Callable[[], None]:
    def wrapper() -> None:
        funcao()
        funcao()

    return wrapper

@repetir_duas_vezes
def dizer_ola() -> None:
    print("Olá!")

dizer_ola()

###############################################################################
print()
print("=" * 60)
print("Exercício 07")
print()

from typing import Callable

def log_execucao(funcao: Callable[[], None]) -> Callable[[], None]:
    def wrapper() -> None:
        print(f"[LOG] Executando {funcao.__name__}")
        funcao()

    return wrapper

@log_execucao
def processar() -> None:
    print("Processando dados...")

processar()

###############################################################################
print()
print("=" * 60)
print("Exercício 08")
print()

from typing import Callable

def mostrar_resultado(funcao: Callable[[], int]) -> Callable[[], int]:
    def wrapper() -> int:
        resultado = funcao()
        print(f"Resultado: {resultado}")
        return resultado

    return wrapper

@mostrar_resultado
def calcular() -> int:
    return 2 + 3

valor = calcular()
print(f"Valor retornado fora da função: {valor}")
