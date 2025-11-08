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
"slicing"
print(L3[1:3])
print(L3[1:8:2])

print("-----------------------------------------------------------------------")
print('L1 =>', *L1, sep=' - ')
print('L2 =>', *L2, sep=' - ')
print('L3 =>', *L3, sep=' - ')
print("-----------------------------------------------------------------------")

print_arr('Lista', L3)

print("-----------------------------------------------------------------------")
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
print(f'del(L4[3:5]) => ) {L4}', end='\n\n')

L5 = list(range(1,10))
print(f'list(range(1,10)) => {L5}', end='\n\n')

L5.clear()
print(f'L5.clear() => {L5}', end='\n\n')

print("-----------------------------------------------------------------------")

print(f'id(L1) = {id(L1)} ==>> {L1} ||| id(L1[1]) = {id(L1[1])} id(L1[2] = {id(L1[2])})')
L1[1] = 'b'
print(f'id(L1) = {id(L1)} ==>> {L1} ||| id(L1[1]) = {id(L1[1])} id(L1[2] = {id(L1[2])})')
print(f'id(L3) = {id(L3)} ==>> {L3} ||| id(L3[1]) = {id(L3[1])} id(L3[2] = {id(L3[2])})')

print("-----------------------------------------------------------------------")
print("-----------------------------------------------------------------------")
print('\nTuplas\n')

T1 = ('a', 'b', 'c', 'd')
T2 = ('c', 'd', 'e', 'f')
T3 = T1 + T2
print(f'T1 = {T1}')
print(f'*T2 = ', *T2)
print(f'T3 = {T3}')

print_arr('Tupla', T1)

print("-----------------------------------------------------------------------")
print("-----------------------------------------------------------------------")
print('\nDicionario\n')

D1 = {'Pablo': 'Bonitao', 'Liz': 'Princesa', 'Larissa': 'Amor Lindona'}
D2 = dict(Flamengo = 'Melhor do Mundo', Vasco='Segunda divisao', Botafogo="É Bairro")
#D3 = D1 + D2
print(f'D1 = {D1}', end='\n\n')
print(f'D2 = {D2}', end='\n\n')
print(f'*D2 = ', *D2, end='\n\n')
D2['Fluminense'] = 'É Fruta'
print(f'D2 = {D2}', end='\n\n')
D2.update({'51':'É pinga'})
print_arr('Dicionario', D2)
del D2['51']
print(f'\nD2 = {D2}', end='\n\n')

print('Pablo' in D1)
print('Pablo' in D1.keys())
print('Bonitao' in D1.values())

