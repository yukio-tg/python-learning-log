'''
# DESAFIO 1

def atacar(atacante,alvo):

    print(f"{atacante["nome"]} atacou {alvo["nome"]}!")

    if atacante["vida"] == 0:

        print(f"{atacante["nome"]} está derrotado(a) e não pode atacar.")

    else:

        dano = calcular_dano(atacante["ataque"],alvo["defesa"])

        print(f"Dano causado: {dano}.")

        alvo["vida"] = aplicar_dano(dano,alvo["vida"])

        print(f"{alvo["nome"]} possui {alvo["vida"]} de vida.")

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

atacar(personagens[0],personagens[1])

atacar(personagens[0],personagens[2])

atacar(personagens[1],personagens[0])

atacar(personagens[1],personagens[2])

atacar(personagens[2],personagens[0])

atacar(personagens[2],personagens[1])

# Desafio 2

found = False
search = input("Digite posição ou nome para buscar, ou sair para sair.")

nomes = [
    "Ana", "Bruno", "Camila", "Daniel", "Eduarda", 
    "Felipe", "Gabriela", "Gustavo", "Isabela", "João", 
    "Larissa", "Lucas", "Mariana", "Pedro", "Beatriz"
]

while search != "sair":
    for indice, nome in enumerate(nomes,start=1):
        if not found:
            if search.isdigit():
                if int(search) == indice:
                    print(f"Em {search} há {nome}.")
                    found = True
            elif search == nome:
                print(f"{search} está em {indice}.")
                found = True
    if not found:
        print("Sua pesquisa nossa lista não alcança a posição desejada ou o nome não está na lista")
    found = False

    # inicio nova pesquisa
    search = input("Digite posição ou nome para buscar, ou sair para sair.")
'''

# DESAFIO 3

personagens = [
    {"nome": "Aldren", "vida": 100, "nivel": 5},
    {"nome": "Lyra", "vida": 80, "nivel": 7},
    {"nome": "Kael", "vida": 120, "nivel": 3},
    {"nome": "Mira", "vida": 0, "nivel": 9}
]

# Listar personagens + sair
# selecionar personagem
# selecionar ação

def start(personagens):
    listar_personagens(personagens)

def listar_personagens(personagens):
    for indice, personagem in enumerate(personagens, start=1):
        print(f"{indice} - {personagem['nome']} | Vida: {personagem['vida']} | Nível: {personagem['nivel']}")
    print("Digite 'sair' para sair.")
    selecionar_personagem(personagens)

def selecionar_personagem(personagens):
    while True:
        selecionado = input("Digite a posição de um dos personagens para selecioná-lo: ")
        
        if selecionado.isdigit(): 
            selecionado = int(selecionado)
            
            if 0 <= selecionado - 1 < len(personagens):
                personagem_escolhido = personagens[selecionado - 1]
                print(f"Você selecionou {personagem_escolhido['nome']}")
                
                selecionar_acao(personagem_escolhido) 
                break
            else:
                print("Personagem não encontrado.")
        elif selecionado.lower() == "sair":
            print("Saindo...")
            break
        else:
            print("Entrada inválida. Digite um número ou 'sair'.")

def selecionar_acao(personagem):
    print(f"1 - Curar {personagem['nome']}")
    print(f"2 - Derrotar {personagem['nome']}")
    
    escolha = 0
    while escolha != 1 and escolha != 2:
        entrada = input("Digite 1 ou 2, para escolher a ação: ")
        if entrada.isdigit():
            escolha = int(entrada)
            
    if escolha == 1:
        curar_personagem(personagem)
    elif escolha == 2:
        derrotar_personagem(personagem)

def curar_personagem(personagem):
    valor_cura = int(input(f"Digite um valor para ser curado de {personagem['nome']}: "))
    personagem["vida"] += valor_cura
    print(f"{personagem['nome']} agora tem {personagem['vida']} de vida.")
    
    start(personagens)
    return personagem["vida"]

def derrotar_personagem(personagem):
    personagem["vida"] = 0
    print(f"{personagem['nome']} foi derrotado! Vida: 0")
    
    start(personagens)
    return personagem["vida"]

start(personagens)