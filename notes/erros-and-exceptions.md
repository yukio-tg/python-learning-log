# NOTAS:

## Geral

- Existem 3 tipos de erros:
    - Lógicos: Quando o programa não crasha, mas também não exibe o resultado esperado.
    - Erro durante a execução: Quando o programa enquanto roda se depara com uma informação que dá crash.
    - Erro de sintaxe: Quando o programa enquanto se prepara para executar se depara com algo que não consegue interpretar.

- Diferença entre 'Exception' e 'Error':
    - Error é algo fatal e grave para o programa. Algo que não pode ser resumido à uma inteiração de valores inválidos. Como por exemplo, o limite da memória RAM ter sido alcançada.
    - Exception é um error tratável que não encerra o programa automaticamente. Por exemplo um valor de tipo não tratável. O programador pode controlar saídas quando um erro desses surge.

## Erros comuns:

- ValueError: O tipo é aceitável mas o valor não. Exemplo: 'idade = int(doze)'
- TypeError: A operação não é válida por causa do tipo. Exemplo: 'resultado = "10" + 5'
- IndexError: Quando a posição acessada não existe. Exemplo: 'nomes = ["Aldren", "Lyra"].. print(nomes[10])'
- KeyError: Quando uma chave acessada no dicionário não existe. Exemplo: 'personagem = {"nome": "Aldren", "vida": 100}.. print(personagem["mana"])'
- ZeroDivisionError: Quando há divisão por zero.
