class Conta:
    def __init__(self, saldo):
        self._saldo1 = saldo
        self._saldo2 = saldo

    @property
    def saldo1(self):
        return self._saldo1

    def saldo2(self):
        return self._saldo2


s1 = Conta(200)
print(f"Saldo1 = {s1.saldo1}")
print(f"Saldo2() = {s1.saldo2()}")
print(f"Saldo2 = {s1.saldo2}")

###############################################################################

print('-' * 80)
s1._saldo1 = 10
s1._saldo2 = 20
print(f"Saldo1 = {s1.saldo1}")
print(f"Saldo2() = {s1.saldo2()}")
print(f"Saldo2 = {s1.saldo2}")

###############################################################################

print('-' * 80)
try:
    s1.saldo1 = 30
except AttributeError as err:
    print(f's1.saldo1 = 30 ==>> {err}')
else:
    print(f"Saldo1 = {s1.saldo1}")

s1.saldo2 = 40
try:
    print(f"Saldo2() = {s1.saldo2()}")
except TypeError as err:
    print(f"print do s1.saldo2 = 40 ==>> {err}")
else:
    print(f"Saldo2 = {s1.saldo2}")

