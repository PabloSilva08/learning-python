"""
Implemente um programa que dá um desconto de 12% sobre o preço de um item à 

venda, exibindo o valor final e o desconto.
"""

valor = float(input('Insira o Valor: '))
fator = float(input('Insira o fator de acrescimo ou decrescimo: '))
calc = valor * fator
print(f'O {valor} * {fator} = {calc}')

