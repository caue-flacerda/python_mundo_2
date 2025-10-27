soma = 0
cont = 0
for contador in range(0,6):
    num = int(input("Entre com seis número: "))
    if num % 2 == 0:
        soma += num
        cont += 1
print("A soma dos {} números pares são: {}".format(cont,soma))
 
