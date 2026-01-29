import os
import json 

funfar: bool = True


def starting() -> str:
    print("\nComandos: listar, desfazer, refazer, exit")
    item: str = input("Digite uma tarefa ou comando: ")
    return (item)


def listar(lista: list[str] = None) -> None:
    if lista is None:
        lista = []
    print("\n\nTAREFAS:\n")
    for item in lista:
        print(f'- {item}')
    if not lista:
        print("Não existe tarefas.")


def additem(item: str, lista: list[str] = None) -> list[str]:
    if lista is None:
        lista = []
    item = item.strip()
    if item == '':
        print("\nVocë nao digitou nenhuma tarefa.")
        return (lista)
    lista.append(item)
    print(f'\nA tarefa {item} foi adicionada.')
    return (lista)


def undo_list(lista: list[str] = None, pilha: list[str] = None) -> list[str]:
    if lista is None:
        lista = []
    if pilha is None:
        pilha = []

    if lista:
        pilha.append(lista[-1])
        print(f'\nA tarefa {lista[-1]} foi desfeita.')
        del lista[-1]
    else:
        print("\nSua lista está vazia.")

    return (lista)


def redo_list(lista: list[str] = None, pilha: list[str] = None) -> list[str]:
    if lista is None:
        lista = []
    if pilha is None:
        pilha = []
    if not pilha:
        print("\nNão existe tarefas para refazer.")

    if pilha:
        lista.append(pilha[-1])
        print(f'\nA tarefa {lista[-1]} foi refeita.')
        del pilha[-1]
    return (lista)


def json_file_save(lista: list[str]) -> None:
    if not lista:
        print("\nLista em branco, nada a salvar.\n")
        return
    with open('dados.json', 'w') as f_json:
        json.dump(lista, f_json, indent=4)
        print("\nLista salva com sucesso.\n")


def json_file_read(lista: list[str]) -> list[str]:
    lista_carregfada: list[str] = []
    try:
        with open('dados.json', 'r') as f_json:
            lista_carregada = json.load(f_json)
            print("\nLista carregada com sucesso.\n")
            return (lista_carregada)
    except FileNotFoundError:
        print("\nArquivo não encontrado.")
        return (lista)


lista = []
pilha = []
while funfar:
    item = starting()

    if item == "listar":
        listar(lista)
    elif item == "desfazer":
        lista = undo_list(lista, pilha)
    elif item == "refazer":
        lista = redo_list(lista, pilha)
    elif item == "save":
        json_file_save(lista)
    elif item == "read":
        lista = json_file_read(lista)
    elif item == "exit":
        funfar = False
    elif item == "clear":
        os.system('clear')
    else:
        lista = additem(item, lista)
