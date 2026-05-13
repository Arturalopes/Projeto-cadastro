from conn import Conectar

def NovoImigrante():
    print("******************************")
    print(" Cadastrar Imigrante ")
    print("******************************")
    print("")

    #solicitando dados do imigrante
    nome = input("Informe o nome: ")
    nacionalidade = input("Informe a nacionalidade: ")
    dataNascimento = input("Informe a data de nascimento: ")
    documento = input("Informe o documento: ")

    #criando a conexão
    conn = Conectar()
    cursor = conn.cursor()

    # enviar o comando para o banco de dados
    cursor.execute("INSERT INTO IMIGRANTE (NOME, NACIONALIDADE, DT_NASCIMENTO, DOCUMENTO)VALUES(%s, %s, %s, %s)",
                   (nome, nacionalidade, dataNascimento, documento,))
    conn.commit()

    print("")
    print("Imigrante cadastrado com sucesso")
    #esse comando é para parar a execução do programa até pressionar enter
    input("Pressione enter para continuar!")

    #fechando as conexoes
    cursor.close()
    conn.close()


def ListarTodosImigrantes():
    print("******************************")
    print(" Lista de Imigrantes ")
    print("******************************")
    print("")

    #criando a conexao
    conn = Conectar()
    cursor = conn.cursor()

    #enviando o camando para o banco de dados
    cursor.execute("SELECT IDIMIGRANTE, NOME, NACIONALIDADE, DT_NASCIMENTO, DOCUMENTO FROM IMIGRANTE")

    #percorrendo o resultado e mostrando em tela
    for id, nome, nacionalidade, dt_nascimento, documento in cursor.fetchall():
        print(f"{id} - {nome} - {nacionalidade} - {dt_nascimento} - {documento}")

    #fechando a conexao
    cursor.close()
    conn.close()

def DetalheImigrante(id):
    print("******************************")
    print(" Detalhe de Imigrantes ")
    print("******************************")
    print("")

    # criando conexão com o banco de dados
    conn = Conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT IDIMIGRANTE, NOME, NACIONALIDADE, DT_NASCIMENTO, DOCUMENTO FROM IMIGRANTE WHERE IDIMIGRANTE = %s", (id,))
    for id, nome, nacionalidade, dt_nascimento, documento in cursor.fetchall():
        print(f"Id: {id}")
        print(f"Nome: {nome}")
        print(f"Nacionalidade: {nacionalidade}")
        print(f"Dt. nascimento: {dt_nascimento}")
        print(f"Documento: {documento}")
        print("")

    cursor.close()
    conn.close()

def AlterarImigrante(id):
    print("******************************")
    print(" Alterando o Imigrante ")
    print("******************************")
    print("")

    print("Informe os novos valores do imigrante:")
    nome = input("Informe o nome: ")
    nacionalidade = input("Informe a nacionalidade: ")
    dt_nascimento = input("Informe a data de nascimento: ")
    documento = input("Informe o documento: ")

    #criando conexao com o banco de dados
    conn = Conectar()
    cursor = conn.cursor()

    # enviando comando sql para alterar o imigrante
    cursor.execute("UPDATE IMIGRANTE SET NOME = %s, NACIONALIDADE = %s, DT_NASCIMENTO = %s, DOCUMENTO = %s WHERE IDIMIGRANTE = %s"
                   , (nome, nacionalidade, dt_nascimento, documento, id))
    conn.commit()

    cursor.close()
    conn.close()

    print("Imigrante atualizado com sucesso!")
    input("pressione enter para voltar ao menu")

def ExcluirImigrante(id):
    print("******************************")
    print(" Excluir o Imigrante ")
    print("******************************")
    print("")

    confirmar = input("Deseja realmente excluir o imigrante (informe 1 para confirmar):")
    if(confirmar == '1'):
        #criando conexao com o banco de dados
        conn = Conectar()
        cursor = conn.cursor()
        # enviando comando sql para excluir a informação
        cursor.execute("DELETE FROM INFORMACAO WHERE IDIMIGRANTE = %s",(id,))
        # enviando comando sql para excluir o imigrante
        cursor.execute("DELETE FROM IMIGRANTE WHERE IDIMIGRANTE = %s",(id,))
        conn.commit()

        cursor.close()
        conn.close()

        print("Imigrante atualizado com sucesso!")
    else:
        print("Operação cancelada!")
    input("pressione enter para voltar ao menu")
