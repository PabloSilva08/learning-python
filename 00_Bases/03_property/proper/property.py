class Produto:
    def __init__(self, nome, valor):
        self._nome = nome
        self._valor = valor

    @property
    def nome(self):
        return(self._nome)

    @property
    def valor(self):
        print('Getter no valor.')
        return(self._valor)

    @valor.setter
    def valor(self, valor):
        if (valor > 500):
            print ("Valor muito alto. Setando 500.")
            self._valor = 500
        else:
            self._valor = valor

###############################################################################

p1 = Produto("bala", 100)

print(f'p1.nome = {p1.nome}\n')
print(f'p1.valor = {p1.valor}\n')

print('-', '#' *79)

print("\n\nTrocanco valor para 200\n")


p1.valor = 200
print(f'p1.nome = {p1.nome}')
print(f'p1.valor = {p1.valor}')

print('-', '#' *79)

print("\n\nTrocanco valor para 600\n")


p1.valor = 600
print(f'p1.nome = {p1.nome}')
print(f'p1.valor = {p1.valor}')

print('-', '#' *79)

print("\n\nTrocanco o nome\n")

print(f'p1.valor = {p1.valor}')
try:
    p1.nome = 'Anderson'
    print(f'p1.nome = {p1.nome}')
except AttributeError as e:
    print(f'\nNome não possui setter. {e}')
