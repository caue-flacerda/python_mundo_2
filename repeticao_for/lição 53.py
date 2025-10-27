frase = str(input('Entre com uma frase qualquer: ')).strip().lower()
junçao = ''.join(frase.split())
print(frase)
print(junçao)
lista = []
for contador in range((len(junçao))-1,-1,-1):
    lista.append(junçao[contador]) 
inversa = ''.join(lista)
print(inversa)
if junçao == inversa:
    print('Essa é frase é um palindromo')
else:
    print("Não é um palindromo. Seu otário")
    