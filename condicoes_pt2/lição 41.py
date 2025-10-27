from datetime import date
nasc = int(input("Entre com seu ano de nascimento, para saber qual é sua confederação: "))
ano = date.today().year
idade = ano - nasc 
if  idade <= 9:
    print("Sua idade é {} e sua confederação é a Mirim ".format(idade))
elif idade <= 14:
    print("Sua idade é {} e sua confederação é a infantil".format(idade))
elif idade <= 19:
    print("Sua idade é {} e sua confederação é a junior".format(idade))
elif idade == 20:
    print("Sua idade é {} e sua confederação é sênior".format(idade))
else:
    print("Sua idade é {} e sua confederação é master".format(idade)) 
