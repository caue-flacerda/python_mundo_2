num = int(input("Entre com um número: "))
cont = 1
soma = num
lista = []
lista.append(num)
maior = lista[0]
menor = lista[0]
r = str(input("Deseja continuar? ")).upper().strip()[0]
while r not in ["N"]:
    num = int(input("Entre com um número: "))
    lista.append(num)
    if maior > lista[-1]:
        if menor > lista[-1]:
            menor = lista[-1]
        else:
            menor == menor
    elif lista[-1] > maior:
        maior = lista[-1]
    soma += num
    cont += 1
    r = str(input("Deseja continuar? ")).upper().strip()[0]
print("A soma é {} foi digitado {} números e a média é {:.1f}. O maior é {} o menor é {}".format(soma,cont,soma/cont, maior,menor))
'''r = ""
n1 = int(input("Numero 1 "))
lista = []
lista.append(n1)
while r not in ["N"]:
    n1 = int(input("Numero 2 "))
    r = str(input("S/N "))
    lista.append(n1)
print("{} {}".format(lista[0],lista[-1]))'''