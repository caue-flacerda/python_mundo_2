a = float(input("Entre com o primeiro segmento: "))
b = float(input("Entre com o segundo segmento: "))
c = float(input("Entre com o terceiro segmento: "))
if a < c + b and b < c + a and c < a + b:
    print("Esses segmentos formam um triângulo: ", end='')
    if c == a and b == c:
        print("Equilátero")
    elif c == a or a == b or b == c:
        print("Isósceles")
    elif c != a and a != b and b != c:
        print("Escaleno")
else:
    print("Esses segmentos não forma um triângulo: ")
    