import sys

argv = sys.argv
argc = len(sys.argv)

print(argc)

n_float = float(argv[1])
n_int = int(argv[1])
print(f"O float = {n_float} ==>> int = {n_int}")
print(f'verificando o isdigit({argv[1]}) = {argv[1].isdigit()}')
