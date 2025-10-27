somaIdade = 0
maiorIdade = 0
nomeVelho = ""
menor20 = 0
for contador in range(1,5):
    print("---------{}°---------".format(contador))
    nome = str(input("Entre com o nome: ")).strip()
    idade = int(input("Entre com a idade: "))
    sexo = str(input("Entre com o sexo [M/F] ")).strip()
    somaIdade += idade
    if contador == 1 and sexo in "Mm":
        maiorIdade = idade
        nomeVelho = nome
    if maiorIdade < idade and sexo in "Mm":
        maiorIdade = idade
        nomeVelho = nome
    if idade < 20 and sexo in "Ff":
        menor20 += 1
print("A média das idades são de {}".format(somaIdade/4))
print("O nome do homem mais velho é: {} e tem {} anos".format(nomeVelho, maiorIdade))
print("Ao todo são {} mulheres com menos de 20 anos".format(menor20))