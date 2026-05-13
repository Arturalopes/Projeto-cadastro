import os
from imigranteTela import MenuImigrante
from servicoTela import MenuServico

def LimpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def Menu():
    while True:
        # limpando a tela 
        LimpaTela()

        # criando o menu principal
        print("+---------------------------+")
        print("| Menu principal            |")
        print("+---------------------------+")
        print("| 1. Imigrante              |")
        print("| 2. Servico Apoio          |")
        print("|                           |")
        print("| 9. Sair                   |")
        print("+---------------------------+")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            MenuImigrante()
        elif opcao == '2':
            MenuServico()
        elif opcao == '9':
            print("Obrigado por utilizar esse app")
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    Menu()