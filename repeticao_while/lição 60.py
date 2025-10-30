fatorial = int(input("Entre com um número: "))
antecessor = fatorial - 1
conta = fatorial * antecessor
while antecessor > 1:
    antecessor += -1
    conta *= antecessor
print("O fatorial de {} é: {}".format(fatorial,conta))
'''
from math import factorial
n = int(input("Entre com um número: "))
fatorial = factorial(n)
print("O fatorial de {} é {}".format(n1, fatorial))
'''