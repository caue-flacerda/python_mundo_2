valor = float(input("Entre com o valor do produto. R$"))
print("Escolha uma das formas de pagamento: \ndinheiro/cheque \ncartão\n2x no cartão\n3x no cartão")
pagamento = str(input("Escolha uma das formas de pagamento: ")).lower().strip()
formaPagamento = ["dinheiro","cheque","cartão", "2x no cartão", "3x no cartão"]
if pagamento == formaPagamento[0]:
    print("No dinheiro fica {} reais".format(valor - (valor * 0.1)))
elif pagamento == formaPagamento[1]:
    print("No cheque fica {} reais".format(valor - (valor * 0.1))) 
elif pagamento == formaPagamento[2]:
    print("No cartão fica {} reais".format(valor -(valor * 0.05)))
elif pagamento == formaPagamento[3]:
    parcela = valor/2
    print("No cartão parcelado 2x fica {} reais".format(parcela))
elif pagamento == formaPagamento[4]:
    qtd = int(input("Entre com a quantidade de parcelas: "))
    parcela = valor/qtd
    print("No cartão parcelado {}x fica {} reias, mas com juros de 30 porcento de desconto fica {} reais ao todo ".format(qtd, parcela,valor + (valor * 0.2)))
else:
    print("Opção inexistente!")
    