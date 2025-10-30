while True:
    num = int(input("Quer ver a tabuada de qual valor? "))
    print("-" * 30)
    if num < 0:
        break
    for c in range(1,11):
        print(f" {num} X {c} = {num*c}") 
print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")