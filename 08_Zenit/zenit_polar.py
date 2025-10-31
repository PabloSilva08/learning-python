import sys

def zenit_polar(my_str: str) -> str:
    len_str = len(my_str)
    zp = "zenitpolarZENITPOLAR"
    pz = "polarzenitPOLARZENIT"
    str_result = ''
    for s in my_str:
        if s in zp:
            index = zp.index(s)
            str_result += pz[index]
        else:
            str_result += s
    return (str_result)

def arq_zp(arq: str) -> str:
    with open(arq, 'r') as arq:
        msg = arq.read()
    print(msg)
    print('---------')
    msg = zenit_polar(msg)
    print(msg)

def term_zp(argc: int, argv: list[str]) -> int:
    line = ''
    my_str = ''
    if argc < 2:
        count = 0
        print("Digite o texto.\n")
        while True:
            line = input()
            if line == '':
                count += 1
            else:
                count = 0
            if count == 2:
                break
            my_str += line + '\n'
    elif argc == 2:
        my_str += argv[1] + '\n'
    else:
        sys.stderr.write("Insira apenas um argumento.\n")

    print('----------------\n')
    my_str = zenit_polar(my_str)
    print(my_str, end='')
    return (0)

def main_header() -> str:
    string = '''
        Escolha uma opção

    (1) - Digitar um texto.
    (2) - Escolher um arquivo.

    Digite algo diferente para sair.
    '''
    return(string)

if __name__ == "__main__":
    argc = len(sys.argv)
    argv = sys.argv

    if (argc == 2):
        try:
            arq_zp(argv[1])
        except:
            print(zenit_polar(argv[1]))
    elif (argc < 2):
        option = input(main_header())
        if (option == '2'):
            option = input('Digite o nome do arquivo.\n')
            try:
                option = arq_zp(option)
            except(FileNotFoundError):
                print(f'O arquivo {option} não foi encontrado.')
        elif (option == '1'):
           term_zp(argc, argv) 
    else:
        print('Por favor insira apenas um ou nenhum argumento.')
