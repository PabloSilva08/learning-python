"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
###############################################################################
###############################################################################

def finaly_value(value: int) -> int:
    value *= 10
    if (v := value % 11) > 9:
        return (0)
    else:
        return (v)

def calculating_the_eleventh(cpf: str) -> int:
    matrix = cpf[:10]
    
    i = 11
    value = 0
    for number in matrix:
        value += int(number) * i
        i -= 1
    return(finaly_value(value))

def calculating_the_tenth(cpf: str) -> int:
    matrix = cpf[:9]
    
    i = 10
    value = 0
    for number in matrix:
        value += int(number) * i
        i -= 1
    return(finaly_value(value))

def simplified_cpf(cpf: str) -> str:
    return(cpf[:3]+cpf[4:7]+cpf[8:11]+cpf[12:])

def validate_cpf_mask(cpf: str) -> bool:
    cpf_char: bool = cpf[3] == '.' and cpf[7] and cpf[11] == '-'
    cpf_numb: bool = cpf[:3].isdigit() and \
                     cpf[4:7].isdigit() and \
                     cpf[8:11].isdigit() and \
                     cpf[12:].isdigit()
    if (cpf_char) and (cpf_numb):
        return(True)
    return(False)

def cpf_treatment(cpf: str, len_cpf: int) -> bool:

    if (len_cpf == 11 and cpf.isdigit()):
        return(True)
    elif (len_cpf == 14 and validate_cpf_mask(cpf)):
        return(True)
    return(False)

if __name__ == '__main__':
    cpf: str = input('Enter a CPF number: ')
    len_cpf: int = len(cpf)
    checked_treatment: bool = cpf_treatment(cpf, len_cpf)

    if checked_treatment:
        if len_cpf == 14:
            cpf = simplified_cpf(cpf)
        digit_10: int = calculating_the_tenth(cpf)
        print(digit_10)
        digit_11: int = calculating_the_eleventh(cpf)
        print(digit_11)
#        print("O cpf simplioficado é ", cpf)
    else:
        print("O cpf não cumpre os pre-requisitos básicos.")
