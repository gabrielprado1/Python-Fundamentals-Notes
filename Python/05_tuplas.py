### Tuplas - principal diferença com listas é que tuplas são imutáveis enquanto listas são mutáveis.
# Pra fazer a tupla coloca os valores entre () e com uma virgula no final (pra ñ confundir com predecencia de operadores) do ultimo item. Os valores permanecerao os mesmos ate o fim da execucao do programa.

frutas = ("x", "x", "x",)

letras = tuple("python",)

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

# Acesso direto - tupla é sequencia então usa índices a partir do 0 e tem índices negativos também.

frutas = ("x", "y", "z",)
frutas[0] # x
frutas[2] # y
frutas[-1] # z

# Tuplas aninhadas - podem armazenar TODOS os tipos de obj em Python. Tuplas armazenando outras tuplas, tabelas.

# Fatiamento

### Metodos na tupla

#().count
cores = ("x", "x",)
cores.count("vermelho")

# ().index
cores.index("java")

# len - tamanho total
len(linguagens)
