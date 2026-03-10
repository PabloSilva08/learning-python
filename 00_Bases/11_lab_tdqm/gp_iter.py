it_1 = ['a', 'b', 'c', 'd']

it = iter(it_1)

print(it)

while (True):
    try:
        print(next(it))
    except StopIteration:
        break


while (True):
    try:
        print(next(it))
    except StopIteration:
        break

print('1')


def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

# Testes esperados
print(is_iterable(123))    # False
print(is_iterable(range(3))) # True

