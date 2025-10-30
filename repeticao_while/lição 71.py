num = int(input("Entre com o saldo que você deseja sacar: R$"))
nota50 = nota20 = nota10 = nota1 = resto = 0
if num > 50 and num % 50 != 0:
    nota50 = num // 50
    resto = num % 50
    if resto > 0:
        nota20 = resto // 20
        resto = resto % 20
        if resto > 0:
            nota10 = resto // 10
            resto = resto % 10
            if resto > 0:
                nota1 = resto
elif num >= 50 and num % 50 == 0:
    nota50 = num // 50
elif num < 50 and num > 20 and num % 20 != 0:
    nota20 = num // 20
    resto = num % 20
    if resto > 0:
        nota10 = resto // 10
        resto = resto % 10
        if resto > 0:
            nota1 = resto
elif num < 50 and num >= 20 and num % 20 == 0:
    nota20 = num // 20
elif num < 20 and num > 10 and num % 10 != 0:
    nota10 = num // 10
    resto = num % 10
    if resto > 0:
        nota1 = resto
elif num < 20 and num >= 10 and num % 10 == 0:
    nota10 = num // 10
elif num < 10:
    nota1 = num
print(f"Total de {nota50} notas de 50")
print(f"Total de {nota20} notas de 20")
print(f"Total de {nota10} notas de 10")
print(f"Total de {nota1} notas de 1")
