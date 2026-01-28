import os

funfar: bool = True

def starting() -> str:
    print("\nComandos: listar, desfazer, refazer, exit")
    item: str = input("Digite uma tarefa ou comando: ").upper()
    return(item)

def listar(lista: list [str] = None) -> None:
    if lista == None:
        lista = []
    print("\n\nTAREFAS:\n")
    for item in lista:
        print(f'- {item}')
    if not lista:
        print("\nNão existe tarefas.")

def additem(item: str, lista: list[str] = None) -> list[str]:
    if lista == None:
        lista = []
    item = item.strip()
    if item == '':
        print("\nVocë nao digitou nenhuma tarefa.")
        return(lista)
    lista.append(item)
    print(f'\nA tarefa {item} foi adicionada.')
    return(lista)

def undo_list(lista: list[str] = None, pilha: list[str] = None) -> list[str]:
    if lista == None:
        lista = []
    if pilha == None:
        pilha = []

    if lista:
        pilha.append(lista[-1])
        print(f'\nA tarefa {lista[-1]} foi desfeita.')
        del lista[-1]
    else:
        print("\nSua lista está vazia.")

    return (lista)

def redo_list(lista: list[str] = None, pilha: list[str] = None) -> list[str]:
    if lista == None:
        lista = []
    if pilha == None:
        pilha = []
    
    if not pilha:
        print("\nNão existe tarefas para refazer.")

    if pilha:
        lista.append(pilha[-1])
        print(f'\nA tarefa {lista[-1]} foi refeita.')
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
