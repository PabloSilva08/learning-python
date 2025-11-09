def print_vet(V :list[float]) -> None:
    print(V)

def soma_vet(V1 :list[float], V2 :list[float]) -> list[float]:
    ln = len(V1)
#    if ln != len(V2):
#        return (False)

    VF = []
    for i in range(ln):
        VF.append(V1[i] + V2[i])
    return(VF)

if __name__ == '__main__':
    VA = [1 ,3, 8]
    VB = [-3, 4]

    print_vet(VA)
    print_vet(VB)

    print(soma_vet(VA, VB))
