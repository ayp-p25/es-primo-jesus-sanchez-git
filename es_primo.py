import math
def Es_primo(N):
    if N<2:
        return False
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return False
        i += 1
    return True
N = int(input("Ingrese el numero que quisiera saber si es primo : \n"))
P = True
i= 0
Primo = Es_primo(N)
print(f"El número {N} {'si' if Primo else 'no'} es primo.")