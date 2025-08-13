### Variáveis de classe e instância

# Atributos do obj - todos os obj nascem com mesmo n de atributos e de classe e instancia. Atributos de INSTÂNCIA sao diferentes pra cada obj (cada obj tem uma cópia), já os de classe são compartilhados entre os obj
class Estudante:
    escola = "DIO" # Variável de classe

    def __init__(self, nome, matricula):
        self.nome = nome 
        self.matricula = matricula 
    
    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovana", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = 'Python'
aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)

# Métodos de classe - ligados a ela e não ao obj; tem acesso ao estado da classe, pois recebem um parâmetro que aponta para ela e NÃo para o obj 'cls'

# Métodos estáticos - nao recebe um 1o argumento explícito; esse método não pode acessar ou morificar o estado da classe

# Quando usar cada um - Geralmente usa-se método de classe para criar métodos de fabrica e métodos estáticos para criar funções utilitárias
class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

p = Pessoa.criar_de_data_nascimento(1997, 2, 12, "Gabriel")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(16))
print(Pessoa.e_maior_idade(28))

### Classes abstratas - é utilizada para criar contratos; NÃO podem ser instanciadas

# Interface em python - conceitua-se em definir um contrato, onde são declarados os métodos (o que deve ser feito) e suas respectivas assinaturas.

# Criando classes abtratas com módulo abc - por padrão, o python não fornece classe abstratas,e  sim um módulo que fornece a base para defini-las, sendo chamado de Abc (Abstract Base Class); ABC funciona decorando métodos da classe base como abstratos e registrando classes concretas como implementações da base abstrata. Um método se torna abstrato quando decorado com '@abstractmethod'

from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)