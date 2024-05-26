import sqlite3
from pathlib import Path


ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / 'bd_bank.db')

cursor = conexao.cursor()
# cursor.row_factory = sqlite3.Row

# By default, SQLite does not have a foreign key supersede.
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        cpf INTERGER UNIQUE NOT NULL,
        address VARCHAR(250) NOT NULL
        )''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS account (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type VARCHAR(50),
        num INTERGER(11) UNIQUE,
        id_client INTEGER,
        saldo DECIMAL,
        FOREIGN KEY (id_client) REFERENCES clientes(id) )''')


def Insert_client(nome, cpf, address):
    data = (nome, cpf, address)
    try:
        cursor.execute(
            "INSERT INTO clientes (nome, cpf, address) VALUES (?,?,?)", data)
        conexao.commit()
    except sqlite3.IntegrityError as e:
        print(f"Erro na operação: {e}")
    except sqlite3.OperationalError as e:
        print(f"Erro 2: {e}")


def Insert_accout(type, num, idd_cliente):
    SALDO_INICIAL = 10.20
    data = type, num, idd_cliente, SALDO_INICIAL
    try:
        cursor.execute(
            "INSERT INTO account (type, num, id_client, saldo) VALUES (?,?,?,?)", data)
        conexao.commit()
    except sqlite3.IntegrityError as e:
        print(f"Erro na operação: {e}")
    except sqlite3.OperationalError as e:
        print(f"Erro 2: {e}")


def Recuperar_id_client(cpf):
    try:
        cursor.execute('SELECT id FROM clientes WHERE cpf=?', (cpf,))
        result = cursor.fetchone()

        if result:
            return result[0]
        else:
            return None
    except Exception as e:
        print(f"Erro tratado 1: {e}")


def verficar_saldo(conta):
    try:
        cursor.execute('SELECT saldo FROM account WHERE num=?', (conta,))
        result = cursor.fetchone()

        if result:
            return float(result[0])
        else:
            return None
    except Exception as e:
        print(f"Erro tratado 2: {e}")


def depositar(valor, conta):
    saldo = verficar_saldo(conta)
    print(saldo)
    if saldo != None:
        atualizar = saldo + valor
        print(atualizar)
        data = atualizar, conta
        print(conta)
        try:
            cursor.execute('UPDATE account SET saldo=? WHERE num=?', data)
            conexao.commit()

        except Exception as e:
            print(f"Erro tratado 3: {e}")
    else:
        return None


def sacar(valor, conta):
    saldo = verficar_saldo(conta)
    if saldo >= valor:
        atualizar = saldo - valor
        data = atualizar, conta
        try:
            cursor.execute('UPDATE account SET saldo=? WHERE num=?', data)
            conexao.commit()
        except Exception as e:
            print(f"Erro tratado 4: {e}")
    else:
        return None
    pass
