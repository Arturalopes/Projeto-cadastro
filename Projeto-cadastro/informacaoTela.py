import os
from informacao import NovaInformacao, ListarInformacao, AlterarInformacao, ExcluirInformacao
from imigrante import DetalheImigrante

def LimpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def MenuInformacao(idImigrante):

    while True:
        LimpaTela()

        #mostrando dados do imigrante
        DetalheImigrante(idImigrante)
        ListarInformacao(idImigrante)

        #criando o menu de informacao
        print(" === Informação Complementar do imigrante === ")
        print("1. Cadastrar informacao   2. Alterar informacao   3. Excluir informacao   9. Voltar")
        print("")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            # chamar o metodo de criar informacao complementar
            NovaInformacao(idImigrante)
        elif opcao == '2':
            # chamar o metodo de alterar informacao complementar
            AlterarInformacao()
        elif opcao == '3':
            # chamar o metodo de excluir informacao complementar
            ExcluirInformacao()
        elif opcao == '9':
            break
        else:
            print("opcao invalida")