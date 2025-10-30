'''for c in range(1,10):
    print(c)
print("Fim")'''
# Os dois funcionam da mesma forma
'''c = 1
while c < 10:
    print(c)
    c += 1
print("Fim")'''
# Dessa forma o while roda independente da quantidade de números eu coloquei
# algo que é não pode ser feito no FOR, pq ele precisa de uma condição
par = 0
impar = 0
n = 1
while n != 0:
    n = int(input("Digite um valor "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("A quantidade de pares digitados foi {} e de impares foi {} ".format(par,impar))
print("Fim")
