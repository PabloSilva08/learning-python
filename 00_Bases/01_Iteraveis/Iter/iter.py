L1 = ['a', 'b', 'c', 'd']

print(L1)
print('#' * 79)

g1 = iter(L1)
g2 = iter(L1)

print(next(g1))
print(next(g1))
print(next(g2))

print('#' * 79)
print('#' * 79)

for i in g2:
    print(i)

print('-' * 79)

for i in g1:
    print(i)
