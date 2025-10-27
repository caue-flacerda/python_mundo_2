from random import choice
print("Vamos jogar jokenpô!")
escolha = str(input("Faça sua escolha: ")).strip().lower()
lista = ["pedra", "papel", "tesoura"]
game = choice(lista)
if escolha == "pedra":
    if game == "tesoura":
        print("Você ganhou!!! {} ganha de {}".format(escolha, "tesoura"))
    elif game == "papel":
        print("Você perdeu kkkk {} perde para {}".format(escolha, "papel"))
    else:
        print("empate! Você jogou {} e o computador jogou {}".format(escolha, "pedra"))
elif escolha == "papel":
    if game == "pedra":
        print("Você ganhou!!! {} ganha de {}".format(escolha, "pedra"))
    elif game == "tesoura":
        print("Você perdeu kkkk {} perde para {}".format(escolha, "tesoura"))
    else:
        print("empate! Você jogou {} e o computador jogou {}".format(escolha, "papel"))
elif escolha == "tesoura":
    if game == "papel":
        print("Você ganhou!!! {} ganha de {}".format(escolha, "papel"))
    elif game == "pedra":
        print("Você perdeu kkkk {} perde para {}".format(escolha, "pedra"))
    else:
        print("empate! Você jogou {} e o computador jogou {}".format(escolha, "tesoura"))
else:
    print("Digite apenas pedra, papel ou tesouro")
