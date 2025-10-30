n1 = int(input("Entre com o primeiro termo: "))
razão = int(input("Entre com a razão: "))
contador = 1
termo = n1
while contador <= 10:
    print("{} -> ".format(termo), end='')
    termo += razão
    contador += 1 
print("FIM")
