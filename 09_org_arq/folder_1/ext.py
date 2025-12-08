s1 = "arq.klb"
s2 = "arq.juio"
s3 = "arq.juio.kio.tt"
s4 = "arq_io"

l1 = s1.split('.')
l2 = s2.split('.')
l3 = s3.split('.')
l4 = s4.split('.')

#if (len(l3) > 1):
#    print("exite l3")
#if (len(l2) > 1):
#    print("exite l2")
print(l1)
print(l2)
print(l3)
print(l4)

tmp1 = '+'.join(l3)
tmp2 = '+'.join(l4)
print(tmp1)
print(tmp2)
