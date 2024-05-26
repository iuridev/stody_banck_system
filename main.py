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
client_1 = client('Marta', 23043245366, 'rua maira da Vila')
create_data_base.Insert_client(client_1.name, client_1.cpf, client_1.address)

# CREATE ACCOUNT
# RECUPERAR ID DE CLIENTE PARA foreign_keys
cpf = client_1.cpf
client_id = create_data_base.Recuperar_id_client(cpf)

# CRIAR CONTA
conta = random.randint(1, 1000)
create_data_base.Insert_accout('corrente', conta, client_id)

create_data_base.depositar(500.0, conta)
create_data_base.sacar(300, conta)
saldo = create_data_base.verficar_saldo(conta)
nome = client_1.name

print(f"o Usuario {nome}, tem na conta {conta}, o saldo de R$`{saldo:.2f}")

conexao.close()
