n1 = float(input('Digite o valor da primeira nota.\n'))
n2 = float(input('Digite o valor da segunda nota.\n'))
n3 = float(input("Digite o valor da terceira nota.\n"))

pesoN1 = 2
pesoN2 = 3
pesoN3 = 1

mediaAritmetica = float((n1+n2+n3)/3)
mediaPonderada = float((n1*pesoN1+n2*pesoN2+n3*pesoN3)/(pesoN1+pesoN2+pesoN2))
meta = 7

print(f"Sua média aritmética é: {mediaAritmetica}.\nSua média ponderada é: {mediaPonderada}.")

if mediaAritmetica < 7 and mediaPonderada < 7:
    print("Você não passa com nenhuma das notas finais. Me desculpe.")
elif mediaAritmetica >= 7 and mediaPonderada <7:
    print("Você está abaixo da nota esperada na média ponderada, mas igual ou acima caso a média seja aritmética.")
elif mediaAritmetica < 7 and mediaPonderada >= 7:
    print("Você está abaixo da nota esperada na média aritmética, mas igual ou acima caso a média seja ponderada.")
else:
    print("Você passa na média 7, com qualquer nota.")