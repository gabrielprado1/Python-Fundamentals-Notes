### Dicionários: chave - obj imutavel, o valor que vem acompanhado pode ser qlq tipo de obj. São delimitados por chaves {}, contem uma lista de pares chave:valor separada por ,

pessoa = {"nome": "Guilherme", "idade": 28}

pessoa = dict(nome="Guilherme", idade=28)

pessoa["telefone"] = "3333-1234" # Adicionando novos valores à "pessoa"

# Os dados são acessados e modificados atraves da chave
pessoa["nome"] # "Guilherme"
pessoa["idade"] # 28

pessoa["nome"] = "Maria" # Subscrevendo

### Dicionarios aninhados - dicionarios podem armazenar qlq tipo de obj em python como valor, desde q a chave seja imuavel como strings e numeros.

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
}

contatos["giovanna@gmail.com"]["telefone"] # 3443-2121, Acessando um dado especifico do dicionario aninhado

### Iterar dicionários - usando for
for chave in contatos:
    print(chave, contatos[chave])

# Tuplas
for chave, valor in contatos.items():
    print(chave, valor)

### Métodos da classe dict

# .clear
contatos.clear()

# .copy - qdo quer manipular o dici mas n alterar os dados do original
contatos.copy()

# .fromkeys - cria chaves p vc de uma vz só
dict.fromkeys(["nome"], ["telefone"])

dict.fromkeys(["nome"], ["telefone"], "vazio")

# .get - quando ñ sabe se a chave existe ou não no dici
contatos.get("chave")
contatos.get("chave", {}) # retorna o dici vazio

# .items - comando for; tuplas
for chave, valor in contatos.items():
    print(chave, valor)

# .keys - retorna todas as chaves
contatos.keys()

# .pop - remover um valor e retorna ele no print
contatos.pop()

resultado = contatos.pop("guilherme@", "não encontrado") # Pra ñ dar erro

# .popitem - não informa a chave, vai retirando itens na sequência
contatos.popitem()

# .setdefault - se ñ tiver ele add com o valor colocado; se existe ele retorna o valor existente e o mantém
contatos.setdefault()

# .update - deixa att o dici com outro dici, se ja existe a chave, subscreve, senão, adiciona o novo conteúdo
contatos.update()

# .values - retorna todos os valores
contatos.values()

# .in - verificar se a chave existe ou ñ de forma "elegante"
resultado = "guilherme@gmail.com" in contatos # True

# .del
del contatos["guilherme@gmail.com"]["telefone"] # Remove a chave específica

del contatos["giovanna@gmail.com"] # Remove toda a chave