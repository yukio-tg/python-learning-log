import random
import os
import time


class NotEnoughMana(Exception):
    "Quando não tem mana o suficiente"


def waiting(ticks):
    for _ in range(ticks):
        print(f".", end="", flush=True)
        time.sleep(0.75)
    os.system("cls")


def acaoHeroi(heroHP, heroMP, enemyHP):
    os.system("cls")
    print(
        f"Sua vida: {heroHP}/{heroMaxHP} | Sua mana: {heroMP}/{heroMaxMP}\nVida do inimigo: {enemyHP}/{enemyMaxHP}\n\n======== Escolha sua ação! =======\n1 - Atacar\n2 - Curar-se (custa {healCost} de mana)\n3 - Sair"
    )
    while True:
        try:
            escolhaDeAcao = int(input("Escolha sua ação\n"))

            if escolhaDeAcao not in [1, 2, 3]:
                raise ValueError

            if (escolhaDeAcao == 2) and heroMP < healCost:
                raise NotEnoughMana

            break
        except NotEnoughMana:
            print("Você não tem Mana o suficiente")
            waiting(5)

        except ValueError:
            print(
                "Entrada inválida. Por favor escolha uma opção existente e apenas com números.\n"
            )
            waiting(5)

    match escolhaDeAcao:
        case 1:
            heroDMG = random.randint(1, 6) + 2
            enemyHP -= heroDMG
            os.system("cls")
            print(f"Você desferiu {heroDMG} pontos de dano.")
            waiting(3)
        case 2:
            heroMP -= healCost

            heroRegen = random.randint(1, 4) + 1
            os.system("cls")

            if (heroHP + heroRegen) < heroMaxHP:
                heroHP += heroRegen
            else:
                heroRegen = heroMaxHP - heroHP

            print(f"Você recuperou {heroRegen} pontos de vida.")
            waiting(3)
        case 3:
            os.system("cls")
            print("Encerrando sua jornada")
            waiting(5)
            exit()

    return heroHP, heroMP, enemyHP


def acaoInimigo(heroHP, enemyHP):
    escolhaAcaoInimigo = random.randint(1, 5)
    if enemyHP > 0:
        if escolhaAcaoInimigo >= 3:
            enemyDMG = random.randint(1, 8)
            heroHP -= enemyDMG
            print(f"O inimigo te desferiu {enemyDMG} pontos de dano.")
            waiting(3)
        else:
            enemyRegen = random.randint(1, 6)

            if (enemyHP + enemyRegen) < enemyMaxHP:
                enemyHP += enemyRegen
            else:
                enemyRegen = enemyMaxHP - enemyHP
                enemyHP += enemyRegen

            print(f"O inimigo recuperou {enemyRegen} pontos de vida.")
            waiting(3)

    return heroHP, enemyHP


def interludio(heroMaxHP, heroMaxMP, passiveRegenMP, incHeroDMG, incHeroHeal):
    print(f"Antes de sair para um novo confronto. Vamos melhorar seu herói:\n")
    print(
        f"Atualmente você possui:\nHP: {heroMaxHP}\nPM: {heroMaxMP}, regenerando {passiveRegenMP} por rodada\nDano: x1\nCura: x1"
    )
    print(
        f"Escolha:\n1. Aumento de Vida (+5)\n2. Aumento de Dano (+0.5)\n3. Aumento de Mana(+3, passiva +1)\n 4. Aumento de Cura (+0.5)\n"
    )

    while True:
        try:
            escolha = int(input())

            if escolha not in [1, 2, 3, 4]:
                raise ValueError
            
            break

        except ValueError:
            print(
                "Entrada inválida. Por favor escolha uma opção existente e apenas com números.\n"
            )
            waiting(5)

    match escolha:
        case 1:
            heroMaxHP += 5
        case 2:
            incHeroDMG += 0.5
        case 3:
            heroMaxMP += 3
            passiveRegenMP += 1
        case 4:
            incHeroHeal += 0.5

    return heroMaxHP, heroMaxMP, passiveRegenMP, incHeroDMG, incHeroHeal


heroMaxHP = 20
heroHP = heroMaxHP
heroMaxMP = 10
heroMP = heroMaxMP
passiveRegenMP = 1
healCost = 4
incHeroDMG = 1
incHeroHeal = 1

enemyMaxHP = 20
enemyHP = enemyMaxHP

while True:
    if heroHP < 1:
        print("Você morreu.")
        break
    elif enemyHP < 1:
        print("Você venceu!")
        break
    else:
        heroHP, heroMP, enemyHP = acaoHeroi(heroHP, heroMP, enemyHP)
        if heroMP < heroMaxMP:
            heroMP += passiveRegenMP
        heroHP, enemyHP = acaoInimigo(heroHP, enemyHP)
