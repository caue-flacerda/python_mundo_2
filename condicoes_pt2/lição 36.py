vcasa = int(input("Entre com o valor da casa: "))
salário = int(input("Entre com o seu salário: "))
tempo = int(input("Em quantos anos você deseja pagar: "))
parcela = tempo * 12
prestação = vcasa / parcela
if prestação > salário * 0.3:
    print("Você não pode comprar a casa, pois seu salário é baixo! KKKKK pobre")
else:
    print("Você pode comprar a casa! Cada prestação mensal ficou no valor de {:.1f}".format(prestação))
