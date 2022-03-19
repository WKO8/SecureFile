#-------------------------
# Importar módulos
#-------------------------
from criar_db import db_function
#-------------------------
# Importando bibliotecas
from colorama import Fore
from string import punctuation, ascii_uppercase, ascii_letters, ascii_lowercase, digits
from random import choice, randint, sample
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
import os
import shutil
import sqlite3
import pyaes
import glob
import smtplib
#-------------------------
# Variáveis Gerais
#-------------------------
# Cor
#-------------------------
amarelo = Fore.YELLOW
azul = Fore.BLUE
verde = Fore.GREEN
vermelho = Fore.RED
resetar = Fore.RESET
#-------------------------
# Listas
#-------------------------
id_usuario = []
nome_usuario = []
email_usuario = []
telefone_usuario = []
caminho_seguro = []
unidade_usb = []
arquivos_pasta = []
hash_alphas = []
hash_betas = []
chave_cript = []
hash_betas_cripto = []
hash_betas_descripto = []
chave_autenticacao = []
#-------------------------
# Strings
#-------------------------
id_request = ""
chave_autenticacao_usuario = ""
pasta_segura = "Secure File"
host = "smtp.gmail.com"
port = "587"
login = "ibrkt.sys@gmail.com"
senha = "1b!rk$tsys"
#-------------------------
# Booleanas
#-------------------------
confirmacao_autenticacao = False
confirmacao_descriptografada = False
confirmacao_entrada = False
confirmacao_criptografada = False
#-------------------------

class Validacao():
    def validarMenu():
        while True:
            print(f"{azul}-{resetar}"*50)
            print(f"{azul}{'MENU INICIAL':^50}{resetar}")
            print(f"{azul}-{resetar}"*50)
            print(f"[ 1 ] Entrar\n[ 2 ] Cadastrar\n[ 3 ] Descriptografar\n[ 4 ] Reenviar Chaves\n[ 5 ] Sair")
            print(f"{azul}-{resetar}"*50)
            try:
                opcao = int(input("Qual das opções você deseja? "))
            except (ValueError, TypeError):
                print(f"{vermelho}Por favor, digite somente números de 1 a 5{resetar}")
            except KeyboardInterrupt:
                print(f"\n{azul}A entrada de dados foi interrompida pelo usuário.{resetar}")
                Validacao.validarMenu()
                
            else:
                if opcao is not None:
                    if opcao > 5 or opcao < 1:
                        print(f"{vermelho}Por favor, digite somente números de 1 a 5{resetar}")
                    elif opcao == 1:
                        Validacao.entrar()
                    elif opcao == 2:
                        Importacao.importar_listas()
                        Validacao.cadastrar()
                    elif opcao == 3:
                        Criptografia.descriptografar()
                    elif opcao == 4:
                        Email.reenviar()
                    else:
                        exit()


    def cadastrar():
        global caminho_arq, unidade_usb

        while True:
            try:
                nome = str(input("Nome: "))
                valid_name = re.search(r'^\b[a-zA-Z]{3,}[a-zA-Z0-9]*?\b$', nome)
            except KeyboardInterrupt:
                print(f"\n{azul}A entrada de dados foi interrompida pelo usuário.{resetar}")
                Validacao.validarMenu()
            else:
                if nome == "" or valid_name == None:
                    print(f"{vermelho}Por favor, digite um nome válido.\n[*] Os 3 primeiros dígitos devem ser letras.\n[*] Não digite caracteres especiais.\n[*] Sem acentos.\n[*] Sem espaços.{resetar}")
                elif nome is not None:
                    while True:
                        try:
                            email = str(input("Email: "))
                            email = email.lower()
                            valid_email = re.search(r'^\b[a-z_\.]{3,}[a-z0-9_\.]*@[a-z]{3,}\.[a-z]{2,}\b$', email)
                        except KeyboardInterrupt:
                            print(f"\n{azul}A entrada de dados foi interrompida pelo usuário.{resetar}")
                            Validacao.validarMenu()
                        else:
                            if valid_email == None:
                                print(f"{vermelho}Por favor, digite um email dentro do padrão válido.{resetar}")
                            elif email in email_usuario:
                                print("", "-"*55, "\n", " ",f"{azul}Já existe um usuário cadastrado com este email.{resetar}\n", "-"*55)
                                input(f"{azul}-=- Aperte ENTER para continuar -=-{resetar}")
                                Validacao.validarMenu()
                            elif valid_email is not None:
                                while True:
                                    try:
                                        caminho = str(input("Caminho da Pasta em que se localiza o arquivo: "))
                                        verifica_pasta = os.path.exists(caminho)
                                    except KeyboardInterrupt:
                                        print(f"\n{azul}A entrada de dados foi interrompida pelo usuário.{resetar}")
                                        Validacao.validarMenu()
                                    else:
                                        if caminho == "" or not verifica_pasta:
                                            print(f"{vermelho}Por favor, digite um caminho válido e existente.\n[*] Exemplo: C:\\Users\\Usuario\\Área de Trabalho\\Pasta{resetar}")
                                        elif verifica_pasta:
                                            while True:
                                                try:
                                                    unidade = str(input("Unidade USB (Ex: D): "))
                                                    verifica_unidade = os.path.exists(f"{unidade}:/")
                                                except KeyboardInterrupt:
                                                    print(f"\n{azul}A entrada de dados foi interrompida pelo usuário.{resetar}")
                                                    Validacao.validarMenu()
                                                else:
                                                    if verifica_unidade != True:
                                                        print(f"{vermelho}Por favor verifique se a unidade do USB está correta.\n[*] Ex.: D:/\n[*] Informe somente a letra da unidade: D\n[*] Certifique-se que o dispositivo está conectado no PC.{resetar}")
                                                    else:
                                                        while True:
                                                            try:
                                                                telefone = input("Telefone: ")
                                                                valid_phone = re.search(r'\b[0-9]{11}\b', telefone)
                                                            except KeyboardInterrupt:
                                                                print(f"\n{azul}A entrada de dados foi interrompida pelo usuário.{resetar}")
                                                                Validacao.validarMenu()
                                                            else:
                                                                if valid_phone == None:
                                                                    print(f"{vermelho}Por favor, digite um telefone válido.\n[*] 11 dígitos.\n[*] Sem caracteres especiais.\n[*] Sem espaço.{resetar}")
                                                                elif int(telefone) in telefone_usuario:
                                                                    print("", "-"*55, "\n", " ",f"{azul}Já existe um usuário cadastrado com este telefone.{resetar}\n", "-"*55)
                                                                    input(f"{azul}-=- Aperte ENTER para continuar -=-{resetar}")
                                                                    Validacao.validarMenu()
                                                                elif valid_phone is not None:
                                                                    while True:
                                                                        try:
                                                                            print(f"\n{azul}--- Seus Dados ---\nNome: {nome}\nEmail: {email}\nTelefone: {telefone}\nCaminho da Pasta: {caminho}\nUnidade do USB: {unidade}\n", "-"*15, f"{resetar}")
                                                                            confirmacao_dados = int(input(f"[1] Sim\n[2] Não\nSeus dados estão corretos? "))
                                                                            if confirmacao_dados > 2 or confirmacao_dados < 1:
                                                                                raise ValueError
                                                                        except (ValueError, TypeError):
                                                                            print(f"{vermelho}Por favor, digite um valor válido.\n[*] 1 ou 2\n[*] Sem espaços.{resetar}")
                                                                        else:
                                                                            if confirmacao_dados == 1:
                                                                                print(f"{azul}Realizando o cadastro...{resetar}")
                                                                                Gerador.gerar_dados(nome, email, telefone, caminho, unidade)
                                                                                Validacao.validarMenu()
                                                                            else:
                                                                                Validacao.cadastrar()


    def entrar():
        Verificacao.verificar_usuario()
        if id_request != "":
            Verificacao.verificar_descriptografada()

            if confirmacao_entrada == True and confirmacao_autenticacao == True:
                print(f"{azul}={resetar}"*50)
                print(f"{azul}{'ACESSO PERMITIDO!':^50}{resetar}")
                print(f"{azul}={resetar}"*50)

                Gerador.regerar()
                Validacao.escolha_entrada()
                Validacao.validarMenu()
            else:
                print(f"{vermelho}={resetar}"*50)
                print(f"{vermelho}{'ACESSO NEGADO':^50}{resetar}")
                print(f"{vermelho}={resetar}"*50)

                Validacao.validarMenu()


    def escolha_entrada():
        while True:
            print(f"{azul}={resetar}"*50)
            print(f"[1] Criptografar o(s) arquivo(s)\n[2] Descriptografar o(s) arquivo(s)\n[3] Sair")
            print(f"{azul}={resetar}"*50)
            try:   
                escolha = int(input("Qual opção deseja? "))
                if escolha < 1 or escolha > 3 or escolha == None:
                    raise ValueError
            except (ValueError, TypeError):
                    print(f"-"*50)
                    print(f"\n{vermelho}Por favor, digite somente números de 1 a 3.{resetar}")
                    print(f"-"*50)
            except KeyboardInterrupt:
                print(f"\n{azul}A entrada de dados foi interrompida pelo usuário.{resetar}")
                Validacao.validarMenu()
            else:
                unidade_do_usb = unidade_usb[id_usuario.index(id_request)]
                caminho_usb = f"{unidade_do_usb}:\\{pasta_segura}"
                caminho_arq = caminho_seguro[id_usuario.index(id_request)]
                chave_criptografia = chave_cript[id_usuario.index(id_request)]

                if escolha == 3:
                    break
                elif escolha in [1,2]:
                    verifica_usb = os.path.exists(f"{unidade_do_usb}:\\")
                    verifica_pasta = os.path.exists(f"{caminho_arq}")
                    if verifica_usb:
                        if verifica_pasta:
                            shutil.move(caminho_arq, caminho_usb)
                            if escolha == 1:
                                Criptografia.criptografar_arquivos(chave_criptografia, caminho_usb)
                            elif escolha == 2:
                                print(f"{azul}={resetar}"*50)
                                print(f"{verde}{'DESCRIPTOGRAFANDO OS ARQUIVOS...':^50}{resetar}")
                                print(f"{azul}={resetar}"*50)
                                Criptografia.descriptografar_arquivos(chave_criptografia, caminho_usb)
                                print(f"{azul}={resetar}"*50)
                                print(f"{verde}{'ARQUIVOS DESCRIPTOGRAFADOS COM SUCESSO':^50}!{resetar}")
                                print(f"{azul}={resetar}"*50)
                        else:
                            if escolha == 1:
                                 Criptografia.criptografar_arquivos(chave_criptografia, caminho_usb)
                            elif escolha == 2:
                                print(f"{azul}={resetar}"*50)
                                print(f"{verde}{'DESCRIPTOGRAFANDO OS ARQUIVOS...':^50}{resetar}")
                                print(f"{azul}={resetar}"*50)
                                Criptografia.descriptografar_arquivos(chave_criptografia, caminho_usb)
                                print(f"{azul}={resetar}"*50)
                                print(f"{verde}{'ARQUIVOS DESCRIPTOGRAFADOS COM SUCESSO':^50}!{resetar}")
                                print(f"{azul}={resetar}"*50)
                    else:
                        print(f"\n{vermelho}Nenhum pendrive de unidade {unidade_do_usb} foi encontrado.\n[*] Insira no seu computador o mesmo pendrive\nde quando você fez o cadastro.{resetar}")


class Verificacao():
    def verificar_usuario():
        global chave_autenticacao_usuario

        Verificacao.pedir_id()
        
        if id_request != "":
            # Pegar chave de autenticação no BD
            # Conectando no BD e iniciando o Cursor
            conn = sqlite3.connect("./sqlite/keys_app.db")
            cursor = conn.cursor()
            # Procurar Chave de Autenticação do Usuário Atual 
            cursor.execute("SELECT chave_autent FROM users WHERE id = (?)", (id_request,))
            item = cursor.fetchone()
            chave_autenticacao_usuario = item
            # Gravando os dados e encerrando a conexão com o BD
            conn.commit()
            conn.close()

            chave_autenticacao_usuario = chave_autenticacao_usuario

            Verificacao.verificar_autenticacao()


    def verificar_autenticacao():
        global confirmacao_autenticacao

        # Verificar Chave de Autenticação no BD
        # Conectando no BD e iniciando o Cursor
        conn = sqlite3.connect("./sqlite/keys_app.db")
        cursor = conn.cursor()
        # Pegando Usuário Referente à Chave de Autenticação 
        cursor.execute("SELECT chave_autent FROM users WHERE id = (?)", (id_request,))
        item = cursor.fetchone()
        # Gravando os dados e encerrando a conexão com o BD
        conn.commit()
        conn.close()

        if item == chave_autenticacao_usuario:
            confirmacao_autenticacao = True
        else:
            confirmacao_autenticacao = False


    def verificar_descriptografada():
        global id_request, confirmacao_entrada, confirmacao_descriptografada
        temp_key_request = ""

        # Pegar Chave Descriptografada no BD
        # Conectando no BD e iniciando o Cursor
        conn = sqlite3.connect("./sqlite/keys_app.db")
        cursor = conn.cursor()
        # Execução 
        cursor.execute("SELECT beta FROM users_data WHERE id = (?)", (id_request,))
        item = cursor.fetchone()[0]
        # Gravando os dados e encerrando a conexão com o BD
        conn.commit()
        conn.close()
        
        while temp_key_request != item:
            temp_key_request = str(input("Chave Descriptografada: "))
            if temp_key_request == item:
                confirmacao_entrada = True
            elif temp_key_request == "00":
                print("="*50)
                Validacao.validarMenu()
            else:
                print("", "-"*50, "\n", " "*8, f"{vermelho}Chave descriptografada inválida.{resetar}\n", "-"*50)
                if confirmacao_descriptografada == True:
                    print(f"{azul}Para voltar ao menu inicial digite: 00{resetar}")
                else:
                    print("="*50)
                    print(" "*3, f"{vermelho}Você ainda não descriptografou a chave.{resetar}")
                    print(" "*3, f"{azul}Para descriptografá-la acesse a opção 3\n{resetar}", " "*11, f"{azul}no menu inicial.{resetar}")
                    print("="*50)
                    break


    def verificar_criptografada():
        global confirmacao_criptografada, id_request
        temp_key_request = ""

        # Pegar Chave Descriptografada no BD
        # Conectando no BD e iniciando o Cursor
        conn = sqlite3.connect("./sqlite/keys_app.db")
        cursor = conn.cursor()
        # Execução 
        cursor.execute("SELECT chave_cript FROM users WHERE id = (?)", (id_request,))
        item = cursor.fetchone()[0]
        print("-"*30)
        # Gravando os dados e encerrando a conexão com o BD
        conn.commit()
        conn.close()

        while temp_key_request != item:
            temp_key_request = str(input("Chave Criptografada: "))
            if temp_key_request == item:
                confirmacao_criptografada = True
            elif temp_key_request == "00":
                print("="*50)
                break
            else:
                print("", "-"*50, "\n", " "*9, f"{vermelho}Chave criptografada inválida.{resetar}\n", "-"*50)
                print(f"{azul}Para voltar ao menu inicial digite: 00{resetar}")
                
    def pedir_id():
        global id_request
        while True:
            try:
                print(f"{azul}Para voltar ao menu inicial digite: 00{resetar}")
                id_request = str(input("Informe o ID: "))
            except (ValueError, TypeError):
                print(f"{vermelho}-{resetar}"*50)
                print(f"{vermelho}{'ID inválido':^50}{resetar}")
                print(f"{vermelho}-{resetar}"*50)
            except KeyboardInterrupt:
                print(f"\n{azul}A entrada de dados foi interrompida pelo usuário.{resetar}")
                Validacao.validarMenu()
                
            else:
                if id_request == "00":
                    print("="*50)
                    id_request = ""
                    break
                for _ in id_request:
                    if _ in punctuation:
                        print(f"{azul}Por favor, digite somente alfanuméricos.{resetar}")
                        id_request = ""
                else:
                    # Conferir ID no BD
                    # Conectando no BD e iniciando o Cursor
                    conn = sqlite3.connect("./sqlite/keys_app.db")
                    cursor = conn.cursor()
                    # Procurar Chave de Autenticação do Usuário Atual
                    while True:
                        try:
                            cursor.execute("SELECT * FROM users WHERE id = (?)", (id_request,))
                        except sqlite3.OperationalError:
                            db_function()
                        else:
                            item = cursor.fetchone()

                            # Validações de Existência do ID
                            if item == None:
                                print("", "-"*50, "\n", " "*18, f"{vermelho}ID inválido.{resetar}\n", "-"*50)
                                id_request = ""
                            elif item != None and item[0] == id_request:
                                break
                    break


class Criptografia():
    def criptografia_hash():
        hash_para_criptografar = hash_betas_cripto[len(hash_betas_cripto)-1]
        for i in hash_para_criptografar:
            if i == "7":
                hash_para_criptografar = hash_para_criptografar.replace(f"{i}", "f")
            elif i == "8":
                hash_para_criptografar = hash_para_criptografar.replace(f"{i}", "w")
            elif i == "0":
                hash_para_criptografar = hash_para_criptografar.replace(f"{i}", "x")
            elif i == "2":
                hash_para_criptografar = hash_para_criptografar.replace(f"{i}", "u")
            elif i == "1":
                hash_para_criptografar = hash_para_criptografar.replace(f"{i}", "l")
            elif i == "5":
                hash_para_criptografar = hash_para_criptografar.replace(f"{i}", "g")

        for k in range(1, 7):
            if hash_para_criptografar[int(k-1):int(k)] == "b":
                hash_para_criptografar = hash_para_criptografar.replace("b", "2")

            elif hash_para_criptografar[int(k-1):int(k)] == "e":
                hash_para_criptografar = hash_para_criptografar.replace("e", "5")
            
            elif hash_para_criptografar[int(k-1):int(k)] == "t":
                hash_para_criptografar = hash_para_criptografar.replace("t", "20")
            
            elif hash_para_criptografar[int(k-1):int(k)] == "a":
                hash_para_criptografar = hash_para_criptografar.replace("a", "1")
            
            elif hash_para_criptografar[int(k-1):int(k)] == "_":
                hash_para_criptografar = hash_para_criptografar.replace("_", "900")

        hash_betas_cripto[len(hash_betas_cripto)-1] = hash_para_criptografar
        hash_betas_descripto.append(hash_para_criptografar)


    def descriptografar():
        Verificacao.verificar_usuario()
        if id_request != "":
            Verificacao.verificar_criptografada()

            if confirmacao_criptografada == True and confirmacao_autenticacao == True:
                print(f"{azul}={resetar}"*50)
                print(f"{verde}{'ACESSO PERMITIDO À DESCRIPTOGRAFIA!':^50}{resetar}")
                print(f"{azul}={resetar}"*50)

                Criptografia.descriptografia_hash()
                
            else:
                print(f"{vermelho}={resetar}"*50)
                print(f"{vermelho}{'ACESSO NEGADO À DESCRIPTOGRAFIA!':^50}{resetar}")
                print(f"{vermelho}={resetar}"*50)


    def descriptografia_hash():
        global id_request, confirmacao_descriptografada

        print("", f"{azul}Descriptografando...{resetar}")

        # Atualizar Chave Descriptografada no BD
        # Conectando no BD e iniciando o Cursor
        conn = sqlite3.connect("./sqlite/keys_app.db")
        cursor = conn.cursor()
        # Pegar Chave Descriptografada Atualizada
        cursor.execute("SELECT chave_cript FROM users WHERE id = (?)", (id_request,))
        item = cursor.fetchone()[0]
        cursor.execute("SELECT beta FROM users_data WHERE id = (?)", (id_request,))
        beta = cursor.fetchone()[0]
        # Gravando os dados e encerrando a conexão com o BD
        conn.commit()
        conn.close()

        for k in range(1, 6):
            if item[int(k-1):int(k+1)] == "20":
                item = item.replace("20", "t")
                    
            elif item[int(k-1):int(k)] == "5":
                item = item.replace("5", "e")
                    
            elif item[int(k-1):int(k)] == "1":
                item = item.replace("1", "a")
            
        item = item.replace("2", "b")
        item = item.replace("900", "_")

        for i in range(5, len(item)):
            if item[int(i)] == "w":
                item = item.replace("w", "8")
            elif item[int(i)] == "x":
                item = item.replace("x", "0")
            elif item[int(i)] == "f":
                item = item.replace("f", "7")
            elif item[int(i)] == "u":
                item = item.replace("u", "2")
            elif item[int(i)] == "l":
                item = item.replace("l", "1")
            elif item[int(i)] == "g":
                item = item.replace("g", "5")

        if item == beta:
            confirmacao_descriptografada = True

            sms = open("sms.txt", "w")
            sms.writelines(item)
            sms.close()

            print(f"{azul}={resetar}"*50)
            print(f"{verde}{'DESCRIPTOGRAFIA BEM-SUCEDIDA!':^50}{resetar}")
            print(f"{azul}={resetar}"*50)
            print(f"{amarelo}{'Sua chave descriptografada foi enviada':^50}{resetar}")
            print(f"{amarelo}{'por SMS para seu celular.':^50}{resetar}")
            print(f"{azul}{'(Você precisará dela para acessar o aplicativo.)':^50}{resetar}")
            print(f"{azul}={resetar}"*50)

        else:
            print("", f"{vermelho}={resetar}"*65, "\n", " "*16, f"{vermelho}DESCRIPTOGRAFIA MAL-SUCEDIDA!{resetar}", "\n", f"{vermelho}={resetar}"*65)


    def criptografar_arquivos(key, caminho):
        print(f"\n{azul}Buscando por arquivos...{resetar}")
        arquivos_pasta.clear()
        for diretorio, subpastas, arquivos in os.walk(caminho):
            for arquivo in arquivos:
                print(f"{amarelo}{os.path.join(arquivo)}{resetar}")
                arquivos_pasta.append(os.path.join(arquivo))
        
        for arq in arquivos_pasta:
            with open(f"{caminho}\\{arq}", "rb") as f:
                file = f.read()
                f.close()

                # Utilizando Algorítmo Padrão de Criptografia Avançado (AES) na Chave
                aes = pyaes.AESModeOfOperationCTR(key)

                # Criptografando o arquivo
                crypt_data = aes.encrypt(file)

                # Informando Usuário
                print(f"{azul}Arquivo {amarelo}{arq} {azul}criptografado com sucesso.{resetar}")

                # Salvando arquivo criptografado

                crypt_file = f'{caminho}\\{arq}' + '.wko'
                crypt_file = open(crypt_file, 'wb')
                crypt_file.write(crypt_data)
                crypt_file.close()

                os.remove(f'{caminho}\\{arq}')


    def descriptografar_arquivos(key, caminho):
        os.chdir(caminho)
        for file in glob.glob('*.wko'):
            name_file = open(file, 'rb')
            file_data = name_file.read()
            name_file.close()

            descrypt_aes = pyaes.AESModeOfOperationCTR(key)
            descrypt_data = descrypt_aes.decrypt(file_data)
            descrypt_file_name = file.replace('.wko', '')

            new_file = open(f'{caminho}\\{descrypt_file_name}', 'wb')
            new_file.write(descrypt_data)
            new_file.close()

            print(f"{azul}Arquivo {amarelo}{descrypt_file_name} {azul}descriptografado com sucesso.{resetar}")

            os.remove(f'{caminho}\\{file}')


class Gerador():
    def gerar_dados(nome, email, telefone, caminho_seguro, unidade_usb):
        Importacao.importar_listas()
        
        print("="*40)
        Gerador.gerador_id()
        # print(f"{verde}ID gerado com sucesso.{resetar}")
        Gerador.gerador_hashes()
        # print(f"{verde}Chaves geradas com sucesso.{resetar}")
        Criptografia.criptografia_hash()
        # print(f"{verde}Chave criptografada com sucesso.{resetar}")
        Gerador.gerador_chave_autenticacao()
        # print(f"{verde}Chave de autenticação gerada com sucesso.{resetar}")
        Gerador.gerar_chave_cript()
        # print(f"{verde}Chave de criptografia gerada com sucesso.{resetar}")

        Exportacao.exportar_bd(id_usuario[len(id_usuario)-1], nome, email, telefone, hash_betas_cripto[len(hash_betas_cripto)-1], chave_autenticacao[len(chave_autenticacao)-1])
        # print(f"{verde}Dados exportados ao banco de dados com sucesso.{resetar}")
        Exportacao.exportar_bd_2(id_usuario[len(id_usuario)-1], hash_betas[len(hash_betas)-1], hash_betas_cripto[len(hash_betas_cripto)-1], hash_alphas[len(hash_alphas)-1], caminho_seguro, unidade_usb, chave_cript[len(chave_cript)-1])
        # print(f"{verde}Dados exportados ao segundo banco de dados com sucesso.{resetar}")

        Importacao.importar_listas()

        Email.enviar_email(nome, email)
        # print(f"{verde}Email enviado com sucesso.{resetar}")

        print("="*50)
        print(f"{verde}{'Você foi cadastrado com sucesso!':^50}{resetar}")
        print("="*50)
        print(f"{azul}Seu ID é:{resetar} {amarelo}{id_usuario[len(id_usuario)-1]}{resetar}")
        print(f"{vermelho}(NÃO PERCA SEU ID){resetar}")
        print("="*50)
        print(f"{amarelo}{'Sua chave foi enviada para o seu email.':^50}{resetar}")
        print("="*50)
        input(f"{azul}{'-=- Aperte ENTER para continuar -=-':^50}{resetar}")
        print("="*50) 


    def gerador_id():
        id = 'ID01'
        while id in id_usuario:
            chars = ascii_uppercase + digits
            os.urandom(1024)
            id = ''.join(choice(chars) for i in range(4))

        id_usuario.append(id)


    def gerador_hashes():
        word_alpha = "alpha"
        word_beta = "beta"

        os.urandom(2048)

        alpha = "".join(sample(word_alpha, len(word_alpha))) + "_" + \
            str(randint(1000000000000000, 9999999999999999))
        beta = "".join(sample(word_beta, len(word_beta))) + "_" + \
            str(randint(1000000000000000, 9999999999999999))

        hash_alphas.append(alpha)
        hash_betas.append(beta)
        hash_betas_cripto.append(beta)


    def gerador_chave_autenticacao():
        chars = ascii_letters + digits
        os.urandom(2048)

        key = ''.join(choice(chars) for i in range(randint(16, 20)))

        chave_autenticacao.append(key)


    def gerar_chave_cript():
        # Gerando Chave pra Criptografar
        chars = digits + ascii_lowercase
        crypt_key = ''.join(choice(chars) for c in range(24)).encode('utf-8')

        chave_cript.append(crypt_key)


    def regerar():
        # Conectando no BD e iniciando o Cursor
        conn = sqlite3.connect("./sqlite/keys_app.db")
        cursor = conn.cursor()
        # Deletando chaves no BD 
        cursor.execute("UPDATE users_data SET alpha = '-' WHERE id = (?)", (id_request,))
        cursor.execute("UPDATE users_data SET beta = '-' WHERE id = (?)", (id_request,))
        cursor.execute("UPDATE users SET chave_cript = '-' WHERE id = (?)", (id_request,))
        cursor.execute("UPDATE users_data SET beta_cript = '-' WHERE id = (?)", (id_request,))

        word_alpha = "alpha"
        word_beta = "beta"

        alpha = "".join(sample(word_alpha, len(word_alpha))) + "_" + str(randint(1000000000000000, 9999999999999999))
        beta = "".join(sample(word_beta, len(word_beta))) + "_" + str(randint(1000000000000000, 9999999999999999))

        # Inserindo chaves no BD 
        cursor.execute("UPDATE users_data SET alpha = (?) WHERE id = (?)", (alpha, id_request))
        cursor.execute("UPDATE users_data SET beta = (?) WHERE id = (?)", (beta, id_request))
        #--------------------
        hash_betas_cripto.append(beta)
        Criptografia.criptografia_hash()
        #--------------------
        cursor.execute("UPDATE users SET chave_cript = (?) WHERE id = (?)", (hash_betas_cripto[len(hash_betas_cripto)-1], id_request))
        cursor.execute("UPDATE users_data SET beta_cript = (?) WHERE id = (?)", (hash_betas_cripto[len(hash_betas_cripto)-1], id_request))
        # Gravando os dados e encerrando a conexão com o BD
        conn.commit()
        conn.close()


class Email():
    def enviar_email(nome, email):
        # Iniciando servidor SMTP
        server = smtplib.SMTP(host, port)
        server.ehlo()
        server.starttls()
        server.login(login, senha)

        # Corpo do Email
        corpo = f"Olá, {nome}!<br>Sua chave é: <b>{hash_betas_cripto[email_usuario.index(email)]}</b>"

        # Montando o email
        email_msg = MIMEMultipart()
        email_msg['From'] = login
        email_msg['To'] = email
        email_msg['Subject'] = "WKO - Secure File - Senha de Acesso"
        email_msg.attach(MIMEText(corpo, 'html'))

        # 3- Enviar o email tipo mime no servidor SMTP
        server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
        server.quit()


    def reenviar():
        Verificacao.verificar_usuario()
        
        if id_request != "":
            Importacao.importar_listas()
            Email.enviar_email(nome_usuario[id_usuario.index(id_request)], email_usuario[id_usuario.index(id_request)])
            print("-"*50)
            print(f"{azul}{'Sua chave foi reenviada para o seu email.':^50}{resetar}")
            print("-"*50)


class Importacao():
    def importar_listas():
        while True:
            try:
                # -----------------------------------------------------
                # Conectando no BD e iniciando o Cursor
                conn = sqlite3.connect("./sqlite/keys_app.db")
                cursor = conn.cursor()
                # Importando dados às listas
                id_usuario.clear()

                cursor.execute("SELECT id FROM users")

                ids = cursor.fetchall()
                for i in ids:
                    id_usuario.append(i[0])

                # print(id_usuario)

                nome_usuario.clear()
                cursor.execute("SELECT nome FROM users")
                nomes = cursor.fetchall()
                for n in nomes:
                    nome_usuario.append(n[0])

                # print(nome_usuario)

                email_usuario.clear()
                cursor.execute("SELECT email FROM users")
                emails = cursor.fetchall()
                for e in emails:
                    email_usuario.append(e[0])

                # print(email_usuario)

                telefone_usuario.clear()
                cursor.execute("SELECT telefone FROM users")
                telefones = cursor.fetchall()
                for t in telefones:
                    telefone_usuario.append(t[0])

                # print(telefone_usuario)

                hash_betas_cripto.clear()
                cursor.execute("SELECT beta_cript FROM users_data")
                betas_cript = cursor.fetchall()
                for bc in betas_cript:
                    hash_betas_cripto.append(bc[0])

                # print(hash_betas_cripto)

                chave_autenticacao.clear()
                cursor.execute("SELECT chave_autent FROM users")
                autents = cursor.fetchall()
                for item in autents:
                    chave_autenticacao.append(item[0])

                # print(chave_autenticacao)

                hash_betas.clear()
                cursor.execute("SELECT beta FROM users_data")
                betas = cursor.fetchall()
                for item in betas:
                    hash_betas.append(item[0])

                # print(hash_betas)

                hash_alphas.clear()
                cursor.execute("SELECT alpha FROM users_data")
                alphas = cursor.fetchall()
                for item in alphas:
                    hash_alphas.append(item[0])
                
                # print(hash_alphas)
                
                caminho_seguro.clear()
                cursor.execute("SELECT secure_path FROM users_data")
                paths = cursor.fetchall()
                for item in paths:
                    caminho_seguro.append(item[0])
                
                # print(caminho_seguro)

                unidade_usb.clear()
                cursor.execute("SELECT unity_usb FROM users_data")
                unities = cursor.fetchall()
                for item in unities:
                    unidade_usb.append(item[0])
                
                # print(unidade_usb)

                chave_cript.clear()
                cursor.execute("SELECT crypt_key FROM users_data")
                chaves = cursor.fetchall()
                for item in chaves:
                    chave_cript.append(item[0])
                
                # print(chave_cript)

                # -----------------------------------------------------
                # Gravando os dados e encerrando a conexão com o BD
                conn.commit()
                conn.close()
            except sqlite3.OperationalError:
                db_function()
            else:
                break

class Exportacao():
    def exportar_bd(id, nome, email, telefone, cript, autent):
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
            (id, nome, email, telefone, cript, autent)
            ]

        cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)", (user))

        # Gravando os dados e encerrando a conexão com o BD
        conn.commit()
        conn.close()

    def exportar_bd_2(id, beta, beta_cript, alpha, caminho_seguro, unidade_usb, chave_cript):
        # Conectando no BD e iniciando o Cursor
        conn = sqlite3.connect("./sqlite/keys_app.db")
        cursor = conn.cursor()
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
            (id, beta, beta_cript, alpha, caminho_seguro, unidade_usb, chave_cript)
            ]

        cursor.executemany("INSERT INTO users_data VALUES (?, ?, ?, ?, ?, ?, ?)", (user_data))

        # Gravando os dados e encerrando a conexão com o BD
        conn.commit()
        conn.close()


# Execução do Programa

Validacao.validarMenu()