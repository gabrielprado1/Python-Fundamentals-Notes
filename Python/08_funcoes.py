### Funções em python - bloco de cód identificado pelo nome e pode ou não receber lista de parâmetros, com valores padrões ou não; programando de forma estruturada.

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem3(nome="Ânonimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem() # Executando
exibir_mensagem2(nome="Guilherme")
exibir_mensagem3()
exibir_mensagem(nome="Chappie")

# Retornando valores - 'return'; em python a função pode retornar mais de um valor. Toda função retorna None por PADRÃO.
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)

# Argumentos nomeados - chave:valor
def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) # Esse terceiro método seria o mais adequado

# Args e kwargs - pode-se combinar parâmetros obrigatórios com args e kwargs. Quando são definidos, o método recebe como (*args (tupla) e **kwargs (dicionário))

### Parâmetros especiais - ou por posição ou por nome

# Positional only
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

# Keyword only *
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

# Positional and Keyword hibrid

# Objetos de primeira classe - funções tbm são obj o que as tornam obj de primeira classe. Podemos atribuir funções à variáveis, passá-las como parâmetros para funções, usá-las como valores em estuturas de dados (listas, tuplas, dici) e usar como valor de retorno p uma função (closures)
def somar (a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(10, 10, somar)

op = somar
print(op(1, 23))

# Escopo local e global - dentro do bloco da função o escopo é local, logo alterações feitas em obj imutáveis ali serão perdidas qdo o método terminar de ser executado. Para usar obj globais utilizamos a keyword global, informa ao interpretador q a variável que está sendo manipulada no escopo local é global. essa NÃO é uma boa prática e deve ser evitada.
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_bonus(500)