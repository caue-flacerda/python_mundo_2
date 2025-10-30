n = s = 0
while True:
    n = int(input("Digite um número "))
    if n == 999:
        break
    s += n
print(f"A soma {s}")
#print("A soma vale {}".format(s))
# Esse loop é infinito, porém com o BREAK ele sai do laço.
# Dessa forma evita a gambiarra do somador menos 999 e do contador menos 1