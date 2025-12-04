import sys

def fator_primo(num: int) -> list[int]:
    ft = []
    if num == 1:
        return(1)
    if num < 1:
        return(0)
    for i in range(2, num):
        if ((num % i) == 0):
            ft.append(i)
            num = num / i
            continue

if '__main__' == __name__:
    num = sys.argv[1]
    fator = ft_fator_primo(num)
