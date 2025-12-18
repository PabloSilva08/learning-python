"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

#Fase de preparação
frase_secreta = input("Digite a palavra/frase que não contenha '*': ").lower()
frase_tmp = ''
for i in frase_secreta:
    if i == '*':
        print("O caracter '*' é proibido.")
        exit(1)
    frase_tmp += '*'
len_frase = len(frase_secreta)
os.system('clear')

#Fase do jogo
ver = True
contador = 0
while ver:
    tmp = ''
    letra = input(
        "Por favor digite uma letra ou '*' para finalizar: "
    ).lower()

    if (letra == '*'):
        print("Você finalizou o programa.")
        break
    if (len(letra) != 1):
        print("Por favor digite apenas uma letra.")
        continue

    contador += 1
    for i in range(len_frase):
        if (frase_tmp[i] == '*' and letra == frase_secreta[i]):
            tmp += frase_secreta[i]
        else:
            tmp += frase_tmp[i]

    if (tmp == frase_secreta):
        print(f"Parabens você descobriu a frase {tmp} em {contador} jogadas.")
        ver = False
    else:
        print(tmp)
        frase_tmp = tmp


