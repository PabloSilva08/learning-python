lista = [1,2,3,4]

for i in lista:
    print(i)

print('-'*80)
for i in lista:
    print(i)

it1 = iter(lista)
it2 = iter(lista)

print('-'*80)

for i in it1:
    print("1 it1",i)

for i in it1:
    print("2 it1",i)

print('-'*80)

for i in it2:
    print("1 it2",i)

for i in it2:
    print("2 it2",i)

ge1 = (x**2 for x in lista)
print('-'*80)

for i in ge1:
    print("2 ge1",i)
for i in ge1:
    print("2 ge1",i)
