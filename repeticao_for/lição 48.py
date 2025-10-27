cont = 0
soma = 0
for contador in range(1, 501 ,2):
    if contador % 3 == 0:
        cont += 1
        soma += contador
        print(contador, end=" ")
    
print("\nA soma de todos os {} valores solicitados é: {}".format(cont,soma))
