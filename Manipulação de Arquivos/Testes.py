arquivo = open("C:/Users/gabri/OneDrive/Desktop/Pastas/Estudos/Pastas Python/Manipulação de Arquivos/lorem.txt", "r")
print(arquivo.read()) # Retorna a string completa
print(arquivo.readline()) # Retorna apenas uma linha
print(arquivo.readlines()) # Retorna linha a linha separado numa lista

# Dica
while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()

#######################################################################################################################

arquivo = open("C:/Users/gabri/OneDrive/Desktop/Pastas/Estudos/Pastas Python/Manipulação de Arquivos/teste.txt", 'w')

arquivo.write('Escrevendo dados em um novo arquivo.')
arquivo.writelines(['\n', 'escrevendo', '\n','um', '\n', 'novo', '\n', 'texto'])

arquivo.close()
               
########################################################################################################################

# Fechando o arquivo corretamente
from pathlib import Path

ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / "lorem.txt", "r") as arquivo:
    print("Trabalhando com o arquivo")

print(arquivo.read())

###################################################################### 

# Trabalhando com CSV
import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Com writer
try:
    with open(ROOT_PATH / 'usuarios.csv', 'w', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id', 'nome'])
        escritor.writerow(['1', 'Maria'])
        escritor.writerow(['2', 'João'])
except IOError as exc:
    print(f'Erro ao criar o arquivo. {exc}')

# Com reader
try:
    with open(ROOT_PATH / 'usuarios.csv', 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row)
except IOError as exc:
    print(f'Erro ao criar o arquivo. {exc}')

# Lendo cada row de forma mais "apresentável"
COLUNA_ID = 0
COLUNA_NOME = 1

try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for idx, row in enumerate(leitor):
            if idx == 0:
                continue
            print(f"ID: {row[COLUNA_ID]}")
            print(f"Nome: {row[COLUNA_NOME]}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")

# Utilizando-se de dicionário para ler (melhor método)
try:
    with open(ROOT_PATH / "usuarios.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"ID: {row['id']}")
            print(f"Nome: {row['nome']}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")