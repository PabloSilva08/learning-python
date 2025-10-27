# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    is_number.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pvieira- <pvieira-@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/10/26 15:09:07 by pvieira-          #+#    #+#              #
#    Updated: 2025/10/26 16:04:18 by pvieira-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def ft_isnumber(number: str) -> bool:
    number = number.strip()
    if not number:
        return(False)
    if ((number[0] == '-') or (number[0] == '+')):
        number = number[1:]
    if number.isdigit():
        return (True)
    
    list_number = number.split('.')
    if(len(list_number) == 2):
        if(list_number[0].isdigit() and list_number[1].isdigit()):
            return(True)
    return(False)

def main(argc: int, argv: list[str]):
    if (argc < 2):
        number = input("Enter the number: ")
    else:
        number = argv[1]

    print(ft_isnumber(number))

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
