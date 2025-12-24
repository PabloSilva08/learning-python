'''
Listas
1 - append, insert, pop, del, clear, extend
'''

def print_arr(A, ls):
    if (A == 'Dicionario'):
        for key, value in ls.items():
            print(f'Dict[{key}] = {value}')
    else:
        for L in range(len(ls)):
            print(f'{A}[{L}] = {ls[L]}')


print("\nListas\n")

L1 = ['A', 'B', 'C', 'D','E', 'F']
L2 = ['E', 'F', 'G', 'H','I', 'J']
L3 = L1 + L2

print(f'L1 => ',L1)
print(f'L2 => ',L2)
print(f'L3 = L1 + L2 => ',L3)

"slicing"
print('\n----Slicing----\n')
print('L3[1:3]   => ', L3[1:3])
print('L3[1:8:2] => ', L3[1:8:2])
print("--------------------------------------------------------------------------------\n")

print('\n----Desempacotnado e mudando o sep ----\n')
print('L1 =>', *L1, sep=' - ')
print('L2 =>', *L2, sep=' - ')
print('L3 =>', *L3, sep=' - ')
print("--------------------------------------------------------------------------------\n")

print('\n----Print com For----\n')
print_arr('Lista', L3)
print("--------------------------------------------------------------------------------\n")

print('\n----Methodos da Lista----\n')
L4 = ['K', 'L', 'M']
print(f'L4 => {L4}', end='\n\n')

L4.extend(L1)
print(f'L4.extend(L1) => {L4}', end='\n\n')

L4.append('P')
print(f'L4.append("P") => {L4}', end='\n\n')

L4.insert(2,'Amor')
print(f'L4.insert(2, <algo> => ) {L4}', end='\n\n')

L4.pop()
print(f'L4.pop() => ) {L4}', end='\n\n')

del(L4[2:5])
print(f'del(L4[2:5]) => ) {L4}', end='\n\n')

L5 = list(range(1,10))
print(f'list(range(1,10)) => {L5}', end='\n\n')

L5.clear()
print(f'L5.clear() => {L5}')

print("--------------------------------------------------------------------------------\n")

print('\n----Estudo com ids----\n')

print(f'id(L1) = {id(L1)} ==>> {L1} \t\t\t\t   ||| id(L1[1]) = {id(L1[1])} id(L1[2] = {id(L1[2])})')
L1[1] = 'b'
print(f'id(L1) = {id(L1)} ==>> {L1} \t\t\t\t   ||| id(L1[1]) = {id(L1[1])} id(L1[2] = {id(L1[2])})')
print(f'id(L3) = {id(L3)} ==>> {L3} ||| id(L3[1]) = {id(L3[1])} id(L3[2] = {id(L3[2])})')

print("-" * 136, '\n\n')
print("#" * 80)
print("--------------------------------------------------------------------------------\n")
print('\nTuplas\n')

T1 = ('a', 'b', 'c', 'd')
T2 = ('c', 'd', 'e', 'f')
T3 = T1 + T2
print(f'T1 = {T1}')
print(f'*T2 = ', *T2)
print(f'T3 = {T3}')
print("--------------------------------------------------------------------------------\n")

print('\n----Print com For----\n')

print_arr('Tupla', T1)

print("--------------------------------------------------------------------------------\n\n")
print("#" * 80)
print("-" * 80)
print('\nDicionario\n')

D1 = {'Pablo': 'Bonitao', 'Liz': 'Princesa', 'Larissa': 'Amor Lindona'}
D2 = dict(Flamengo = 'Melhor do Mundo', Vasco='Segunda divisao', Botafogo="É Bairro")

print(f'D1 = {D1}', end='\n\n')
print(f'D2 = {D2}', end='\n\n')
print(f'*D2 = ', *D2, end='\n')
print("--------------------------------------------------------------------------------\n")

print('\n----Adicionando chave valor----\n')
D2['Fluminense'] = 'É Fruta'
print(f'D2["Fluminense"] = "É Fruta" ==> {D2}', end='\n')
print("--------------------------------------------------------------------------------\n")

print('\n----Update e print com For----\n')
D2.update({'51':'É pinga'})
print_arr('Dicionario', D2)
print("--------------------------------------------------------------------------------\n")

print('\n----del D2[51]----\n')
del D2['51']
print(f'D2 = {D2}')
print("--------------------------------------------------------------------------------\n\n")

print('----Pesquisa Key - Value in D1----\n')
print('Pablo' in D1)
print('Pablo' in D1.keys())
print('Bonitao' in D1.values())

print("--------------------------------------------------------------------------------\n\n")
print("#" * 80)
print("-" * 80, '\n')

print('\nSet\n')

S1 = {'a', 'b', 'c', 'd'}
S2 = set('')
S2.add('f')

print('S1 ==> ', S1)
print('S2 ==> ', S2)
print("--------------------------------------------------------------------------------\n")

print('\n---ids do set----\n')

print('Os set não possui indice, logo não é possivel acessar diretamente. Somente pela iteração.')
print('Não possuimos poder sobre a ordenação do set.\n')
for s in S1:
    print(f'{s} = id({id(s)})')
print("--------------------------------------------------------------------------------\n\n")

print('\n---Adicionar e remover elementos----\n')

S2.add('g')
S2.add('h')
print('S2 ==> ', S2)
S2.discard('h')
print('S2 ==> ', S2)
S2.update('hij')
print('S2 ==> ', S2)
print("--------------------------------------------------------------------------------\n")

print('\n---União e intercessão----\n')
S1 = set('abc')
S2 = set('bcd')

print('S1 ==> ', S1)
print('S2 ==> ', S2)

S3 = S1 | S2
S4 = S1 & S2

print('\nS3 = S1 | S2 ==> ', S3)
print('S4 = S1 & S2 ==> ', S4)

S5 = S1 - S2
S6 = S2 - S1

print('\nS5 = S1 - S2 ==> ', S5)
print('S6 = S2 - S1 ==> ', S6)

S7 = S1 ^ S2
print('\nS7 = S1 ^ S2 ==> ', S7)
print("--------------------------------------------------------------------------------\n")
