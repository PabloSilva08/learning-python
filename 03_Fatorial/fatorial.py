number = int(input("Insira um número positivo: "))
if number < 0:
    print("Por favor insira um número positivo.")
    exit (1)
elif number == 0:
    print(f'!0 = 1')
else:
    val = inter = number
    while inter > 1:
        number = number * (inter - 1)
        inter = inter - 1
    print(f'!{val} = {number}')
