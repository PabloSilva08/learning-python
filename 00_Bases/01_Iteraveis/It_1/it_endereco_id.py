import ctypes
import sys
from typing import List, Any

def inspecionar_memoria_com_id(lista_alvo: List[Any]) -> None:
    """
    Mostra o endereço físico do slot e comprova que o conteúdo 
    deste slot é exatamente o id() do objeto.
    """
    endereco_lista: int = id(lista_alvo)
    
    # Deslocamento para chegar no ponteiro do array (CPython 64-bit)
    offset_ob_item: int = 24
    
    # Pegamos o endereço onde começa o array de dados
    endereco_array_ponteiros: int = ctypes.c_longlong.from_address(endereco_lista + offset_ob_item).value

    print(f"--- RAIO-X DA LISTA (Objeto Lista id: {endereco_lista}) ---")
    print(f"{'IDX':<4} | {'ONDE ESTÁ O PONTEIRO?':<26} | {'O QUE TEM DENTRO? (Hex)':<24} | {'CONFIRMAÇÃO (id)':<20}")
    print("-" * 85)

    for i in range(len(lista_alvo)):
        # 1. Onde a "gaveta" está (Endereço Físico do Slot)
        endereco_da_gaveta: int = endereco_array_ponteiros + (i * 8)
        
        # 2. Lendo a memória RAM diretamente naquela gaveta
        # Isso extrai o valor cru que está gravado lá.
        valor_dentro_da_gaveta: int = ctypes.c_longlong.from_address(endereco_da_gaveta).value
        
        # 3. Pegando o id() oficial do Python
        id_oficial: int = id(lista_alvo[i])
        
        # Formatando para exibição
        hex_gaveta = hex(endereco_da_gaveta)
        hex_conteudo = hex(valor_dentro_da_gaveta)
        
        print(f"{i:<4} | {hex_gaveta:<26} | {hex_conteudo:<24} | id: {id_oficial}")

    print("-" * 85)
    print("CONCLUSÃO VISUAL:")
    print("Compare a coluna do MEIO (Hex) com a coluna da DIREITA (Decimal).")
    print("Se você converter o Hex para Decimal, verá que são IDÊNTICOS.")
    print("A lista guarda literalmente o ID do objeto.")

# --- EXECUÇÃO ---

# Criando objetos
num: int = 42
texto: str = "Tipagem"
flutuante: float = 9.99

# Montando a lista
minha_lista: List[Any] = [num, texto, flutuante]

inspecionar_memoria_com_id(minha_lista)
