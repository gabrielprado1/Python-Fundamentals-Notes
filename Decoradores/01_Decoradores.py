### Inner functions - é possível definir funções dentro de outras funções
# Python permite que utilize-se funções como valores de retorno
def calculadora(operacao):
    def soma(a, b):
        return a + b
    
    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b
    
    def div(a, b):
        return a / b
    
    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div

print(calculadora("+")(2, 3))

##################################
def mensagem(nome):
    print("Executando nome")
    return f"Oi {nome}"

def mensagem_longa(nome):
    print("Executando mensagem longa")
    return f"Olá tudo bem com você {nome}'"

def executar(funcao):
    print("Executando executar")
    return funcao()

executar(mensagem("Joao"))

###################################
def principal():
    print("Executando a funcao principal")

    def funcao_interna():
        print("Executando a funcao interna")

    def funcao_2():
        print("executando a funcao 2")

    funcao_interna()
    funcao_2()

principal()

#######################

# Decorador simples
def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar")
        funcao()
        print("Faz algo depois de executar")
    return envelope

@meu_decorador
def ola_mundo():
    print("Olá mundo!")

print(ola_mundo())

# Açucar sintático - permite que vc use decoradores de maneira mais simples com o símbolo @

# Funções de decoração com argumentos - podemos usar *args e **kwargs na função interna, fazendo ela aceitar um n arbitrário ed argumentos posicionais e de palavras-chave
def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar")
        funcao(*args, **kwargs)
        print("Faz algo depois de executar")
    return envelope

@meu_decorador
def ola_mundo(nome):
    print("Olá mundo {nome}!")

ola_mundo("Gabriel")

# Retornando valores de funções decoradas - O decorador pode decidir se retorna o valor da função decorada ou ñ. Para que o valor seja retornado, a função envelope deve retornar o valor da função decorada
def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar")
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois de executar")
        return resultado
    return envelope

@meu_decorador
def ola_mundo(nome):
    print("Olá mundo {nome}!")
    return nome.upper()

resultado = ola_mundo("Gabriel")
print(resultado)

# Introspecção - capacidade de um obj saber sobre seus proprios atributos em tempo de execução
import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)
    
    return envelope

@meu_decorador
def ola_mundo(nome):
    print("Olá mundo {nome}!")

print(ola_mundo.__name__)