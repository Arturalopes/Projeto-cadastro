from conn import Conectar

def NovoServico():
    print("******************************")
    print(" Cadastrar Servico ")
    print("******************************")
    print("")

    #solicitando dados do Servico
    tipo = input("Informe o Tipo: ")
    nome = input("Informe a Nome: ")
    endereco = input("Informe a Endereço: ")
    telefone = input("Informe o Telefone: ")

    #criando a conexão
    conn = Conectar()
    cursor = conn.cursor()

    # enviar o comando para o banco de dados
    cursor.execute("INSERT INTO SERVICO_APOIO (TIPO, NOME, ENDERECO, TELEFONE)VALUES(%s, %s, %s, %s)",
                   (tipo, nome, endereco, telefone,))
    conn.commit()

    print("")
    print("Servico cadastrado com sucesso")
    #esse comando é para parar a execução do programa até pressionar enter
    input("Pressione enter para continuar!")

    #fechando as conexoes
    cursor.close()
    conn.close()


def ListarTodosServicos():
    print("******************************")
    print(" Lista de Servicos ")
    print("******************************")
    print("")

    #criando a conexao
    conn = Conectar()
    cursor = conn.cursor()

    #enviando o camando para o banco de dados
    cursor.execute("SELECT IDSERVICO_APOIO, TIPO, NOME, ENDERECO, TELEFONE FROM SERVICO_APOIO")

    #percorrendo o resultado e mostrando em tela
    for id, tipo, nome, endereco, telefone in cursor.fetchall():
        print(f"{id} - {tipo} - {nome} - {endereco} - {telefone}")

    #fechando a conexao
    cursor.close()
    conn.close()

def DetalheServico(id):
    print("******************************")
    print(" Detalhe de Serviço ")
    print("******************************")
    print("")

    # criando conexão com o banco de dados
    conn = Conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT IDSERVICO_APOIO, TIPO, NOME, ENDERECO, TELEFONE FROM SERVICO_APOIO WHERE IDSERVICO_APOIO = %s", (id,))
    for id, tipo, nome, endereco, telefone in cursor.fetchall():
        print(f"Id: {id}")
        print(f"Tipo: {tipo}")
        print(f"Nome: {nome}")
        print(f"Endereço: {endereco}")
        print(f"Telefone: {telefone}")
        print("")

    cursor.close()
    conn.close()

    input("pressione enter para voltar ao menu")

def AlterarServico(id):
    print("******************************")
    print(" Alterando o Servico ")
    print("******************************")
    print("")

    print("Informe os novos valores do serviço:")
    tipo = input("Informe o Tipo: ")
    nome = input("Informe a Nome: ")
    endereco = input("Informe a Endereço: ")
    telefone = input("Informe o Telefone: ")

    #criando conexao com o banco de dados
    conn = Conectar()
    cursor = conn.cursor()

    # enviando comando sql para alterar o servico
    cursor.execute("UPDATE SERVICO_APOIO SET TIPO = %s, NOME = %s, ENDERECO = %s, TELEFONE = %s WHERE IDSERVICO_APOIO = %s"
                   , (tipo, nome, endereco, telefone, id))
    conn.commit()

    cursor.close()
    conn.close()

    print("Servico atualizado com sucesso!")
    input("pressione enter para voltar ao menu")

def ExcluirServico(id):
    print("******************************")
    print(" Excluir o SErvico ")
    print("******************************")
    print("")

    confirmar = input("Deseja realmente excluir o servico (informe 1 para confirmar):")
    if(confirmar == '1'):
        #criando conexao com o banco de dados
        conn = Conectar()
        cursor = conn.cursor()

        # enviando comando sql para excluir o servico
        cursor.execute("DELETE FROM SERVICO_APOIO WHERE IDSERVICO_APOIO = %s",(id,))
        conn.commit()

        cursor.close()
        conn.close()

        print("Servico atualizado com sucesso!")
    else:
        print("Operação cancelada!")

    input("pressione enter para voltar ao menu")

def ListarServicosTipo():
    print("******************************")
    print(" Pesquisa de servico por tipo ")
    print("******************************")
    print("")

    tipo = input("Informe o tipo de servico (uma parte do texto): ")

    #criando a conexao
    conn = Conectar()
    cursor = conn.cursor()

    #enviando o camando para o banco de dados
    cursor.execute(f"SELECT IDSERVICO_APOIO, TIPO, NOME, ENDERECO, TELEFONE FROM SERVICO_APOIO WHERE UPPER(TIPO) LIKE UPPER('%{tipo}%')")

    #percorrendo o resultado e mostrando em tela
    for id, tipo, nome, endereco, telefone in cursor.fetchall():
        print(f"{id} - {tipo} - {nome} - {endereco} - {telefone}")

    #fechando a conexao
    cursor.close()
    conn.close()

