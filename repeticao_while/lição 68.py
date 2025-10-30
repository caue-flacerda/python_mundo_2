from random import randint
pc = randint(0,10)
soma = 0
cont = 0
while True:
    num = int(input("Escolha um número: "))
    parImpar = " "
    while parImpar not in "PI":
        parImpar = str(input("Você quer par ou impar? [P/I] ")).strip().upper()[0]
    soma = num + pc
    if parImpar in "PAR":
        if soma % 2 == 0:
            print(f"Você VENCEU! Eu pensei em {pc} e você em {num}")
            print("Vamos jogar novamente")
            cont += 1
        else:
            print(f"Você perdeu, eu pensei em {pc} e você em {num}")
            break
    else:
        if soma % 2 == 1:
            print(f"Você VENCEU! Eu pensei em {pc} e você em {num}")
            print("Vamos jogar novamente ")
            cont += 1
        else:
            print(f"Você perdeu, eu pensei em {pc} e você em {num}")
            break
print(f"GAME OVER! Você venceu {cont} vezes")