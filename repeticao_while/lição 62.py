n1 = int(input("Entre com o primeiro termo: "))
razão = int(input("Entre com a razão: "))
lista = []
lista.append(n1)
contador = 0
cont2 = 0
while contador < 9:
    n1 += razão
    lista.append(n1)
    contador += 1
print(lista)
lista2 = []
x = lista[9]
lista2.append(x)
r = str(input("Deseja continuar? [S/N] ")).upper()
while r not in ["N"]:
    num = int(input("Mais quantos termos você deseja? "))
    while cont2 < num:
        x += razão
        cont2 += 1
        lista2.append(x)
    print(lista2)
    r = str(input("Deseja continuar? [S/N] ")).upper() 
print("Tchau!")