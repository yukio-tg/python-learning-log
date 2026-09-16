# DESAFIO 1 (CALCULADORA ROBUSTA)
num_a = None
num_b = None
operacao = None
resultado = None


while num_b is None:
    try:
        if num_a is None : num_a = int(input("Insira valor 1\n"))
        elif num_b is None : num_b = int(input("Insira valor 2\n"))
    except ValueError:
        print("Insira valor válido!")

while operacao is None:
    print("Escolha operação: ")
    print("Digite: '+' para somar.")
    print("Digite: '-' para subtrair.")
    print("Digite: '*' para multiplicar.")
    print("Digite: '/' para dividir.")

    operacao = input()

    match operacao:
        case "+":
            resultado = num_a + num_b
        case "-":
            resultado = num_a - num_b
        case "*":
            resultado = num_a * num_b
        case "/":
            try:
                resultado = num_a / num_b
            except ZeroDivisionError:
                resultado = "Divisão por zero?"
        case _:
            print("Operação escolhida não existe. Tente novamente")
            operacao = None

print(resultado)