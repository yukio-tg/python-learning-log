numero = int(input("digite um valor entre um e 100\n"))

baixo = 0
alto = 100
etapas = 1

while True:
    meio = (baixo+alto) // 2
    chute = meio
    
    if chute == numero:
        print(f"O seu valor é {meio}. Em {etapas} etapas.")
        break
    
    elif chute > numero:
        alto = meio
        etapas += 1
        
        print(f"{chute} alto!")
        
    else:
        baixo = meio
        etapas += 1
        
        print(f"{chute} baixo!")