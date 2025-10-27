import sys
import os 
import random 

def number_insertion(argc:int, argv: list[str], number) -> int:
    if (argc >= 2):
        if int(argv[1]) == -1:
            number = random.randint(0, 100)
        else:
            number = int(argv[1])
    else:
        number = int(input("Insira um número natural entre 0 a 100 para ser \
 encontrado: "))
    return(number)

def search_number(number) -> None:
    count:int = 1
    x = int(input(f"({count}) Insira um número natural entre 0 a 100: "))
    while (x != number):
        count += 1
        if (x < number):
            x = int(input(f"({count}) Insira um número maior: "))
        else:
            x = int(input(f"({count}) Insira um número menor: "))
    print(f'Parabéns o número {x} foi encontrado em {count} tentativas.')

def main(argc: int, argv: list[str]) -> int:
    number: int = 0
    try:
        number = number_insertion(argc, argv, number)
        os.system('clear')

        if ((number < 0) or number > 100):
            print(f'O número {number} não está entre 0 e 100')
            return(1)
        search_number(number)
    except ValueError:
        sys.stderr.write("(ERRO):  Insira um valor natural entre 0 a 100.\n")

    return(0)


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
