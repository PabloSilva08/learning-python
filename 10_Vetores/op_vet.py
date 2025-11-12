def soma_vet(V1 :list[float], V2 :list[float]) -> list[float]:
    ln :int = len(V1)
    VF :list[float] = []
    for i in range(ln):
        VF.append(V1[i] + V2[i])
    return(VF)

def pro_escalar_vet(escalar :float, V1 :list[float]) -> list[float]:
    return[escalar * vf  for vf in V1]

def subtracao_vet(V1 :list[float], V2 :list[float]) -> list[float]:
    return(soma_vet(V1, pro_escalar_vet(-1, V2)))

if __name__ == '__main__':
    VA = [1 ,3, 8, -9]
    VB = [-3, 4, 0, -1]
    esc = 2

    print('VA = ', VA)
    print('VB = ', VB)

    print('-' * 80)
    print('Soma = ', soma_vet(VA, VB))
    print(f'Produto escalar {esc} * {VA} = ', pro_escalar_vet(esc, VA))
    print('Subtracao = ', subtracao_vet(VA, VB))
