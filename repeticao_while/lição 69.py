contIdade = 0
contH = 0
contM = 0
while True: 
    idade = int(input("Entre com a idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Entre com o sexo. [M/F] ")).strip().upper()[0]
    if idade > 18:
        contIdade += 1
    if sexo == "M":
        contH +=1
    if sexo == "F" and idade < 20:
        contM += 1
    res = " "
    while res not in "SN":
        res = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if res in "N":
        break
print(f"O total de pessoas maiores de 18 anos é de {contIdade}")
print(f"Ao todo temos {contH} homens cadastrados")
print(f"E temos {contM} mulheres com menos de 20 anos")

    
    
    
