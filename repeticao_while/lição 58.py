from random import randint
computador = randint(0,10)
jogador = ''
contador = 0
print('vou pensar em um número entre 0 e 10. Tente adivinhar...')
while computador != jogador:
    jogador = int(input("Em que número eu pensei "))
    if computador != jogador:
        print("Você errou! Tenta de novo ;) ")
        if computador > jogador:
            print("Mais... Tenta de novo")
        elif computador < jogador:
            print("Menos... Tenta de novo")
        contador += 1
print("Você consegui!!! Eu também pensei no {}. Você precisou de {} tentativas para acertar.".format(computador,(contador + 1)))