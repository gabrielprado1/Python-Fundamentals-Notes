### Listas - Armazenar de maneira sequencial qualquer objeto; Cria-se utilizando o construtor "list", função range ou colocando valores separados por vírgula em colchetes; objetos mutáveis, podem ser alterados os valores após criação.

frutas = ["laranja", "maca", "uva"]

frutas = []

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 42000000, 2020, 2900, "São Paulo", True]

# Acesso direto - lista é sequencia logo acessa seus dados usando índices começando no 0.

# índices negativos - suporta indexação negativa, começa em -1.

frutas = ["laranja", "maca", "uva"]
frutas [-1] # uva

# Lista pode armazenar outras listas, criando estruturas bidimensionais (tabelas) acessando índice de linha e coluna.

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0] # Primeira linha [1, "a", 2]
matriz[0][0] # Primeiro item da primeira linha '1'
matriz[0][-1] # '2'
matriz[-1][-1] # "c"

# Fatiamento - lembrar que começa com 0

lista = ['p', 'y', 't', 'h', 'o', 'n']

lista[2:]
lista[:2]
lista[1:3]
lista[0:3:2]
lista[::]
lista[::-1]

# Iterar listas - o mais comum é utilizando 'for'

carros = ['gol', 'celta', 'palio']

for carro in carros:
    print(carro)

# Função enumerate - saber qual o índice do obj dentro do laço 'for'

carros = ['gol', 'celta', 'palio']

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Compreensão de listas - sintaxe mais curta quando deseja-se: criar nova lista com valores de uma existente (filtro) ou nova lista aplicando modificações.

# Modo 1
numeros = [1,30,21,2,9,65,34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# Modo 2
numeros = [1,30,21,2,9,65,34]
pares = [numero for numero in numeros if numero % 2 == 0
]

# Modificando valores
numeros = [1,30,21,2,9,65,34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

# Vers 02
numeros = [1,30,21,2,9,65,34]
quadrado = [numero ** 2 for numero in numeros]

### Metodos para lista

# [].append - metodo para add objetos à lista. Lembrando que qualquer objeto pode ser add inclusive outras listas.

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, "Python", [40, 30, 20]]

# [].clear
print(lista) # [1, "Python", [40, 30, 20]]

lista.clear()

# [].copy - cria listas com id diferentes e o que se faz em uma não se reflete na outra.

lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(id(l2), id(lista))

l2[0] = 2 # Sairão diferentes no print

# [].count - quantas vezes o obj aparece na lista
cores = ["vermelho", x , x , x]
cores.count("vermelho") # 1 

# [].extend - fazer a juncao de listas e varios items de uma vez, ele nao substitui os itens semelhantes!
linguagens = [x, x, x]
linguagens.extend(["java", "csharp"])

# [].index - descobrir onde esta a primeira ocorrencia do obj
linguagens = [x, x, x, x,]
print(linguagens.index("java"))

# [].pop - conceito de pilha de pratos, ele sempre tira o ultimo elemento da lista, mas pode passar para o pop qual o indice que deseja remover
linguagens.pop(0)
linguagens.pop

# [].remove - retira passando o obj, ele remove apenas uma referencia do obj
linguagens = [x, x, x, x, "c"]
linguagens.remove("c")

# [].reverse - para fazer o espelhamento da lista, inverter.
linguagens.reverse()

# [].sort - ordenar a lista em ordem alfabetica
linguagens.sort()
linguagens.sort(key=lambda x: len(x), reverse=True)
# Função built in 'sorted'
sorted(linguagens, key=lambda x: len(x, reverse=True))

# len - tira o tamanho das coisas, de lenght
linguagens = [x, x, x, x, x]
len(linguagens) # 05



