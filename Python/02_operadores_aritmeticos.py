produto_1 = 10
produto_2 = 20

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2) # Divisão sem resto
print(produto_1 * produto_2)
print(produto_1 % produto_2) # Modulo
print(produto_1 ** produto_2) # Exponenciação

# Operadores de comparação, retorno é sempre valor booleano
saldo = 450
saque = 200
print(saldo == saque)
# Resposta = false
print(saldo != saque)
# Resposta = true pq significa 'diferente de'
print(saldo > saque)
print(saldo >= saque) # Maior ou igual
print(saldo < saque)
print(saldo <= saque) # Menor ou igual

# Operadores de atribuição, definir o valor inicial ou sobrescrever o valor de uma variavel
saldo = 500 # Atribuição simples
saldo += 200 # Atrib com adição
saldo -= 200 # *= /= //= %= **=

# Operadores lógicos
# Operador E - para ser true, td tem que ser true
saldo >= saque and saque <= limite

# Operador OU - para retornar true tem que ter pelo menos 01 condição true
saldo >= saque or saque <= limite

# Operador Negação, inverso do falso? True
not 1000 > 1500
# Resposta True

# Parênteses

# Operador de identidade
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
# Resposta = true
curso is not nome_curso
# Resposta = false
saldo is limite
# R = true

# Operadores de Associação - case sensitive
curso = "Curso de Python"
frutas = ["laranja","uva", "limao"]
saques = [1500, 100]

"Python" in curso
# R = True
"maca" not in frutas
# R = True
200 in saques
# R = False