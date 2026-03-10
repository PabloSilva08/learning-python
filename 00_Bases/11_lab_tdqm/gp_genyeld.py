l = ['a', 'b', 'c', 'd']

for i in l:
    print(i)

print()

def ft_yegen(l):
    for i in l:
        if i == 'c':
            return i
        else:
            yield i

k = (ft_yegen(l))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
