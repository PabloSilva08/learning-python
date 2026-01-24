import ctypes
import sys
from typing import List, Any

def inspecionar_memoria_profunda(lista_alvo: List[Any]) -> None:
    """
    Mostra o endereço do SLOT (onde o ponteiro fica) e 
    o endereço do OBJETO (para onde o ponteiro aponta).
    """
    # 1. Pegamos o endereço da estrutura da Lista (o Cabeçalho)
    endereco_lista: int = id(lista_alvo)
    
    # 2. Hack de CPython:
    # Em 64-bit, o ponteiro para o array de dados (ob_item) fica 
    # deslocado 24 bytes do início da estrutura da lista.
    # (8 bytes refcnt + 8 bytes type + 8 bytes size = 24 bytes)
    offset_ob_item: int = 24
    
    # Lemos o valor que está na memória neste local. 
    # Esse valor É o endereço onde começa o Array de Ponteiros.
    endereco_array_ponteiros: int = ctypes.c_longlong.from_address(endereco_lista + offset_ob_item).value

    print(f"--- Inspeção de Memória (Lista com {len(lista_alvo)} itens) ---")
    print(f"Endereço do Objeto Lista (Cabeçalho): {hex(endereco_lista)}")
    print(f"Endereço do Array de Gavetas (Dados): {hex(endereco_array_ponteiros)}")
    print("-" * 80)
    print(f"{'ÍNDICE':<8} | {'ENDEREÇO DA GAVETA (SLOT)':<30} | {'ENDEREÇO DO OBJETO (CONTEÚDO)':<30}")
    print("-" * 80)

    for i in range(len(lista_alvo)):
        # O endereço desta gaveta específica
        # Base do array + (índice * 8 bytes)
        endereco_da_gaveta: int = endereco_array_ponteiros + (i * 8)
        
        # O endereço do objeto (o que id() retorna normalmente)
        endereco_do_objeto: int = id(lista_alvo[i])
        
        print(f"{i:<8} | {hex(endereco_da_gaveta):<30} | {hex(endereco_do_objeto):<30}")

    print("-" * 80)
    print("CONCLUSÃO:")
    print("Note como a Coluna do MEIO cresce exatamente de 8 em 8 (0x0...0, 0x0...8, 0x0...0).")
    print("Isso prova que as gavetas são vizinhas físicas.")

# --- EXECUÇÃO ---

# Criando objetos espalhados
a: int = 100
b: str = "Python"
c: float = 3.14

minha_lista: List[Any] = [a, b, c]

inspecionar_memoria_profunda(minha_lista)
