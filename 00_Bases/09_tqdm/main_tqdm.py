from tqdm import tqdm
import tqdmm
import time

frase = "Pablo Vieira Carvalho Silva"
l1 = [11, 22, 33, 44, 55, 66, 77]
l2 = 8

#c1 = tqdmm.PTqdm(l1)
#for i in tqdmm.PTqdm(l1):
#    print(i)
#    time.sleep(1)
#
#t = tqdm(frase)
#print(t)

for i in tqdm(range(1,9)):
    time.sleep(.1)

print(hasattr(range(10), '__len__'))

print(range(10).__len__())


print(hasattr(l1, '__len__'))
