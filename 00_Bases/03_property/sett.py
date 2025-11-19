class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = float(preco)
        self._preco2 = float(preco)

    @property
    def preco(self):
        return (self._preco)

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self._preco = float(novo_preco)

    @property
    def preco2(self):
        return (self._preco2)

    #sem o preco.setter ele nao joga o preco 3 para cá
    def preco2(self, novo_preco):
        if novo_preco > 0:
            self._preco2 = float(novo_preco)

p1 = Produto("Teclado", 100)
p1.preco = 10
print(f'{p1._nome} - R$ {p1.preco}')

p1.preco = -100
p1._nome = 'Chip7'
print(f'{p1._nome} - R$ {p1.preco}')

p1._preco = -100
p1._nome = 'Chip7'
print(f'{p1._nome} - R$ {p1.preco}')
print('-' * 80)


p1.preco2 = 10
print(f'{p1._nome} - R$ {p1.preco2}')

p1.preco2 = -100
print(f'{p1._nome} - R$ {p1.preco2}')

p1._preco2 = -100
print(f'{p1._nome} - R$ {p1.preco2}')
print('-' * 80)
