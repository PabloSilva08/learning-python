class Conta:
    def __init__(self):
        self._depositos = []
        self._saques = []

    def depositar(self, valor):
        self._depositos.append(valor)

    def sacar(self, valor):
        self._saques.append(valor)

    def saldo2(self):
        return sum(self._depositos) - sum(self._saques)

    @property
    def saldo(self):
        return sum(self._depositos) - sum(self._saques)

conta = Conta()
conta.depositar(100)
conta.sacar(40)
print(conta.saldo) # imprime 60
print(conta.saldo2()) 
print('-'*80)
try:
    conta.saldo2 = 20
    print(conta.saldo2) 
except:
    print('Deu ruim no conta.saldo2')
print('-'*80)
try:
    conta.saldo = 30
#    print(conta.saldo) 
except AttributeError as err:
    print(f'Deu ruim no conta.saldo ==> {err}')
print('-'*80)
try:
    print(conta.saldo2()) 
except TypeError as err:
    print(f'Deu ruim no conta.saldo2() ==> {err}')
