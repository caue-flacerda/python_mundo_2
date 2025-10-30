menor = contPreço = soma = atualMenor = cont = 0
listaN = []
listaP = []
contArray = -1
while True:
    nome = str(input("Entre com o nome do produto: ")).strip()
    preço = float(input("Entre com o preço: R$ "))
    soma += preço
    listaN.append(nome)
    listaP.append(preço)
    cont += 1
    contArray += 1
    if preço > 1000:
        contPreço += 1
    if cont == 1 or menor > listaP[0 + contArray]:
        menor = listaP[0 + contArray]
        atualMenor = contArray  
    resp = " "
    while resp not in "SN":          
        resp = str(input("Quer continuar? ")).strip().upper()[0]
    if resp in "N":
        break
print(f"O total foi R${soma}")
print(f"Tem {contPreço} produtos que custam mais de R$1000")
print(f"O nome do produto mais barato é {listaN[atualMenor]} e custa: R${menor}")
