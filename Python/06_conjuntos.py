### Conjuntos

# Sets - coleção que não possui obj repetidos, conjuntos matematicos ou elim itens duplicados; NÃO garante a ordem. Quando vc coloca os valores em modo conjunto e printa ele automaticamente já elimina os valores duplicados.

set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

set("abacaxi") # {"b","a","c","x","i"}

set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"} # é uma tupla!

# Conjuntos em python ñ suportam indexação e nem fatiamento. Caso queira isso é necessário converter o conjunto pra lista.

# Forma mais comum p percorrer dados de um conjunto é usando 'for'

# Enumerate

### Métodos classe Set

# {}.union
conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) # {1, 2, 3, 4}

# {}.intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b) # {2, 3}

# {}.difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}

# {}.symmetric_difference - A intersecção
conjunto_a.symmetric_difference(conjunto_b) # {1, 4}

# {}.issubset 
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) # True
conjunto_b.issubset(conjunto_a) # False

# {}.issuperset - o contrário do exemplo acima

# {}.isdisjoint
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b) # True
conjunto_a.isdisjoint(conjunto_c) # False

# {}.add - se o elem nao existir, é add; se já existe, é ignorado.
sorteio = {1, 23}

sorteio.add(25)
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(25) # {1, 23, 25, 42}

# {}.clear - limpa o set
sorteio.clear()

# {}.copy 
sorteio.copy()

# {}.discard - se for valor que existe ele discarta, se não existe o valor ele só ignora;
numeros = {1, 2, 3, 1, 2, 4, 5}

numeros.discard(2)

# {}.pop - no caso de conjuntos o pop sempre tira o valor da FRENTE (começo) da lista
numeros.pop()

# {}.remove - esse método dá erro se o elemento que foi pedido a ser removido não existe.
numeros.remove()

# len - tirar o tamanho do conjunto
len(numeros)

# in - verificar se esta no conjunto
1 in numeros
10 in numeros 


