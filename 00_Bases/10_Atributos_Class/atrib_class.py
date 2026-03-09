class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

        def ano_de_nascimento(self):
            return(Pessoa.ano_atual - self.idade)




p1 = Pessoa('Joao', 20)
p2 = Pessoa('Maria', 20)
p3 = Pessoa('Marta', 20)


print('p1 ano atual = ', p1.ano_atual)
print('p2 ano atual = ', p2.ano_atual)
print('p3 ano atual = ', p3.ano_atual)

p1.ano_atual = 1990

print()
print('p1 ano atual = ', p1.ano_atual)
print('p2 ano atual = ', p2.ano_atual)
print('p3 ano atual = ', p3.ano_atual)

Pessoa.ano_atual = 2000

print()
print('p1 ano atual = ', p1.ano_atual)
print('p2 ano atual = ', p2.ano_atual)
print('p3 ano atual = ', p3.ano_atual)
