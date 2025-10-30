n = str(input("Entre com o seu sexo: [M/F] " )).strip().upper()[0]
while n not in ['M','F']:
    n = str(input("Dados inválidos. Tente novamente: [M/F] " )).strip().upper()[0]
print("Sexo {} registrado com sucesso".format(n))
