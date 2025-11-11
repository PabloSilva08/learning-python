def print_vet(V :list[float]) -> None:
    print(V)

def soma_vet(V1 :list[float], V2 :list[float]) -> list[float]:
    ln :int = len(V1)
    VF :list[float] = []
    for i in range(ln):
        VF.append(V1[i] + V2[i])
    return(VF)

def subtracao_vet(V1 :list[float], V2 :list[float]) -> list[float]:
    pass

if __name__ == '__main__':
    VA = [1 ,3, 8, 9]
    VB = [-3, 4, 0, -1]

    print_vet(VA)
    print_vet(VB)

    print(soma_vet(VA, VB))
