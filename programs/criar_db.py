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
     'Matheus',
      'klodivilf@gmail.com',
       '31997489888',
        'b512090093lgg9xg4ul63wx3',
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
        ('ID01', 'abte_7210840586510319', 'b512090093lgg9xg4ul63wx3', 'palha_8511994129412443', 'C:\\Users\\w_ko\\Área de Trabalho\\A\\B', 'D', b'y0mkre6iu9adtamm')
        ]

    cursor.executemany("INSERT INTO users_data VALUES (?, ?, ?, ?, ?, ?, ?)", (user_data))
    # Gravando os dados e encerrando a conexão com o BD
    conn.commit()
    conn.close()

db_function()