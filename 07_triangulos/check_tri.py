'''
Dados 3 valores numéricos não negativos, responda se é possível existir um 
triângulo cujas medidas sejam estes valores
'''
def check_triangle(a: int, b: int, c: int) -> bool:
    if (a < 1 or b < 1 or c < 1 ):
        return(False)
    if (a + b > c) and (a + c > b) and  (c + b > a):
        return(True)
    return(False)

if __name__ == '__main__':
    try:
        a = int(input("Enter the number: "))
        b = int(input("Enter the number: "))
        c = int(input("Enter the number: "))

        if check_triangle(a, b, c):
            print(f'Sides {a}, {b} and {c} form a triangle.')
        else:
            print(f'Sides {a}, {b} and {c} don\'t form a triangle.')

    except ValueError:
        print("Invalid argument.")
