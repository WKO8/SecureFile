import sqlite3

def db_function():
    # Conectando no BD e iniciando o Cursor
    conn = sqlite3.connect("./sqlite/keys_app.db")
    cursor = conn.cursor()
    # Criação da Tabela com as linhas
    cursor.execute("""CREATE TABLE IF NOT EXISTS users 
            (id text,
            nome text,
            email text,
            telefone integer,
            chave_cript text,
            chave_autent text
            )""")
    # Inserção de Dados do Primeiro Usuário
    user = [
    ('ID01',
     'WKO',
      'klodivilf@gmail.com',
       '00112233445',
        '20215900uw4uf69wx6fx933w',
         '412499412941244415564389')
    ]

    cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)", (user))

    # Criação da Tabela com as linhas
    cursor.execute("""CREATE TABLE IF NOT EXISTS users_data 
            (id text,
            beta text,
            beta_cript text,
            alpha text,
            secure_path text,
            unity_usb text,
            crypt_key text
            )""")
    # Inserção de Dados do Primeiro Usuário
    user_data = [
        ('ID01', 'abte_7210840586510319', '20215900uw4uf69wx6fx933w', 'palha_8511994129412443', 'C:\\Users\\username\\Desktop\\A\\B', 'D', b'y0mkre6iu9adtamm')
        ]

    cursor.executemany("INSERT INTO users_data VALUES (?, ?, ?, ?, ?, ?, ?)", (user_data))
    # Gravando os dados e encerrando a conexão com o BD
    conn.commit()
    conn.close()

db_function()