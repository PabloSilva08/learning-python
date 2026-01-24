from typing import List

def inspecionar_memoria() -> None:
    # Criamos objetos separadamente
    a: int = 10
    b: int = 20
    c: list = ['e', 'f', 'g', 'h', 'i']
    d: int = 30
    
    # Colocamos na lista
    lista: List[int] = [a, b, c, d]
    
    # Vamos ver onde esses números moram
    print(f"Endereço do 10 (Item 0): {id(lista[0])}")
    print(f"Endereço do 20 (Item 1): {id(lista[1])}")
    print(f"Endereço do l (Item 1): {id(lista[2])}")
    print(f"Endereço do 30 (Item 1): {id(lista[3])}")
    
    # Diferença entre os endereços
    diff: int = id(lista[1]) - id(lista[0])
    print(f"Distância na memória: {diff} bytes")
    # Em C, isso seria exatamente 4 ou 8 bytes. 
    # Em Python, pode ser um número enorme ou aleatório, 
    # pois os objetos estão espalhados na memória heap.

    diff: int = id(lista[1]) - id(lista[0])
    print(f"Distância na memória: {diff} bytes")
    diff: int = id(lista[2]) - id(lista[0])
    print(f"Distância na memória: {diff} bytes")
    diff: int = id(lista[3]) - id(lista[0])
    print(f"Distância na memória: {diff} bytes")

    print('-'*40)
    print('-'*40)

    diff: int = id(lista[1]) - id(lista[0])
    print(f"Distância na memória: {diff} bytes")
    diff: int = id(lista[2]) - id(lista[1])
    print(f"Distância na memória: {diff} bytes")
    diff: int = id(lista[3]) - id(lista[2])
    print(f"Distância na memória: {diff} bytes")
inspecionar_memoria()

'''
Original
from typing import List

def inspecionar_memoria() -> None:
    # Criamos objetos separadamente
    a: int = 10
    b: int = 20

    # Colocamos na lista
    lista: List[int] = [a, b]

    # Vamos ver onde esses números moram
    print(f"Endereço do 10 (Item 0): {id(lista[0])}")
    print(f"Endereço do 20 (Item 1): {id(lista[1])}")

    # Diferença entre os endereços
    diff: int = id(lista[1]) - id(lista[0])
    print(f"Distância na memória: {diff} bytes")
    # Em C, isso seria exatamente 4 ou 8 bytes.
    # Em Python, pode ser um número enorme ou aleatório,
    # pois os objetos estão espalhados na memória heap.

inspecionar_memoria()

'''

