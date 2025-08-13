# Manipulando arquivos em python
file = open("example.txt", 'r')
file.close()

'r' # Somente leitura
'w' # Gravação
'a' # Anexar

# Lendo de um arquivo
file.read()
file.readline()
file.readlines()

# Lembrar de abrir o arquivo no modo correto
# Funções para escrever em um arquivo
file.write()
file.writelines()

##################################################################################################################

### Tratamento de exceção e manipulação de arquivos - mais comuns

# FileNotFoundError - o arq não pode ser encontrado no diretório especificado

# PermissionError - tentativa de abrir um arquivo sem as permissões adequadas p leitura ou gravação

# IOError - erro geral de E/S[entrada/saida], como problemas de permissão, falta de espaço em disco etc

# UnicodeDecodeError - erro ao tentar decodificar os dados de um arquivo de texto usando uma codificação inadequada

# UnicodeEncodeError - erro semelhante ao de cima, mas ao tentar codificar

# IsADirectoryError - quando é feita uma tentativa de abrir um diretório em vez de um arq de texto

from pathlib import Path

ROOTH_PATH = Path(__file__).parent

try:
    arquivo = open(ROOTH_PATH / 'novo-diretorio' / 'novo.txt', 'r')
except FileNotFoundError as exc:
    print("Arquivo ñ encontrado!")
    print(exc)
except IsADirectoryError as exc:
    print(f"Não foi possível abrir o arq: {exc}")
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")

#######################################################################################################################################

# Boas práticas na manipulação de arquivos

# Bloco with - gerenciamento de contexto (context manager) com a declaração 'with'; O gerenc permite trabalhar com os arqs de forma segura, garantindo seu fechamento correto, mesmo com exceções

# Verificar se o arq foi aberto c/ sucesso antes de executar operações

# Use a codificação correta - o argumento 'encoding' da função 'open()' permite especificar a codificação
try: 
    with open(ROOTH_PATH/'arquivo-utf-8.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('Aprendendo a manipular arquivos utilizando Python')
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")

########################################################################################################################################

### Trabalhando com arquivos CSV - é um formato de arquivo de texto, amplamente utilizado para armazenar dados tabulares. CSV significa 'Comma Separated Values'

# Práticas recomendadas 
# 1. Usar csv.writer e csv.reader
# 2. Fazer o tratamento correto das exceções
# 3. Ao gravar arquivos CSV definir o arg newline='' no método 'open'