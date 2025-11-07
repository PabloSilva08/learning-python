'''
Listas
1 - append, insert, pop, del, clear, extend
'''

def print_arr(A, ls):
    for L in range(len(ls)):
        print(f'{A}[{L}] = {ls[L]}')


print("\nListas\n")

L1 = ['A', 'B', 'C', 'D','E', 'F']
L2 = ['E', 'F', 'G', 'H','I', 'J']
L3 = L1 + L2
"slicing"
print(L3[1:3])
print(L3[1:8:2])

print("-----------------------------------------------------------")
print('L1 =>', *L1, sep=' - ')
print('L2 =>', *L2, sep=' - ')
print('L3 =>', *L3, sep=' - ')
print("-----------------------------------------------------------")

print_arr('Lista', L3)

print("-----------------------------------------------------------")
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
print(f'list(range(1,10)) => {L5}')
