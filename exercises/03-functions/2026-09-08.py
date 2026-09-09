# DESAFIO 5
def atacar(atacante,alvo):
    print(f"{atacante["nome"]} atacou {alvo["nome"]}!")
    if atacante["vida"] == 0 #continuar dps
def calcular_dano(ataque,defesa):
    return max(ataque - defesa, 0)

def aplicar_dano(dano,vida):
    vida -= dano
    return max(vida, 0)

personagens = [
    {
        "nome": "Aldren",
        "vida": 100,
        "ataque": 30,
        "defesa": 10
    },
    {
        "nome": "Bruna",
        "vida": 80,
        "ataque": 45,
        "defesa": 5
    },
    {
        "nome": "Kael",
        "vida": 120,
        "ataque": 20,
        "defesa": 20
    }
]