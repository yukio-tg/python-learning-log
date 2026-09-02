

'''

numeros = [7, 12, 4, 18, 9, 21]

numeroDesejado = int(input())
found = False

for numero in numeros:
    if numero == numeroDesejado:
        found = True

if found == True:
    posicao = numeros.index(numeroDesejado)+1
    print(f"Número encontrado na posiçao {posicao}.")
else:
    print("Número não está na lista")

numeros = [1, 2, 3, 4, 5]

for i in range(len(numeros)):
    numeros[i] = numeros[i]*2
    print(numeros[i])

# EXERCÍCIO 1: LISTA SEM ÍNDICES

numeros = [12, 5, 8, 21, 4]

for numero in numeros:
    print(numero)

# EXERCÍCIO G

# não sabia lidar com listas então tive que pesquisar

lista_numero = [0,98,-1,4+2,36]

menor = lista_numero[0]
maior = lista_numero[0]
soma = 0
nPares = 0

for i in range(len(lista_numero)):
    if lista_numero[i] < menor:
        menor = lista_numero[i]

    if lista_numero[i] > maior:
        maior = lista_numero[i]

    soma += lista_numero[i]

    if lista_numero[i] % 2 == 0: #pesquisei como fazia isso (não lembrava)
        nPares += 1

print(f"Maior número é: {maior}\nMenor número é: {menor}\nSoma total é: {soma}\nExistem {nPares} números pares.")

# EXERCÍCIO D

numero = int(input("digite um valor"))
soma = 0

for i in range(1,numero+1):
    soma += i

    print(soma)

# EXERCÍCIO E

numero = int(input("digite um valor"))

for i in range(1,numero+1):
    print(i)

for i in range(1,numero+1,2):
    print(i)

# EXERCÍCIO D

# Foi necessário uma pesquisa pois não sabia como funcionava FOR e RANGE

for i in range(0,21,2): #se houver um terceiro número ele faz "pulos"
    print(i)

for i in range(19,0,-1):
    print(i)

for i in range(21):
    print(i)

# EXERCICIO WHILE C (recebedor de numero contínuos)

numero = int(input("Digite um número\n"))

contador = 0
soma = 0

while numero != 0:
    contador += 1
    soma += numero
    numero = int(input("Digite um número\n"))

print(f"Você digitou zero!\nDigitou um total de {contador} números.\nSomados são igual a {soma}.")

# EXERCICIO WHILE B (senha)

senhaCorreta = "Abóbrinha"
senha = input("Digite uma tentativa para a senha correta\n")

while senha != senhaCorreta:
    print("Senha incorreta")
    senha = input("Digite uma tentativa para a senha correta\n")

print("Senha correta!")

# EXERCICIO WHILE A (contador)
numero = 0

while numero != 10:
    numero += 1
    print(f"{numero}")

while numero != 0:
    numero -= 1
    print(f"{numero}")

# TESTE 4 (funções)

# Houveram dificuldades tive que pesquisar a estrutura

def calcular_dano(dmg,rd,pvHeroi):
    newDMG = dmg-rd

    if newDMG > 0:
        pvHeroi -= newDMG

    return pvHeroi

dmg = int(input("Digite um dano"))
rd = 2
pvHeroi = 20

newPvHeroi = calcular_dano(dmg, rd, pvHeroi) 

print(f"A vida do herói ficou: {newPvHeroi}")

# TESTE 3 (While test)

number = int(input("Digite um número\n"))

while number != 0:
    print("Seu número não é 0")

    number = int(input("Digite um número\n"))

print("Seu número é 0, saindo...")

# TESTE 2 (checa intervalos)

idade = int(input("Insira uma idade em anos\n"))

if idade <= 12:
    print("É uma criança")
elif idade <= 17:
    print("É um adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")

#TESTE 1 (número positivo, negativo ou zero)

numero = float(input("Insira um número positivo, negativo ou igual a 0\n"))

if numero > 0:
    print("Seu número é positivo")
elif numero < 0:
    print("Seu numero é negativo")
else:
    print("Seu número é 0")

'''