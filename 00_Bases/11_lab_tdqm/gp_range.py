# O range é considerado preguiçoso por que ele nao gera de uma vez todos os elementos da sequencia na memoria.

#Ex_01 
print('Exercício 01')
print(len(range(5)), '\n')

#Ex_02
print('Exercício 02')
r = range(10, 20)
count = 0
for i in r:
    count += 1
    print(i)
    if (count == 3):
        break
print()

#Ex_03
print('Exercício 03')
r = len(range(5, 30, 5))
print(r,'\r')


#Ex_04
print('Exercício 04')
def f_len_range(start, stop, step=1):
    if step == 0:
        return 0
    return (len(range(start, stop, step)))

print(f_len_range(0, 10, 2))
