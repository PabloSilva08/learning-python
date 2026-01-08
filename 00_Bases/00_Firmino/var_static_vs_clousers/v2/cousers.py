
def nivel5() -> int:
    def somando(k):
        def parcela(n):
            return (n + k)
        return parcela

    soma_k1 = somando(0)
    soma_k2 = somando(10)
    print(*dir(soma_k2), sep='\n')

    print((soma_k1(3), soma_k2(5)))

def nivel4():
    nivel5()

def nivel3():
    nivel4()
    
def nivel2():
    nivel3()

def nivel1():
    nivel2()


if __name__ == "__main__":
    nivel1()
    nivel1()















