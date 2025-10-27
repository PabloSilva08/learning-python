import sys

def check_prime_number(arg) -> bool:
    if (arg < 2):
        return(False)
    if arg == 2:
        return(True)
    if (arg % 2 == 0):
        return(False)

    i = 3
    while(i * i <= arg):
        if (arg % i == 0):
            return (False)
        i += 2
    return(True)




if __name__ == '__main__':
    argc = len(sys.argv)
    argv = sys.argv

    if (argc >= 2):
        if not argv[1].strip().isdigit():
            print("ERROR: Numero náo é inteiro")
        else:
            argv = int(argv[1])
    else:
        argv = int(input('Insira um número Inteiro: '))
    if check_prime_number(argv):
        print(f'O {argv} é primo.')
    else:
        print(f'O {argv} não é primo.')

#    print("\n--------------------------\n")
#    for i in range(100):
#        if check_prime_number(i):
#            print(f'O {i} é primo.')
#        else:
#            print(f'O {i} não é primo.')
