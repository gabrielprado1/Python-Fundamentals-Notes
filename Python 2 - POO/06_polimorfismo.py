### Polimorfismo - muitas formas; Significa o mesmo nome de função (mas assinaturas diferentes), sendo usado para tipos diferentes

# Mesmo método com comportamento diferente - na herança, a classe flha herda os métodos da classe pai. Porém é possível modificar um método em uma classe filha herdada da classe pai; Útil nos casos em que o método herdado não se encaixa perfeitamente
class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar...")

# FIXME: Exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

def plano_voo(obj):
    obj.voar()

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())

### Pra fazer polimorfismo precisa da herança