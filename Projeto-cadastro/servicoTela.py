import os
from servico import NovoServico, ListarTodosServicos, DetalheServico, AlterarServico, ExcluirServico, ListarServicosTipo

def LimpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def MenuServico():
    while True:
        # limpando a tela 
        LimpaTela()

        # criando o menu servico
        print(" === Menu Serviço === ")
        print("1. Cadastrar serviço ")
        print("2. Listar serviço ")
        print("3. Ver detalhe do serviço")
        print("4. Alterar serviço")
        print("5. Excluir serviço")
        print("6. Buscar servico por tipo")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            # chamando o metodo para cadastrar novo servico
            NovoServico()
        elif opcao == '2':
            # chamando o metodo para listar todos os servicos
            ListarTodosServicos()
            input("Pressione enter para continuar!")
        elif opcao == '3':
            # chamando o metodo que lista todos os servico para que o usuario escolha um
            ListarTodosServicos()
            print("")
            id = input("Informe o ID do serviço para ver detalhes: ")

            LimpaTela()
            # chamando o metodo para ver detalhes do imigrante
            DetalheServico(id)
        elif opcao == '4':
            #chamando o metodo para listar todos os servicos para escolher um
            ListarTodosServicos()
            print("")
            id = input("Informe o Id do servico para alterar: ")
            #chamando o metodo para alterar o imigrante
            AlterarServico(id)

        elif opcao == '5':
            #chamando o metodo para listar todos os servicos para escolher um
            ListarTodosServicos()
            print("")
            id = input("Informe o Id do servico para excluir: ")
            #chamando o metodo para excluir o servico
            ExcluirServico(id)
        elif opcao == '6':
            #chamando o metodo para listar todos os servicos para escolher um
            ListarServicosTipo()
            input("Pressione enter para continuar!")
        elif opcao == '9':
            break
        else:
            print("Opção inválida")
