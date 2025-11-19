a = 0 
try:
    b = 1/a

    print(f'b = {b}')

except Exception as erro:
    a = 4
    print('ERROR:', erro)

else:
    print('To no else.')

finally:
    a = 2
    print('To no finally')

print(f'Eita porra a = {a}')



#while (a == True):
#    se = input('Insira a senha: ')
#    if se == 'ab':
#        print('Login feito')
#        a = False
#    else:
#        print('senha incorreta')
