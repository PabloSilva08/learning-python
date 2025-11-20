import traceback
import sys

def ll():
    try:
        lis = [1, 2, 3]
        for i in range(len(lis) + 1):
            print(f'passei na ll() lis -> {lis[i]}')
    except IndexError as err:
        print(f'ERROOOO: {err}')
    print('Dentro de ll() e depois do execpt')

a = int(sys.argv[1])
try:
    b = 1/a

    print(f'b = {b}')

except ZeroDivisionError as erro:
    a = 4
    print('ERROR:', erro)
#    trace = traceback.format_exc()
#    print(trace)
    ll()
    print('Apos ll()')

else:
    print('To no else.')

finally:
    a = 2
    print('To no finally')

print(f'Eita porra a = {a}')


