'''
Dada uma string com uma única letra e uma outra string qualquer,  responda
quantas vezes a letra está presente na outra string. Exemplos:Exemplos

    “a”; “abacaxi”: 3
    “c”; “bola”: 0
    “u”; “”: 0
'''
string = input('Insert the word or phrase: ')
c = input('Insert the character: ')
count = 0

for ch in string:
    if c == ch:
        count += 1

print(f"The '{c}' appers {count} times.")

'''
Ainda considerando uma string com uma única letra e uma outra string qualquer,
responda com uma lista de índices indicando as posições em que a letra está 
presente.Exemplos:

    “a”; “abacaxi”: [0, 2, 4]
    “c”; “bola”: []
    “u”; “fuleiro”: [1]
'''
l = []
for i in range(len(string)):
    if c == string[i]:
        l.append(i)

print(l)
