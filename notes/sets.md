A principal diferença entre sets e listas, é que sets, não acumulam elementos iguais. Ou seja:

nomes = ["Aldren", "Lyra", "Aldren", "Kael", "Lyra"]
Aldren
Lyra
Aldren
Kael
Lyra
é preservado tudo!


já o mesmo em sets:
nomes = ["Aldren", "Lyra", "Aldren", "Kael", "Lyra"]
Aldren
Lyra
Kael
Apenas elementos únicos!


para criar um set vazio é necessário avisar que é um set!

dados = set()


.add() adiciona um novo elemento
.remove() remove um elemento, mas se ele não existir temos um erro.
.discard() remove um elemento, sem erros mesmo se não existir.