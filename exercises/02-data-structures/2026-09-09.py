'''
# EXPERIMENTO

texto = "  Guerreiro Aldren  "

print(len(texto))
print(texto[2])
print(texto[-3:])
print("Aldren" in texto)
print(texto.strip())
print(texto.lower())

# DESAFIO 1 (STRINGS)

''''''
Requisitos

O programa deve:

Receber o nome do usuário. (input)
Remover espaços desnecessários das extremidades. .strip
Criar uma versão normalizada do nome para comparação. .
Informar o nome formatado. print(.capitalize)
Informar quantos caracteres o nome possui. len(nome)
Informar o primeiro caractere. nome[0]
Informar o último caractere. nome[len(nome)-1]
Verificar se o nome contém a letra "a". if a in nome contador++
Informar quantas vezes "a" aparece no nome. if contador: true
Mostrar o nome invertido.


nome = input("Insira nome")
nome = nome.strip()
nome = nome.capitalize()
print(nome)
print(f"Nome possui {len(nome)} carácteres.")
print(f"Começa com {nome[0]}.")
print(f"Termina com {nome[-1]}.")

contador = 0
for letra in nome:
    if letra == "a" : contador += 1
if contador:
    print("Nome contém letras A.")
    print(f"Nome contém {contador} letras A.")
else:
    print("Nome não contém 0 As.")

print(nome[::-1])

'''

# DESAFIO 2 (SETS)

usuario_a = set()

print("Selecione quais serão as permissoes do usuário.")
print("1 - ler")
print("2 - comentar")
print("3 - escrever")
print("4 - moderar")
print("5 - excluir")
print("Selecione 0 para seguir para a próximo usuário")

opcao = int(input())

while opcao != 0:
    match opcao:
        case 1 : usuario_a.add("ler")
        case 2 : usuario_a.add("comentar")
        case 3 : usuario_a.add("escrever")
        case 4 : usuario_a.add("moderar")
        case 5 : usuario_a.add("excluir")

    opcao = int(input())

usuario_b = set()

print("Selecione quais serão as permissoes do usuário.")
print("1 - ler")
print("2 - comentar")
print("3 - escrever")
print("4 - moderar")
print("5 - excluir")
print("Selecione 0 para realizar a leitura")

opcao = int(input())

while opcao != 0:
    match opcao:
        case 1 : usuario_b.add("ler")
        case 2 : usuario_b.add("comentar")
        case 3 : usuario_b.add("escrever")
        case 4 : usuario_b.add("moderar")
        case 5 : usuario_b.add("excluir")

    opcao = int(input())

'''
O programa deve descobrir:
Todas as permissões existentes nos dois usuários.
As permissões que ambos possuem.
As permissões exclusivas do primeiro usuário.
As permissões exclusivas do segundo usuário.
As permissões que pertencem a apenas um dos usuários.
Se os dois usuários possuem pelo menos uma permissão em comum.
Se os dois usuários possuem exatamente as mesmas permissões.
'''

print(f"Todas:\n{usuario_a.union(usuario_b)}\n")
print(f"Ambos:\n{usuario_a.intersection(usuario_b)}\n")
print(f"Exclusivas do usuário A:\n{usuario_a - usuario_b}\n")
print(f"Exclusivas do usuário B:\n{usuario_b - usuario_a}\n")
print(f"Somente um:\n{usuario_a ^ usuario_b}\n")

print("Possuem algo em comum?")
if usuario_a.intersection(usuario_b) : print(f"Sim\n")
else : print(f"Não\n")

print("Possuem exatamente as mesmas permissões?")
if usuario_a == usuario_b : print(f"Sim\n")
else : print(f"Não\n")