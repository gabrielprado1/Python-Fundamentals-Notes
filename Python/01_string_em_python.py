### Início em Python
nome = input("Informe o seu nome:")
idade = input("Informe a sua idd:")

print(nome, idade, sep="#")

# Maiúscula, minúscula e título
curso = "pYthon"

print(curso.upper())

print(curso.lower())

print(curso.title()) # Python

# Elim espaços em branco
curso = "    Python "

print(curso.strip())

print(curso.lstrip()) # Left strip (lado esq)
print(curso.rstrip()) # Right strip

# Junções e centralização
curso = "Python"

print(curso.center(10, "#"))

print(".".join(curso))

### Interpolação de variáveis

# Old style, %; não se usa mais.

# Format .format; dá pra se usar o índice, de 0 á infinito...

# f-string
nome = "Gabriel"
idade = 28
profissao = "Programador"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

# Formatar strings com f-string
PI = 3.14156

print(f"Valor de PI:{PI:.2f}") # PI: 3.14
print(f"Valor de PI: {PI:10.2f}") # PI:    3.14

### Fatiamento de strings; técnica para retornar substrings, informando: inicio (start), fim (stop) e passo (step).
# [start:stop[, step]]
nome = "Guilherme Arthur de Carvalho"

nome[0] # "G"
nome[:9] # "Guilherme"
nome[10:] # "Arthur de Carvalho"
nome[10:16] # "Arthur"
nome[10:16:2] # "Atu"
nome[:] # "Guilherme Arthur de Carvalho"

# Como espelhar a string
nome[::-1] 

### String multilinhas ou triplas, quando quer montar um menu ou uma mensagem diferente para o usuario.
nome = Gabriel 

mensagem = f"""
    Olá meu nome é {nome},
  Eu estou aprendendo Python
        Essa mensagem tem diferentes recuos.
"""
print("""
============ MENU ============
      1- Alcatra
      2- Macarrão
      3- Doce

==============================

Obrigado por ser nosso cliente!

    Volte sempre!
""")

