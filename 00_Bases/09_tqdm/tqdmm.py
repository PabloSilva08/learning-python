from tqdm import tqdm
import time

frase = "Pablo Vieira Carvalho Silva"

for letra in tqdm(frase):
    print(letra)
    time.sleep(1)
