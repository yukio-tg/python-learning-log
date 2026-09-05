"""

# DESAFIO 1

def calcular_dano(dano,defesa):
    dano -= defesa
    if dano < 0:
        dano = 0
    return dano

print(calcular_dano(20,5))
print(calcular_dano(10,10))
print(calcular_dano(5,10))


# DESAFIO 2

def calcular_dano(ataques,defesa):
    danos = []

    for ataque in ataques:
        ataque -= defesa
        if ataque < 0:
            ataque = 0
        danos.append(ataque)

    return danos


ataques1 = [20,15,8]
defesa1 = 5
ataques2 = [10, 5, 20]
defesa2 = 8

print(calcular_dano(ataques1,defesa1))
print(calcular_dano(ataques2,defesa2))

"""

# DESAFIO 3, 4, 5


def maior_nivel(personagens):
    if personagens:
        maior = personagens[0]["nivel"]

        for personagem in personagens:
            if personagem["nivel"] > maior:
                maior = personagem["nivel"]

        return maior
    else:
        return None


def filtrar_por_nivel(personagens, nivel_minimo):
    filtrados = []
    for personagem in personagens:
        if personagem["nivel"] >= nivel_minimo:
            filtrados.append(personagem["nome"])
    return filtrados

def buscar_personagem(personagens,nome_buscado):
    if personagens:
        for personagem in personagens:
            if personagem["nome"] == nome_buscado:
                return personagem
    return None

def analisar_nivel_do_grupo(personagens, nivel_minimo):
    personagens_acima_do_nivel = filtrar_por_nivel(personagens,nivel_minimo)

    return maior_nivel(personagens), personagens_acima_do_nivel

def avaliar_grupo(personagens, nivel_minimo):
    maior = maior_nivel(personagens)
    personagens_aptos = filtrar_por_nivel(personagens,nivel_minimo)
    resultado = {"maior_nivel": maior, "personagens_aptos": personagens_aptos}

    if len(personagens_aptos) >= 2 and maior > (nivel_minimo):
        resultado["grupo_aprovado"] = True
        return resultado

    resultado["grupo_aprovado"] = False
    return resultado

def distribuir_xp(personagens, xp):
    if personagens:
        for personagem in personagens:
            personagem["xp"] = xp * personagem["nivel"]

        return personagens

personagens = [
    {"nome": "Aldren", "vida": 70, "nivel": 6},
    {"nome": "Bruna", "vida": 120, "nivel": 8},
    {"nome": "Kael", "vida": 45, "nivel": 4},
    {"nome": "Mira", "vida": 90, "nivel": 7},
]

distribuir_xp(personagens, 100)
print(maior_nivel(personagens))
print(filtrar_por_nivel(personagens, 7))
print(buscar_personagem(personagens,"Kael"))

resultado = analisar_nivel_do_grupo(personagens, 7)
print(resultado)

print(avaliar_grupo(personagens,7))