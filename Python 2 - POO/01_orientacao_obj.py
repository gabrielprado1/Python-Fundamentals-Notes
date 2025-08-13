### Orientação a Objetos em python - o paradigma de programação orientada a objetos estrutura o código abstraindo problemas em obj do mundo real, facilitando o entendimento e tornando-o mais modular e extensível. Conceitos chave: classes e objetos

# Classes e objetos - classe define as caracteristicas e comportamentos de um objeto, mas nao conseguimos usá-las diretamente. Objetos podemos usá-los e possuem caracteristicas e comportamentos que foram definidos nas classes

### Construtores e destrutores

# Construtor - é sempre executado qundo uma nova instância da classe é criada. Neste metodo inicializamos o estado do nosso obj. Para declarar o método construtor da classe, criamos um método com nome __init__
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

# As variáveis que aparecem dentro da classe como nome, cor, acordado são chamados de ATRIBUTOS

# Destrutor - é sempre executado quando uma instância (obj) é destruida. Não são tão necessários em python. Para declarar o método destrutor criamos um com o nome de __del__
class Cachorro:
    def __del__(self):
        print("Destruindo a instância")

c = Cachorro()
del c

#############################
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe...")
    
    def falar(self):
        print("Au au au!")

    def criar_cachorro(self):
        c = Cachorro("Zeus", "Branco e preto", acordado=False)
        print(c.nome)

c = Cachorro("Chappie", "amarelo")
c.falar()