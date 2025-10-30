menu = int
n1 = int(input("Entre com um número: "))
n2 = int(input("Entre com: "))
while menu != 5:
    print("[1] somar\n[2] mutiplicar\n[3] maior\n[4] novos números\n[5] sair")
    menu = int(input("Faça sua escolha: "))
    if menu == 1:
        print("A soma entre {} e {} é {}".format(n1,n2,n1+n2)) 
    elif menu == 2:
        print("A mutiplicação entre {} e {} é {}".format(n1,n2,n1*n2))
    elif menu == 3:
        if n1 > n2:
            print("O maior número é {}".format(n1))
        elif n1 < n2:
            print("O maior número é {}".format(n2))
        else:
            print("Não há maior")
    elif menu == 4:
        print("Vamos trocar os números")
        n1 = int(input("Entre com o 1° número: "))
        n2 = int(input("Entre com o 2° número: "))
    elif menu > 5:
        print("Opção inválida")
print("Tchau!!!")
