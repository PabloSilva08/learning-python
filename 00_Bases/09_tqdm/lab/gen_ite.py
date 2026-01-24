l1 = ['p', 'a', 'b', 'l', 'o']

print(f'l1, {type(l1)}')

l2 = [i for i in range(10)]

print(f'\nl2, {type(l2)}')

print('#' * 80)
print(f'\nr1, {type(range(10))}')

r2 = range(10)
print(f'\nr2, {type(r2)}, { r2 }')

print('#' * 80)
print('#' * 80)


l3 = iter(l1)
print('l1 ==>> ', l1)
print('l2 ==>> ', l2)
print('l3 ==>> ', l3,'||', type(next(l3)),'||', next(l3) )


print('#' * 80)
print('-' * 80)
print('#' * 80)

class Contador:
    def __init__(self, inicio, fim):
        self.atual = inicio
        self.fim = fim

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual > self.fim:
            raise StopIteration

        valor = self.atual
        self.atual += 1
        return valor


c1 = Contador(1, 5)

g1 = (i for i in range(1, 10))
print(g1)

def contadory(inicio, fim):
    atual = inicio
    while atual <= fim:
        yield atual
        atual += 1

c2 = contadory(1, 5)
print('#' * 80)
print(type(c1),'||',  c1)
print(type(c2),'||',  c2)
