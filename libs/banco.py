import sqlite3

def criar_tabela():
    # Conecta ao banco de dados (cria o banco de dados se não existir)
    conn = sqlite3.connect('banco.sqlite')
    cur = conn.cursor()

    # Cria a tabela VIACEP
    cur.execute('''
        CREATE TABLE IF NOT EXISTS VIACEP (
            cep VARCHAR(255),
            logradouro TEXT,
            complemento TEXT,
            unidade TEXT,
            bairro TEXT,
            localidade TEXT,
            uf TEXT,
            estado TEXT,
            regiao TEXT,
            ibge TEXT,
            gia TEXT,
            ddd TEXT,
            siafi TEXT
        )
    ''')

    conn.commit()
    conn.close()

def ver_tabela():
    conn = sqlite3.connect('banco.sqlite')
    cur = conn.cursor()
    comando = 'SELECT * FROM VIACEP'
    cur.execute(comando)  # Aqui ocorre o erro se a tabela não existir
    dados = cur.fetchall()
    conn.close()
    return dados


def inserir_tabela(cep, logradouro, complemento, unidade, bairro, localidade, uf, estado, regiao, ibge, gia, ddd, siafi):
    #INSERIR INFORMAÇÕES DO BANCO
    conn = sqlite3.connect('banco.sqlite')
    # cursor object
    cur = conn.cursor()
    # Criar Tabela
    comando = f"""  INSERT INTO VIACEP (CEP, UNIDADE, UF, BAIRRO, LOCALIDADE, DDD, GIA, ESTADO, REGIAO, IBGE, COMPLEMENTO, LOGRADOURO, SIAFI)  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""" 
    value = (cep, unidade, uf, bairro, localidade, ddd, gia, estado, regiao, ibge, complemento, logradouro, siafi)
    cur.execute(comando, value)
    conn.commit()
    # Fechar coenxão
    conn.close()

criar_tabela()