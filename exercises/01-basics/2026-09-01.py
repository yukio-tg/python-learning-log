'''

# DESAFIO 5 RELATÓRIO DE INVENTÁRIO

inventario = ["espada", "poção", "espada", "arco", "poção", "poção"]

repetidos = []
unicos = []

for item in inventario:
    if item not in repetidos:
        if item in unicos:
            unicos.remove(item)
            repetidos.append(item)
        else:
            unicos.append(item)


print(f"Existem {len(inventario)} itens no inventário.\nOs itens que aparecem mais de uma vez são: {repetidos}\nOs itens que não se repetem são {unicos}.")

# DESAFIO 4 ANÁLISE DE DADOS

notas = [7.5, 4.0, 8.5, 6.0, 9.0, 3.5, 8.0]

n_maior7_igual7 = 0
n_maior = notas[0]
n_menor = notas[0]
soma = 0
media = 0
reprovados = []

for n in notas:
    if n >= 7:
        n_maior7_igual7 += 1
    else:
        reprovados.append(n)

    if n_menor > n:
        n_menor = n
    if n_maior < n:
        n_maior = n

    soma += n

media = soma/len(notas)

print(f"Existem {n_maior7_igual7} notas maior ou igual a 7.\nA maior nota é {n_maior}\nA menor nota é {n_menor}\nA média da turma é {media}.\nAs notas reprovadas são: {reprovados}")

# DESAFIO 3 Construindo uma nova lista

numeros = [3, 8, 12, 5, 17, 20, 7]

maiores_que_dez = []

for n in numeros:
    if n > 10:
        maiores_que_dez.append(n)

print(maiores_que_dez)

# DESAFIO 2 VALOR + POSIÇÃO

numeros = [7, 12, 4, 18, 9, 21]

for i in range(len(numeros)):
    if numeros[i] > 10:
        print(f"{numeros[i]} está na posição {i}.")

# DESAFIO 1 ENCONTRAR POSIÇÃO

numeros = [7, 12, 4, 9, 21, 18]

contador = 0

while True:
    if numeros[contador] == 18:
        print(f"O {numeros[contador]} está na posição {contador} da lista.")
        break
    elif contador+1 < len(numeros):
        contador += 1
    else:
        print("O número não está na lista")
        break

# DESAFIO 0 CONTAGEM
# ideia: um loop for que a cada iteração analisa se o conteúdo é igual à 5, se for ele soma +1 no contador

numeros = [12, 5, 8, 5, 21, 4, 5, 10]

contador = 0

for numero in numeros:
    if numero == 5:
        contador += 1

print(f"Foi encontrado {contador} números 5.")

'''