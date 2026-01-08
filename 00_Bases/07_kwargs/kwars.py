di = {'nume': 'Pablo', 'n_meio': 'Vieira', 'last': 'Silva'}

print('print normal ==>', di)

print('\n* ==>>', *di)
print('\n** ==>>', di.items())
print('-' * 40)

d1 = {**di}
print('\n', d1)

(d2, d3), *d4 = di.items()

print(d2, d3, d4)
