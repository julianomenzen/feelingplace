import os
from tokensGoogle import tokensGoogle
from databaseService import *
from municipioService import *
from hospedagemService import *
from restauranteService import *

from servicosEspecializadosService import *

def criarEstruturaTabelas():
    print("Criando tabelas...")
    criarTabelaMunicipio()
    criarTabelaHospedagens()
    criarTabelaRestaurantes()
    criarTabelaEspabelecimentosEspecializados()
    criarTabelaTags()
    print("Tabelas criadas....")
    print("Pressione qualquer tecla para continuar....")
    input()

def importarEnderecos():
    os.system('cls||clear')
    servicoMunicipio = municipioService()
    servicoMunicipio.processarArquivo("csv\\municipios.csv");

def importarHospedagens(tokens):
    os.system('cls||clear')
    servicoHospesagem = hospedagemService()
    servicoHospesagem.processarArquivo("csv\\hospedagem.csv", tokens);

def importarRestaurantes(tokens):
    os.system('cls||clear')
    servicoRestaurante = restauranteService()
    servicoRestaurante.processarArquivo("csv\\restaurantes.csv", tokens);

def importarEstabelecimentosEspecializados(tokens):
    os.system('cls||clear')
    servicoEspecializado = servicosEspecialiadosService()
    servicoEspecializado.processarArquivo("csv\\especializados.csv", tokens);


def processarMenu(opcao):
    tokens = tokensGoogle()
    
    if (opcao == '1'):
        criarEstruturaTabelas()
    elif (opcao == '2'):
        importarEnderecos()
    elif (opcao == '3'):
        importarHospedagens(tokens)
    elif (opcao == '4'):
        importarRestaurantes(tokens)
    elif (opcao == '5'):
        importarEstabelecimentosEspecializados(tokens)
    elif (opcao == '5'):
        importarEstabelecimentosEspecializados(tokens)
    elif (opcao == '7'):
        importarEnderecos()
        importarHospedagens(tokens)
        importarRestaurantes(tokens)
        importarEstabelecimentosEspecializados(tokens)
        #teste


def menu():
	nomes=[]
	escolha = ''
	while (escolha != '0'):
            os.system('cls||clear')
            print("Escolha uma opção:\n")
            print("1 - Criar estrutura de tabelas\n2 - Importar Endereços\n3 - Importar Hospedagens\n4 - Importar Restaurantes\n5 - Importar Estabelecimentos Especializados\n6 - Importar dados do Instagram\n7 - Importar tudo \n\n0 - Sair")
            escolha = input()
            processarMenu(escolha)
			
menu()