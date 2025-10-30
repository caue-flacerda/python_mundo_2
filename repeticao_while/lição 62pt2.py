n1 = int(input("Entre com o primeiro termo: "))
razão = int(input("Entre com a razão: "))
contador = 1
termo = n1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print("{} -> ".format(termo), end='')
        termo += razão
        contador += 1 
    print("Pausa")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("Progressão finalizada com {} termos mostrados.".format(total))
