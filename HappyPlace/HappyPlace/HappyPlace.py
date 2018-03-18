import os

from databaseService import *


stringconexao = ""

def criarEstruturaTabelas():
    print("Criando tabelas...")
    criarTabelaMunicipio()
    print("Tabelas criadas....")
    print("Pressione qualquer tecla para continuar....")
    input()

def importarMunicipios():
    print("Opcao 2 escolhida....")

def processarMenu(opcao):
    if (opcao == '1'):
        criarEstruturaTabelas()
    elif (opcao == '2'):
        importarMunicipios()

def menu():
	nomes=[]
	escolha = ''
	while (escolha != '0'):
            os.system('cls||clear')
            print("Escolha uma opção:\n")
            print("1 - Criar estrutura de tabelas\n2 - Importar Municipio \n\n0 - Sair")
            escolha = input()
            processarMenu(escolha)
			
menu()
