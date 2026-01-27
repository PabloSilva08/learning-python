import os

funfar: bool = True

def starting() -> str:
    print("\nComandos: listar, desfazer, refazer, exit")
    item: str = input("Digite uma tarefa ou comando: ").upper()
    return(item)

def listar(lista=None) -> None:
    if lista == None:
        lista = []
        print("\nNão existe tarefas.")
    print("\n\nTAREFAS:\n")
    for item in lista:
        print(f'- {item}')

def additem(item: str, lista=None) -> list[str]:
    if lista == None:
        lista = []
    lista.append(item)
    return(lista)

def undo_list(lista=None, pilha=None) -> list[str]:
    if lista == None:
        lista = []
    if pilha == None:
        pilha = []

    if lista:
        pilha.append(lista[-1])
        del lista[-1]
    else:
        print("\nSua lista está vazia.")

    return (lista)

def redo_list(lista=None, pilha=None) -> list[str]:
    if lista == None:
        lista = []
    if pilha == None:
        pilha = []
    
    if pilha:
        lista.append(pilha[-1])
        del pilha[-1]
    
    return (lista)

lista = []
pilha = []
while funfar:
    item = starting()

    if item == "LISTAR":
        listar(lista)
    elif item == "DESFAZER":
        lista = undo_list(lista, pilha)
    elif item == "REFAZER":
        lista = redo_list(lista, pilha)
    elif item == "EXIT":
        funfar = False
    elif item == "CLEAR":
        os.system('clear')
    else:
        lista = additem(item, lista)
