n1 = int(input("Entre com o primeiro termo da pa: "))
razão = int(input("Entre com a razão da pa: "))
pa = []
pa.append(n1)
for contador in range(0,9):
    n1 += razão
    pa.append(n1)
print(pa)
    