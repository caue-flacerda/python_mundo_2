from datetime import date
hj = date.today().year
contMaior = 0
contMenor = 0
for contador in range(1,8):
    ano = int(input("Entre com ano de nascimento da {}°: ".format(contador)))
    if hj - ano >= 21:
        contMaior += 1
    else:
        contMenor += 1
print("A quantidade de pessoas com mais de 21 anos é de {} pessoas e menores são de {} pessoas".format(contMaior,contMenor))
