altura = float(input("Entre com sua altura: "))
peso = float(input("Entre com seu peso: "))
imc = peso/(altura ** 2)
if imc < 18.5:
    print("Você está abaixo do peso normal")
elif imc >= 18.5 and imc < 25:
    print("Peso ideal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 40:
    print("Obesidade")
elif imc >= 40:
    print("Baleia!!! kkkkkk")
    