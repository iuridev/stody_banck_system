from dataBase import create_data_base
from classes.client import client
from classes.accout import Accout
import sqlite3
from pathlib import Path
import random

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / 'dataBase' / 'bd_bank.db')

cursor = conexao.cursor()


#  CREATE CLIENT
client_1 = client('Maria Bezerra', 7463839203, 'rua 9 de julho')
# create_data_base.Insert_client(client_1.name, client_1.cpf, client_1.address)

# CREATE ACCOUNT
# RECUPERAR ID DE CLIENTE PARA foreign_keys
cpf = 7463839203
client_id = create_data_base.Recuperar_id_client(cpf)
print(client_id)

# CRIAR CONTA
conta = random.random()
create_data_base.Insert_accout('corrente', conta, client_id)

conexao.close()
