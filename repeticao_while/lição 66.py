soma = cont = 0
while True:
    num = int(input("Entre com um número. (Para parar digite 999) "))
    if num == 999:
        break
    cont += 1
    soma += num
print(f"A soma dos {cont} valores foi {soma}")
