### Encapsulamento - descreve a ideia de agrupar dados e os métodos que manipulam esses dados em uma unidade, impondo restrições ao acesso direto a variáveis e métodos e poed evitar a modificação acidental de dados; A variável de um obj só pode ser alterada pelo método desse obj

# class Conta:
#     pass
# - saldo: float # Método privado por segurança
# + depositar (valor: float)
# + sacar(valor: float)

# Modificadores de acesso - python não tem palavras reservadas, porém usamos convenções no nome do recurso, para definir se é publica ou privada

# Público - pode ser acessado de fora da classe; Particular, só pode ser acessado na classe

# Todos os recursos são públicos, a menos que o nome inicie com underline

class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo # Método privado
        self.nro_agencia = nro_agencia
    
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor
    
    def mostrar_saldo(self):
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo)

##### Properties - property(), cria atributos gerenciados em suas classes. Esses atributos, tbm conhecidos como propriedades, podem ser usados qdo precisa-se modificar sua implementação interna SEM alterar a API pública da classe

class Foo:
    def __init__(self, x=None):
        self._x = x
    
    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = -1

foo = Foo(10)
print(foo.x)

#######################################
class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self._ano_nascimento

pessoa = Pessoa("Gabriel", 1997)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}") 