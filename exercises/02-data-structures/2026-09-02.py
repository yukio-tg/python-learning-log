'''
# DIAGNÓSTICO
# PRECISA GUARDA: QUANTAS VEZES O NÚMERO 3 APARECE; O MAIOR E O MENOR NÚMERO ENCONTRADO

numeros = [14, 3, 8, 3, 21, 7, 3, 10]

contador = 0
maior = numeros[1]
menor = numeros[1]

for n in numeros:
    if n == 3 : contador += 1
    if n > maior : maior = n
    if n < menor : menor = n

print(f"Menor: {menor}; Maior: {maior}; Vezes que o número 3 apareceu: {contador}")

# TESTES

personagem = {
    "nome": "Aldren",
    "vida": 70,
    "mana": 40,
    "classe": "Guerreiro",
    "nivel": 6
}

for k,  v in personagem.items():
    print(f"{k} → {v}")
    

# DESAFIO DE CONDICIONAIS

personagens = {
    "Aldren": 70,
    "Bruna": 120,
    "Kael": 45,
    "Mira": 90
}

for k,v in personagens.items():
    if v > 60:
        print(f"{k} possui {v} PV.")

'''

# LISTAS DE DICIONÁRIOS DESAFIO

personagens = [
    {"nome": "Aldren", "vida": 70, "nivel": 6, "classe": "Guerreiro"},
    {"nome": "Bruna", "vida": 120, "nivel": 8, "classe": "Maga"},
    {"nome": "Kael", "vida": 45, "nivel": 4, "classe": "Ladino"},
    {"nome": "Mira", "vida": 90, "nivel": 7, "classe": "Clériga"}
]

# OBJETIVO:
# - Maior nível, menor vida, média de vida de todos os personagens, mostrar personagens com nível 6 ou superior, sistema de busca

maior_valor = personagens[0]["vida"]
menor_valor = personagens[0]["vida"]
maior = personagens[0]["nome"]
menor = personagens[0]["nome"]
soma = 0
evoluidos = []
absoluto = personagens[0]
buscado = input(f"Insira nome buscado:\n")
encontrado = None

for p in personagens:
    if p["vida"] > maior_valor:
        maior = p["nome"]
        maior_valor = p["vida"]
    if p["vida"] < menor_valor:
        menor = p["nome"]
        menor_valor = p["vida"]
    if p["nivel"] >= 6:
        evoluidos.append(p['nome'])
    if p["nivel"] > absoluto["nivel"]:
        absoluto = p
    if encontrado == None and buscado == p["nome"]:
        encontrado = p

    soma += p["vida"]

print(f"Maior vida: {maior} ({maior_valor} PV)... Menor vida: {menor} ({menor_valor} PV)")
print(f"Soma das vidas: {soma}")
print(f"Maiores que nível 5: {evoluidos}")
print(f"Maior nível: {absoluto['nome']} ({absoluto['nivel']})")
print(f"Média de todas as vidas: {soma/(len(personagens))}")
if encontrado != None:
    print(f"Personagem requisitado: {encontrado}")
else:
    print("Personagem não está na lista")