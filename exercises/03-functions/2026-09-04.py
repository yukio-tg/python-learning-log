'''

# DESAFIO 1

def distribuir_xp(personagens, xp):
    for personagem in personagens:
        personagem["xp"] = xp * personagem["nivel"]
        if personagem["vida"] < 50:
            personagem["xp"] += 200

personagens = [
    {"nome": "Aldren", "vida": 70, "nivel": 6},
    {"nome": "Bruna", "vida": 120, "nivel": 8},
    {"nome": "Kael", "vida": 45, "nivel": 4},
    {"nome": "Mira", "vida": 90, "nivel": 7},
]

distribuir_xp(personagens, 100)
print(personagens)


# DESAFIO 2

def adicionar_xp(personagem,xp):
    personagem["xp"] += xp

def calcular_nivel(xp):
    return xp // 100 + 1 # é a mesma coisa que int(xp / 100) + 1

personagens = [
    {"nome": "Aldren", "vida": 70, "nivel": 6, "xp": 0},
    {"nome": "Bruna", "vida": 120, "nivel": 8, "xp": 0},
    {"nome": "Kael", "vida": 45, "nivel": 4, "xp": 0},
    {"nome": "Mira", "vida": 90, "nivel": 7, "xp": 0},
]

adicionar_xp(personagens[0], 250)

novo_nivel = calcular_nivel(personagens[0]["xp"])

personagens[0]["nivel"] = novo_nivel

print(personagens[0])

# DESAFIO 3

def analisar_personagem(personagem):
    nome = personagem["nome"]
    nivel = personagem["nivel"]
    situacao_vida = None

    if personagem["vida"] >= 100:
        situacao_vida = "Saudável"
    elif personagem["vida"] >= 50:
        situacao_vida = "Ferido"
    elif personagem["vida"] < 50:
        situacao_vida = "Crítico"
    
    return nome, nivel, situacao_vida

def gerar_resumo(personagens):
    criticos = 0
    for personagem in personagens:
        nome,nivel,situacao_vida = analisar_personagem(personagem)
        print(f"{nome} | Nível {nivel} | {situacao_vida}")
        if situacao_vida == "Crítico":
            criticos += 1
    print(f"Personagens em estado crítico: {criticos}")

personagens = [
    {"nome": "Aldren", "vida": 70, "nivel": 6, "xp": 250},
    {"nome": "Bruna", "vida": 120, "nivel": 8, "xp": 730},
    {"nome": "Kael", "vida": 45, "nivel": 4, "xp": 380},
    {"nome": "Mira", "vida": 90, "nivel": 7, "xp": 510},
]

gerar_resumo(personagens)

# DESAFIO 4

def calcular_dano(personagem,defesa):
    dano = personagem["ataque"]
    if dano >= defesa:
        dano -= defesa
        return dano
    else:
        return 0

def realizar_ataque(personagem,defesa):
    print(f"{personagem["nome"]} causou {calcular_dano(personagem,defesa)} de dano!")

personagem = {
    "nome": "Aldren",
    "ataque": 30
}

realizar_ataque(personagem,20)
realizar_ataque(personagem,50)
'''