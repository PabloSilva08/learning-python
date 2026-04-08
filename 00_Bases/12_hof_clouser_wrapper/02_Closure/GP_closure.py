print("Exercício 01")

from typing import Callable

def criar_saudacao(nome: str) -> Callable[[], str]:
    def saudar() -> str:
        return f'Olá, {nome}!'
    return saudar

saudacao = criar_saudacao("Pablo")
print(saudacao())

###############################################################################
print()
print("=" * 60)
print("Exercício 02")
print()

from typing import Callable

def criar_multiplicador(fator: int) -> Callable[[int], int]:
    def multiplicar(numero: int) -> int:
        return numero * fator

    return multiplicar

dobrar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)

print(dobrar(5))
print(triplicar(5))

###############################################################################
print()
print("=" * 60)
print("Exercício 03")
print()

from typing import Callable

def criar_somador(valor: int) -> Callable[[int], int]:
    def somar(numero: int) -> int:
        return numero + valor

    return somar

somar_10 = criar_somador(10)
print(somar_10(5))

###############################################################################
print()
print("=" * 60)
print("Exercício 04")
print()

from typing import Callable

def criar_verificador_aprovacao(nota_minima: float) -> Callable[[float], bool]:
    def verificar(nota: float) -> bool:
        return nota >= nota_minima

    return verificar

aprovar_com_6 = criar_verificador_aprovacao(6.0)
aprovar_com_7 = criar_verificador_aprovacao(7.0)

print(aprovar_com_6(6.5))
print(aprovar_com_7(6.5))

###############################################################################
print()
print("=" * 60)
print("Exercício 05")
print()

from typing import Callable

def criar_prefixador(prefixo: str) -> Callable[[str], str]:
    def prefixar(texto: str) -> str:
        return f"{prefixo}{texto}"

    return prefixar

aviso = criar_prefixador("[AVISO] ")
erro = criar_prefixador("[ERRO] ")

print(aviso("Sistema iniciado"))
print(erro("Falha ao conectar"))

###############################################################################
print()
print("=" * 60)
print("Exercício 06")
print()

from typing import Callable

def criar_contador() -> Callable[[], int]:
    contador = 0
    def incrementar() -> int:
        nonlocal contador
        contador += 1
        return contador

    return incrementar

contador1 = criar_contador()

print(contador1())
print(contador1())
print(contador1())

###############################################################################
print()
print("=" * 60)
print("Exercício 07")
print()

from typing import Callable

def criar_formatador_preco(moeda: str, casas: int) -> Callable[[float], str]:
    def formatar(valor: float) -> str:
        return f"{moeda}{valor:.{casas}f}"

    return formatar


formatar_real = criar_formatador_preco("R$ ", 2)
formatar_dolar = criar_formatador_preco("$ ", 3)

print(formatar_real(12.5))
print(formatar_dolar(12.5))

###############################################################################
print()
print("=" * 60)
print("Exercício 08")
print()

from typing import Callable

def criar_validador_minimo(minimo: int) -> Callable[[int], bool]:
    def validar(valor: int) -> bool:
        return valor >= minimo

    return validar

valores = [3, 7, 10, 15]

validar_5 = criar_validador_minimo(5)
validar_10 = criar_validador_minimo(10)

print(list(filter(validar_5, valores)))
print(list(filter(validar_10, valores)))
