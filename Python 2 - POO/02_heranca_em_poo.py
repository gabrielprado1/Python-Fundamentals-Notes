# Herança em POO - é a capacidade de uma classe filha derivar ou herdar as caracteristicas e comportamentos da classe pai (base)

# Beneficios da herança: Representa bem os relacionamentos do mundo real; Fornece reutilização de código e permite add + recursos a uma classe sem modificá-la; é de natureza transitiva, se classe B herdar da A, todas as subclasses de B herdarão automaticamente de A também

# Sintaxe
class A:
    pass

class B(A):
    pass

# Herança simples - quando a classe filha herda apenas UMA classe pai, como no exemplo acima
class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return self.cor

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("preta", "abc-1234", 2)
moto.ligar_motor

carro = Carro("branco", "xde-221", 4)
carro.ligar_motor

caminhao = Caminhao("roxo", "gbhk-223", 8)
caminhao.ligar_motor


# Herança múltipla (não são todas as linguagens que implementam) - quando uma classe filha herda de várias classes pai
class A:
    pass

class B:
    pass

class C(A, B):
    pass

#####################################


