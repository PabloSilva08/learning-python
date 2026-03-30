l1 = [1, 2, 3, 4, 5]

l2 = [i*2 for i in l1]

print(l2)


l3 = tuple(i*3 for i in l1)
l4 = list(i*3 for i in l1)

print(l3)
print(l4)


l3[1] = 9
l4[1] = 9

print(l3)
print(l4)
