"""
Ideia realizar 5 desafios em python utilizando apenas:

variáveis;
tipos;
entrada/saída;
condicionais;
loops;
funções;
listas;
strings;
sets;
match;
tratamento de exceções.
 """

""" # DESAFIO 1: Receba uma frase do usuário e descubra quantas vezes cada palavra aparece.

frase = input("Digite sua frase, cada palavra repetida na frase será contabilizada.\n")
frase = frase.lower()
frase = frase.split()
palavras_lista = {}

for palavra in frase:
    try:
        palavras_lista[palavra] += 1
    except KeyError:
        palavras_lista[palavra] = 1

for chave, valor in palavras_lista.items():
    print(f"{chave}: {valor}") """

# DESAFIO 2: Receba vários números inteiros e determine quais aparecem exatamente uma vez.

numeros = input("Digite uma quantidade qualquer de números inteiors separados por espaços. Ao fim serão contabilizados os não repetidos.\n")
numeros = numeros.split()
numeros_not_repetidos = set(numeros[0])
numeros_not_repetidos_final = set()

while numeros_not_repetidos != numeros_not_repetidos_final:
    for numero in numeros:
        if numero in numeros_not_repetidos:
            numeros_not_repetidos.remove(numero)
        else:
            numeros_not_repetidos.add(numero)

print(numeros_not_repetidos)