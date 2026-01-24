from typing import List, Iterator

# 1. Criamos a lista
# A lista mora num endereço de memória, digamos Endereço X
lista: List[str] = ["A", "B", "C"]

# 2. Criamos o iterador
# O iterador é um objeto novo, mora no Endereço Y
meu_iterador: Iterator[str] = iter(lista)

print(f"Endereço da Lista na RAM:    {id(lista)}")
print(f"Endereço do Iterador na RAM: {id(meu_iterador)}")

# 3. Consumindo itens
# Note que o objeto 'meu_iterador' continua no MESMO endereço (Y).
# Ele não está "andando" na memória. Ele está paradinho no lugar dele,
# apenas atualizando seu contador interno.
print("-" * 30)
item1 = next(meu_iterador)
print(f"Peguei '{item1}'. O iterador mudou de lugar na RAM? Não. ID: {id(meu_iterador)}")

item2 = next(meu_iterador)
print(f"Peguei '{item2}'. O iterador mudou de lugar na RAM? Não. ID: {id(meu_iterador)}")
