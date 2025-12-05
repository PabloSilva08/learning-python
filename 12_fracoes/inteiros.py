import sys

def fatores_primo(num: int) -> list[int]:
    fatores_primos = []
    if num == 1:
        return(1)
    if num < 1:
        return(0)
    n = num
    i = 2
    while (i <= num):
        if ((n % i) == 0):
            fatores_primos.append(i)
            n = n / i
            continue
        i += 1
    return(fatores_primos)

if '__main__' == __name__:
    num = int(sys.argv[1])
    fatores = fatores_primo(num)
    print(fatores)
