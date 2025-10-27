from datetime import date
ano = int(input("Digite o ano que você nasceu: "))
year = date.today().year
calculo = year - ano
difmaior = calculo - 18
difmenor = 18 - calculo
if (year - ano) == 18:
    print("Você deve se alistar no exército")
elif (year - ano) < 18:
    print("Você deverá se alistar daqui {} ano(s)".format(difmenor))
else:
    print("Você deveria ter se alistado há {} ano(s) atrás".format(difmaior))
