# Um iterador é um obj que contem um n contável de valores que podem ser iterados, significando assim que vc pode percorrer todos os valores; O protocolo consiste em dois métodos especiais:
# "__iter__()" e "__next__()"

class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
       return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration

for i in MeuIterador(numeros=[38, 13, 11]):
    print(i)

### Geradores - tipos especiais de iteradores; ao contrário das listas ou outros iteráveis, ñ armazenam todos os seus valoers na memória
# São definidos usando funções regulares, mas, ao invés de retornar valores usando 'return', utiliza-se 'yield'
def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)

# Usa-se gerador quando o código for mais simples