l = ['a', 'b', 'c', 'd']

for i in l:
    print(i)

print()

def ft_yegen(l):
    for i in l:
        if i == 'c':
            yield "Imprimindo o c" 
#            return i
        else:
            yield i

k = (ft_yegen(l))
print(next(k))
print(next(k))
print(next(k))
print(next(k))

print("-"*40)
print("-"*40)
print()


def tap(iterable):
    for item in iterable:
        print(f"Log: Processando item -> {item}")
        yield item

# Testando o comportamento "pass-through"
# Podemos até encadear com o exercício anterior!
numeros = [10, 20, 30]
fluxo = tap(numeros)

for valor in fluxo:
    # O valor chega aqui após ser impresso dentro da função tap
    print(f"Recebido no loop final: {valor}")
