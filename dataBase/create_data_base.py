import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / 'bd_bank.db')

cursor = conexao.cursor()

# By default, SQLite does not have a foreign key supersede.
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        cpf INTERGER(11) UNIQUE NOT NULL,
        address VARCHAR(250) NOT NULL 
        )''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS account (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type VARCHAR(50),
        num INTERGER(11) UNIQUE,
        id_client INTEGER,
        FOREIGN KEY (id_client) REFERENCES clientes(id) )''')
