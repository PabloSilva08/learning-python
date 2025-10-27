import sys

def number_insertion(argc: int, argv: list[str]) -> int:
    if (argc >= 2):
        number = int(argv[1])
    else:
        number = int(input("Insira um número positivo: "))
    return (number)

def fat_iterativo(number: int) -> None:
    val = inter = number
    while inter > 1:
        number = number * (inter - 1)
        inter = inter - 1
    print(f'!{val} = {number}')

def fat_recursivo(number: int) -> int:
    if (number == 1):
        return (1)
    else:
        number = number * (fat_recursivo(number - 1))
    return(number)

def main(argc: int, argv: list[str]) -> int:
    number: int = 0

    try:
        number = number_insertion(argc, argv)
        if number < 0:
            print("Por favor insira um número positivo.")
            exit (1)
        elif number == 0:
            print(f'!0 = 1')
        else:
            print("Modo Iterativo\n")
            fat_iterativo(number)
            print("----------------------------------\n")
            print("Modo Recursivo\n")
            print(f'!{number} = {fat_recursivo(number)}')
    except ValueError:
         sys.stderr.write("\033[91mTem que ser digitado números inteiros.\
                         \033[0m\n")
    return (0)


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

