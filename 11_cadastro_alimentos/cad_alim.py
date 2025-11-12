import sys

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
BOLDRED = "\033[1m\033[31m"
BOLDGREEN =  "\033[1m\033[32m"
BOLDYELLOW =  "\033[1m\033[33m"
BOLDBLUE = "\033[1m\033[34m"
BOLDMAGENTA = "\033[1m\033[35m"
BOLDCYAN = "\033[1m\033[36m"
BOLDWHITE = "\033[1m\033[37m"
RESET = '\033[0m'

def print_lista(lista :list[str]) -> None:
    for l in lista:
        print(l, end='')

def listar_item(lista :list[str]) -> None:
    for l in range(len(lista)):
        print(f'{l + 1} {lista[l]}', end='')

def ler_lista(arq :str) -> list[str]:
    lista :list[str] = []

    with open(arq, 'r') as arq:
        lista = arq.readlines()
    return(lista)

def adicionar_lista(arq :list[str], item :str) -> None:
    with open(arq, 'a') as arq:
        arq.write(f"- {item.capitalize()}\n")

def dont_exist_in_the_list(arq :list[str], item :str) -> bool:
    lista = ler_lista(arq)
    for l in lista:
        if (f'- {item}' == l.strip().lower()):
            return(False)
    return(True)

def escrever_lista(arq :str) -> None:
    item = input(f'{BOLDCYAN}Digite o alimento:{RESET} ')
    item = item.strip().lower()

    if (item == ''):
        print(f'{BOLDRED}----Item não adicionado.----{RESET}')
    elif dont_exist_in_the_list(arq, item):
        adicionar_lista(arq, item)
        print(f'{BOLDGREEN}Item adicionado com sucesso.{RESET}')
    else:
        print(f'{BOLDRED}----Item já existe.----{RESET}')

def retirar_item(arq) -> None:
    r_item = int(input(f'{BOLDCYAN}Digite o número do item a ser retirado:{RESET} '))
    lista = ler_lista(arq)

    if ((r_item > 0) and (r_item <= len(lista))):
        del(lista[r_item - 1])
        with open(arq, 'w') as arq:
            arq.writelines(lista)
    else:
        print(f'{BOLDRED}O número digitado não foi encontrado.{RESET}')

if __name__ == '__main__':
    arq = 'Lista.txt'
   
    try:
        print('* Imprmindo a lista.\n')
        lista = ler_lista(arq)
        print_lista(lista)
        print('-' * 40)

        print('* Escrevendo na lista.\n')
        escrever_lista(arq)
        lista = ler_lista(arq)
        print()
        print_lista(lista)
        print('-' * 40)
         
        print('* Retirar item da lista.\n')
        lista = ler_lista(arq)
        listar_item(lista)
        retirar_item(arq)
        lista = ler_lista(arq)
        print()
        listar_item(lista)
        print('-' * 40)

    except IndexError as error:
        print(f'{BOLDRED}-----{error}-----{RESET}')
