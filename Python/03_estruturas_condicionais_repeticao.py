### Identação no Python é diferente. É com base nos espaços, diferentemente do Java (identação e blocos).

def sacar(valor: float):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")

sacar(100)

### Estruturas condicionais

# If - apenas 01 desvio
saldo = 2000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")

# If/else - 02 desvios. Se If for verdadeiro, é executado, senão, o segundo bloco é executado.
saldo = 2000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")

# If/Elif/Else - mais de 02 desvios; Elif é nova expressão lógica; Não existe n' máximo de eflis.
opcao = int(input("Infoem uma opcao:[1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção inválida")

# If aninhado - if dentro de if;
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque Realizado")
    elif saque <= (saldo + cheque_especial):
        print("Saque c uso do cheque esp")
    else:
        print("Não foi possivel realizar")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque Realizado")
    else:
        print("Saldo insuficiente")

# If ternário - única linha; primeira parte é caso seja verdadeiro; segunda parte é a expressão lógica, terceira retorno caso expressão não atendida.

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")

##### Estruturas de Repetição

# For (For/else)- percorrer objeto iterável; Quando sabemos o número exato de vezes que o bloco de código deve ser executado.
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("Executa no final do laço")

# Função built in Range
for numero in range (0, 11): # Sendo o 0 opcional
    print(numero, end="")

# Tabuada do 05
for numero in range(0, 51, 5): # (start, fim, step)
    print(numero, end=" ")

# While (While/else) - repetir um bloco de código várias vezes; não sabemos o n' exato de vezes q o bloco deve ser executado.
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n [2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário.")

# Break e Continue - continue quando quer pular execução e break quanto quiser parar.
opcao = -1

while True:
    numero = int(input("Informe um numero: "))

    if numero == 10:
        break

    print(numero)

for numero in range(100):

    if numero == 12:
        break

    # if numero == 12:
    # continue 

    if numero % 2 == 0:
        continue # números ímpares

