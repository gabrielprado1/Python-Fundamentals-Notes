### OS SHUTIL
import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Criar um diretório
os.mkdir(ROOT_PATH / 'novo-diretorio')

arquivo = open(ROOT_PATH / 'novo.txt', 'w')
arquivo.close

# Renomear um arquivo
os.rename(ROOT_PATH / 'novo.txt', ROOT_PATH / 'alterado.txt')

# Remover um arquivo
os.remove(ROOT_PATH/'novo.txt')

# Mover um arquivo
shutil.move(ROOT_PATH / 'novo.txt', ROOT_PATH / 'novo-diretorio' / 'novo.txt')
