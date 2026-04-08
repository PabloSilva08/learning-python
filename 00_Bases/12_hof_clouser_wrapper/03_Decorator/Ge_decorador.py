print("Exercício 01")
print()

from typing import Callable

def anunciar(funcao: Callable[[], None]) -> Callable[[], None]:
    def wrapper() -> None:
        print("A função será executada!")
        funcao()

    return wrapper

@anunciar
def bom_dia():
    print("Bom dia!")

bom_dia()

###############################################################################
print()
print("=" * 60)
print("Exercício 02")
print()

from typing import Callable, Any

def gritar(funcao: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        grito = funcao(*args, **kwargs)
        return grito.upper()

    return wrapper

@gritar
def saudar(nome: str) -> str:
    return f"bom dia, {nome}"

print(saudar("Pablo"))


###############################################################################
#print()
#print("=" * 60)
#print("Exercício 02")
#print()
#
#from typing import Callable, Any
#
#def gritar(funcao: Callable[[str], Any]) -> Callable[[str], Any]:
#    def wrapper(x) -> Any:
#        grito = funcao(x)
#        return grito.upper()
#
#    return wrapper
#
#@gritar
#def saudar(nome: str) -> str:
#    return f"bom dia, {nome}"
#
#print(saudar("Larissa"))
#
###############################################################################
#print()
#print("=" * 60)
#print("Exercício 02")
#print()
#
#from typing import Callable, Any
#
#def gritar(funcao: Callable[[str], Any]) -> Callable[[str], Any]:
#    def wrapper(*args: Any, **kwargs: Any) -> Any:
#        grito = funcao(x)
#        return grito.upper()
#
#    return wrapper
#
#@gritar
#def saudar(nome: str) -> str:
#    return f"bom dia, {nome}"
#
#print(saudar("Liz"))

###############################################################################
print()
print("=" * 60)
print("Exercício 03")
print()

from typing import Callable, Any
import time

def cronometrar(funcao: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        tempo = time.time() - inicio
        print(f"A função {funcao.__name__} levou {tempo} segundos")
        return resultado
    return wrapper

@cronometrar
def demora():
    time.sleep(1)
    return "Terminei"

print(demora())

###############################################################################
print()
print("=" * 60)
print("Exercício 04")
print()

from typing import Callable, Any

def apenas_inteiros(funcao: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        inteiro = all([isinstance(item, int) for item in args])
        if not inteiro:
            raise TypeError("Um ou mais número não é inteiro.")
        return funcao(*args, **kwargs)
 #Essa parte ficou errada no codigo, por que quem é o responsavel por isso é quem chama a afunçao
 #       except TypeError as e:
 #           return f"Erro: {e}"
    return wrapper

@apenas_inteiros
def somar(a, b):
    return a + b

print(somar(10, 20)) # Funciona: 30
#print(somar(10, "20")) # Erro: TypeError

###############################################################################
###############################################################################

from typing import Callable, Any

def apenas_inteiros(funcao: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Usando Generator Expression (sem os colchetes [])
        if not all(isinstance(item, int) for item in args):
            raise TypeError("Apenas argumentos inteiros são permitidos.")
        
        return funcao(*args, **kwargs)
    return wrapper

@apenas_inteiros
def somar(a: int, b: int) -> int:
    return a + b

# Agora o erro "explode" no console, o que é o comportamento esperado de um TypeError
# print(somar(10, "20"))

###############################################################################
print()
print("=" * 60)
print("Exercício 05")
print()

from typing import Callable, Any

def dobrar_resultado(funcao: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        resultado = funcao(*args, **kwargs)
        return resultado * 2
    return wrapper




@dobrar_resultado
def calcular_area_quadrado(lado: int) -> int:
    return lado * lado

print(calcular_area_quadrado(5)) # O quadrado de 5 é 25, o dobro é 50.

###############################################################################
print()
print("=" * 60)
print("Exercício 06")
print()

from typing import Callable, Any

def repetir(n: int) -> Callable[..., Any]:
    def decorador(funcao: Callable[..., None]) -> Callable[..., None]:
        def wrapper(*arg: Any, **kwarg: Any) -> None:
            for i in range(n):
                funcao()
        return wrapper
    return decorador


@repetir(3)
def dizer_oi():
    print("Oi!")

dizer_oi()
# Deve imprimir "Oi!" três vezes.

###############################################################################
#Correcao Minima
#from typing import Callable, Any
#
#def repetir(n: int):
#    def decorador(funcao: Callable[..., Any]) -> Callable[..., Any]:
#        def wrapper(*args: Any, **kwargs: Any) -> Any:
#            resultado = None
#            for _ in range(n):
#                # Passamos os argumentos aqui para a função original
#                resultado = funcao(*args, **kwargs)
#            return resultado
#        return wrapper
#    return decorador
###############################################################################
#Forma Pythonica
#from typing import Callable, Any, TypeVar

# Usamos TypeVar para dizer que o que entra de tipo, sai de tipo
#F = TypeVar('F', bound=Callable[..., Any])
#
#def repetir(n: int) -> Callable[[F], F]:
#    def decorador(funcao: F) -> F:
#        def wrapper(*args: Any, **kwargs: Any) -> Any:
#            ultimo_resultado = None
#            for _ in range(n):
#                ultimo_resultado = funcao(*args, **kwargs)
#            return ultimo_resultado
#        return wrapper # type: ignore
#    return decorador # type: ignore

###############################################################################
print()
print("=" * 60)
print("Exercício 07")
print()

from typing import Callable, Any

def limitar_chamadas(max_vezes: int) -> Callable[..., Any]:
    contador = 0
    def decorador(funcao: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            nonlocal contador
            if contador < max_vezes:
                contador += 1
                return funcao(*args, **kwargs)
            else:
                return print("Limite de execuções atingido")
        return wrapper
    return decorador




@limitar_chamadas(2)
def realizar_pagamento():
    print("Pagamento processado!")

realizar_pagamento() # "Pagamento processado!"
realizar_pagamento() # "Pagamento processado!"
realizar_pagamento() # "Limite de execuções atingido"

###############################################################################
# Versão Pythoninca
#
#from typing import Callable, Any
#
#def limitar_chamadas(max_vezes: int):
#    contador = 0
#    def decorador(funcao: Callable[..., Any]):
#        def wrapper(*args: Any, **kwargs: Any) -> Any:
#            nonlocal contador
#            if contador < max_vezes:
#                contador += 1
#                return funcao(*args, **kwargs) # Passa args e retorna valor
#            return "Limite de execuções atingido" # Retorna a string
#        return wrapper
#    return decorador
#
###############################################################################

###############################################################################
print()
print("=" * 60)
print("Exercício 08")
print()

from typing import Callable, Any

def memoizar() -> Callable[..., Any]:
    def decorador(funcao: Callable[..., Any]) -> Callable[..., Any]:
        cache ={}
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if args not in cache:
                cache[*args] = funcao(*args, **kwargs)
                return cache[*args]
            return cache[*args]
        return wrapper
    return decorador

@memoizar()
def calculo_pesado(n):
    print(f"Fazendo cálculo para {n}...")
    return n * n

print(calculo_pesado(5)) # Imprime "Fazendo cálculo..." e retorna 25
print(calculo_pesado(5)) # Retorna 25 direto do cache (não imprime a frase)

###############################################################################
#from typing import Callable, Any
#
#def memoizar() -> Callable[..., Any]:
#    def decorador(funcao: Callable[..., Any]) -> Callable[..., Any]:
#        cache = {}
#        def wrapper(n):
#            if n not in cache:
#                cache[n] = funcao(n)
#            return cache[n]
#        return wrapper
#    return decorador


@memoizar()
def calculo_pesado(n):
    print(f"Fazendo cálculo para {n}...")
    return n * n

print(calculo_pesado(5)) # Imprime "Fazendo cálculo..." e retorna 25
print(calculo_pesado(5)) # Retorna 25 direto do cache (não imprime a frase)

