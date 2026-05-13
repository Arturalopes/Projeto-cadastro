import os
from imigrante import NovoImigrante, ListarTodosImigrantes, DetalheImigrante, AlterarImigrante, ExcluirImigrante
from informacaoTela import MenuInformacao

def LimpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def MenuImigrante():
    while True:
        # limpando a tela 
        LimpaTela()

        # criando o menu imigrante
        print("+-----------------------------+")
        print("| Menu Imigrante              |")
        print("+-----------------------------+")
        print("| 1. Cadastrar imigrante      |")
        print("| 2. Listar imigrante         |")
        print("| 3. Ver detalhe do imigrante |")
        print("| 4. Alterar imigrante        |")
        print("| 5. Excluir imigrante        |")
        print("|                             |")
        print("| 9. Sair                     |")
        print("+-----------------------------+")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            # chamando o metodo para cadastrar novo imigrante            
            NovoImigrante()
        elif opcao == '2':
            # chamando o metodo para listar todos os imigrantes
            ListarTodosImigrantes()
            input("Pressione enter para continuar!")
        elif opcao == '3':
            # chamando o metodo que lista todos os imigrante para que o usuario escolha um
            ListarTodosImigrantes()
            print("")
            id = input("Informe o ID do imigrante para ver detalhes: ")
            # chamando o metodo para ver detalhes do imigrante
            MenuInformacao(id)
        elif opcao == '4':
            #chamando o metodo para listar todos os imigrantes para escolher um
            ListarTodosImigrantes()
            print("")
            id = input("Informe o Id do imigrante para alterar: ")
            #chamando o metodo para alterar o imigrante
            AlterarImigrante(id)

        elif opcao == '5':
            #chamando o metodo para listar todos os imigrantes para escolher um
            ListarTodosImigrantes()
            print("")
            id = input("Informe o Id do imigrante para excluir: ")
            #chamando o metodo para excluir o imigrante
            ExcluirImigrante(id)
        elif opcao == '9':
            break
        else:
            print("Opção inválida")
