
def nivel1() -> int:
    def somando(k):
        def parcela(n):
            return (n + k)
        return parcela

    soma_k1 = somando(0)
    soma_k2 = somando(10)

    print((soma_k1(3), soma_k2(5)))
#    return((soma_k1, soma_k2))
    
def nivel3():
    nivel1()
#    a, b = nivel1()
 #   print(a(3), b(5))


def nivel2():
    nivel3()


if __name__ == "__main__":
#    a0, b0 = nivel1()
    nivel1()
#    print(a0(5), b0(5))
    nivel2()















