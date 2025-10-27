n1 = int(input("Entre com um numéro para a tabuada: "))
for contador in range(1, 11):
    print("{} X {:2} = {}".format(n1, contador, n1 * contador))
