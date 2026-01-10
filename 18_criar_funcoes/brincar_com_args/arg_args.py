
def saudar(*msg, **sg):
#    print(f'{msg[0]} {msg[1]} meu {msg[2]} {sg['nome']} {sg['sob']}')
    k = list(sg.values())
    print(f'{msg[0]} {msg[1]} meu {msg[2]}', *k)

if __name__ == '__main__':
    li = ['Bom', 'dia', 'amigo']

    di = {'nome': "Carlos", 'sob': 'Doria' }

    saudar(*li, **di)

    saudar(*li)
    di2 = dict()
    print(di2)
