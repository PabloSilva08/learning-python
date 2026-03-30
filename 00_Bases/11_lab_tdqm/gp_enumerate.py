lista = ["a", "b", "c"]

for x, y in enumerate(lista, start=2):
    print(x, y)

def find_first_index(string, char):
    for x, y in enumerate(string):
        if char == y:
            return (x)
    return(-1)

enc = find_first_index("Pablo Vieira", "P")
print(enc)
