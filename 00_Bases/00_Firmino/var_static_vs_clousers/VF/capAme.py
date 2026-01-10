def wrapper():
    n: int = 0

    def sum_k(k: int):
        nonlocal n
        n = n + k
        print(f"Chamadas: {n}")

    return sum_k

soma_k = wrapper()

def nivel1() -> None:
    soma_k(3)


def nivel3() -> None:
    soma_k(5)


def nivel2() -> None:
    nivel3()


def main() -> int:
    nivel1()
    nivel2()

    return 0

if __name__ == "__main__":
    main()
    print(*globals(), sep='\n')
