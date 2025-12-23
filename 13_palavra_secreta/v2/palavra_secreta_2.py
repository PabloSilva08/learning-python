import os
from color_format import *

def char_revealed(texto_secreto: str, letras_certas: str) -> str:
    t_oculto: str = ""
    for ts in texto_secreto:
        if ts in letras_certas:
            t_oculto += ts
        else:
            t_oculto += '*'
    return(t_oculto)

def declaration(texto_oculto: str, letras_erradas: str) -> None:
    print(f'{BOLDRED}Letras erradas = {letras_erradas}{RESET}')
    print(texto_oculto)

def finaly(texto_oculto: str, count: int) -> None:
    print(f'{BOLDCYAN}Parabéns você acertou ==>> {texto_oculto}')
    print(f'Levou {count} tentativas.{RESET}')

if __name__ == '__main__':
    letras_certas: list[str] = []
    letras_erradas: list[str] = []

    texto_secreto: str = input("Digite o texto secreto: ").lower()
    os.system('clear')
    if (len(texto_secreto) < 2):
        texto_secreto = "Pablo Vieira".lower()
    ver: bool = True
    count: int = 0
    texto_oculto: str = ""

    while ver:
        count += 1
        letras_totais: list[str] = letras_certas + letras_erradas
        caracter = input(f"\n{count} - Por favor digite um caracter ou '*' para desistir: ").lower()
        if caracter == '*':
            print(f'{BOLDRED}Você desisitiu.{RESET}')
            exit(1)
        if (len(caracter) > 1):
            if caracter == texto_secreto:
                texto_oculto = caracter
                finaly(texto_oculto, count)
                break
            else:
                count = len(caracter * 2)
                continue
        if caracter in  letras_totais:
            declaration(texto_oculto, letras_erradas)
            continue
        elif caracter in texto_secreto:
            letras_certas.append(caracter)
            texto_oculto = char_revealed(texto_secreto, letras_certas)
            declaration(texto_oculto, letras_erradas)
        else:
            letras_erradas.append(caracter)
            declaration(texto_oculto, letras_erradas)
        if texto_oculto == texto_secreto:
            finaly(texto_oculto, count)
            break
    print('FIM')
