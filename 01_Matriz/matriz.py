# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    matriz.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pvieira- <pvieira-@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/10/14 11:05:26 by pvieira-          #+#    #+#              #
#    Updated: 2025/10/20 22:00:44 by pvieira-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def array_row_constructor(line: int, column: int, len_element: int) \
        -> list[float]:
    mat_lin = []
    tmp: int = 0
    for m in range(column):
        tmp = input(f"Digite o elemento M_{line + 1}x{m + 1}: ")
        if ((vapo := len(tmp)) > len_element):
             len_element = vapo
        mat_lin.append(tmp)
    return (len_element, mat_lin)

def matriz_constructor(line: int, column: int) -> list[list[float]]:
    mat_tmp = []
    mat = []
    len_element = 0
    for i in range(line):
        len_element, mat_tmp = array_row_constructor(i, column, len_element)
        mat.append(mat_tmp)
    return (len_element, mat)

def left_bracket(i: int, line: int) -> None:
    c1 = '┌'
    c3 = '└'

    if i == 0:
        print(c1, end=' ')
    elif i != (line - 1):
        print("│", end=' ')
    else:
        print(c3, end=' ')

def right_bracket(i: int, line: int) -> None:
    c2 = '┐'
    c4 = '┘'
        
    if i == 0:
        print(f' {c2}', end='\n')
    elif i != (line - 1):
        print(" │", end='\n')
    else:
        print(f' {c4}', end='\n')

def print_matriz(line: int, column: int, matriz: list[list], len_element: int) \
        -> None:
    if (line == 1):
        print(f'[', end='')
        print(*matriz[0], sep=' ', end='')
        print(f']', end='')
    else:
        for i in range(line):
            left_bracket(i, line)
            print(*[f"{x:^{len_element}}" for x in matriz[i]], sep=' ', end=' ')
            right_bracket(i, line)

def main(argc: int, argv: list[str]) -> int:
    try:
        if (argc == 1):
            line = int(input("Digite o número de Linhas: "))
            column = int(input("Digite o número de colunas: "))
        elif (argc == 2):
            line = int(argv[1])
            column = int(input("Digite o número de colunas: "))
        else:
            line = int(argv[1])
            column = int(argv[2])

        if ((line < 1) or (column < 1)):
            sys.stderr.write("\033[91mLinha e colunas nao podem ser menores\
 que 1.\033[0m\n")
            return(1)

        matriz = []
        len_element, matriz = matriz_constructor(line, column)
        print_matriz(line, column, matriz, len_element)

    except ValueError:
        sys.stderr.write("\033[91mTem que ser digitado números inteiros.\
                         \033[0m\n")
        sys.exit(1)
    return (0)


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)


