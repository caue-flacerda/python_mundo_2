termo = int(input("Quantos termos você deseja? "))
n2 = 1
soma = 0
lista = []
lista.append(n2)
contador = 0
cont = 0
while contador < termo - 1:
       if contador == 0:
        soma = n2 + 0 
        contador += 1
        lista.append(soma)
       else:
        soma += lista[0 + cont]
        lista.append(soma)
        contador += 1
        cont += 1
print("{}".format(lista))
    