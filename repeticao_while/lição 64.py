soma = 0
cont = 0
num = int(input("Entre com um número inteiro. Condição de parada 999 "))
while num != 999:
    cont += 1
    soma += num
    num = int(input("Entre com um número inteiro: "))
print("Você digitou {} números e a soma é {}".format(cont,soma))
