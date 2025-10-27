n1 = float(input("Entre com a primeira nota: "))
n2 = float(input("Entre com a segunda nota: "))
media = (n1 + n2)/2
if media < 5:
    print("Você reprovou! Sua média foi {:.1f}".format(media))
elif media > 5 and media < 7:
    print("Você está de recuperação! Sua média foi {:.1f}".format(media))
elif media >= 7:
    print("Você passou! Sua média foi {:.1f}".format(media))
    