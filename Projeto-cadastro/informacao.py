from conn import Conectar

def NovaInformacao(idImigrante):
    print(" === Nova informacao complementar === ")
    print("")

    tipo = input("Informe o tipo de Informacao Complementar: ")
    descricao = input("Informe a descricao: ")
    ano_inicio = input("Informe o ano inicial: ")
    ano_fim = input("Informe o ano final: ")

    #criando a conexao
    conn = Conectar()
    cursor = conn.cursor()

    #enviando o comando para o banco de dados
    cursor.execute("INSERT INTO INFORMACAO (IDIMIGRANTE, TIPO, DESCRICAO, ANO_INICIO, ANO_TERMINO) VALUES (%s, %s, %s, %s, %s)",
                   (idImigrante, tipo, descricao, ano_inicio, ano_fim))

    conn.commit()

    # fechando a conexao
    cursor.close()
    conn.close()

    print("")
    print("Informacao salva com sucesso")
    input("Pressione enter para continuar")

def ListarInformacao(idImigrante):
    print("")
    print(" === Informações do Imigrante === ")
    print("")

    #conexao com banco de dados
    conn = Conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT IDINFORMACAO, TIPO, DESCRICAO, ANO_INICIO, ANO_TERMINO FROM INFORMACAO WHERE IDIMIGRANTE = %s ", (idImigrante, ))

    #percorre a lista de resulto do comando
    for id, tipo, descricao, ano_inicio, ano_termino in cursor.fetchall():
        print(f" {id} - {tipo} - {descricao} - {ano_inicio} - {ano_termino}")

    cursor.close()
    conn.close()

    print("")
    print("")

def AlterarInformacao():
    print("")
    print(" === Alterando Informações do Imigrante === ")
    print("")

    idInformacao = input("Selecione o id da informacao: ")
    tipo = input("Informe o tipo de Informacao Complementar: ")
    descricao = input("Informe a descricao: ")
    ano_inicio = input("Informe o ano inicial: ")
    ano_fim = input("Informe o ano final: ")

    conn = Conectar()
    cursor = conn.cursor()

    cursor.execute("UPDATE INFORMACAO SET TIPO = %s, DESCRICAO = %s, ANO_INICIO = %s, ANO_TERMINO = %s WHERE IDINFORMACAO = %s",
                   (tipo, descricao, ano_inicio, ano_fim, idInformacao))
    conn.commit()

    cursor.close()
    conn.close()

    print("Informação atualizada com sucesso")
    input("Pressione enter para continuar")

def ExcluirInformacao():
    print("")
    print(" === Excluindo Informações do Imigrante === ")
    print("")

    idInformacao = input("Selecione o id da informacao: ")

    conn = Conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM INFORMACAO WHERE IDINFORMACAO = %s",(idInformacao,))
    conn.commit()

    cursor.close()
    conn.close()

    print("Informação excluida com sucesso")
    input("Pressione enter para continuar")    