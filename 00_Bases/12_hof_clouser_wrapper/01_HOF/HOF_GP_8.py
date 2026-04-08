# 1 - GPT
print("GPT = Nivel 05\n\n")

from typing import Callable, List
import math

lista_de_notas: List[float] = [6.0, 7.5, 8.0, 4.5, 9.0]

def aprovar_se_maior_ou_igual_6(nota: float) -> bool:
    return nota >= 6.0

def arredondar_para_cima(nota: float) -> float:
    return float(math.ceil(nota))

def processar_notas(transformar: Callable[[float], float], 
                    criterio: Callable[[float], bool], 
                    lista_de_notas: List[float]) -> list[float]:

    nova_lista_de_notas: List[float] = []
    lista_notas_aprovadas: List[float] = []

    for nota in lista_de_notas:
        nova_lista_de_notas.append(transformar(nota))

    for nota in nova_lista_de_notas:
        if criterio(nota):
            lista_notas_aprovadas.append(nota)

    return lista_notas_aprovadas

print(processar_notas(arredondar_para_cima, aprovar_se_maior_ou_igual_6, lista_de_notas))
