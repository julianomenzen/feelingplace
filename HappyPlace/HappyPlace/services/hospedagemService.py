from pathlib import Path
from progressoService import *
from estabelecimentoHospedagem import *
from hospesagemRepository import *
from correiosWebService import *
from googleMapsWebService import * 
from funcoesString import *
from threading import Thread
class hospedagemService(object):
    """description of class"""
    def buscarCidadeLatLong(self, service_correios, hospesagemLinha, tokens):
        cidade = service_correios.buscar_cidade_por_cep(funcoesString.somenteNumeros(hospesagemLinha.cep))
        if (cidade.strip() != ''):
            hospesagemLinha.localidade = cidade
                    
        local = googleMapsWebService.retornarLatitudeLongitude(hospesagemLinha.logradouro, hospesagemLinha.bairro, hospesagemLinha.localidade, hospesagemLinha.uf, tokens)
        if (local != ""):
            hospesagemLinha.latitude = local['lat']
            hospesagemLinha.longitude = local['lng']

    def processarArquivo(self, caminho, tokens):
        service_correios = correiosWebService()
        repositorio = hospesagemRepository()
        i = 0
        hospedagens = Path(caminho)
        #verifica se o arquivo existe
        if (not hospedagens.exists()):
            print("O arquivo " + caminho + " nao foi encontrado") 
        else:
            #identifica quantos registros o arquivo possuir
            with open(caminho) as f:
                content = f.read().splitlines()
            
            threads = []
            for linha in content:
                #Controla numero de threads pra não virar uma zona
                if (len(threads) > 10):
                    for x in threads:
                        x.join()
                    threads = []

                linha = str.replace(linha, "'", " ")
                if (i == 0):
                    i = i + 1
                    continue
                x = str.split(linha,';')
                if (x[0] != ""):
                    if (len(x) < 30):
                        j = len(x)
                        while j < 30:
                            j = j + 1
                            x.append("")
       
                    hospesagemLinha = hospedagem(x[0],x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17], x[18], x[19], x[20], x[21], x[22], x[23], x[24], x[25], x[26], x[27], x[28], x[29])
                    if (not repositorio.validaExistePorCNPJ(hospesagemLinha.cnpj)):
                        t = Thread(target=self.salvarHospedagem,args=[service_correios, hospesagemLinha, i, content, repositorio, tokens])
                        t.start()
                        threads.append(t)
                    #self.salvarHospedagem(service_correios, hospesagemLinha, i, content)
                    
                i = i + 1

    def salvarHospedagem(self, service_correios, hospesagemLinha, i, content, repositorio, tokens, ):
        #Será que vai dar desempenho? Me pareceu que sim!
        self.buscarCidadeLatLong(service_correios, hospesagemLinha, tokens)
        repositorio.inserir(hospesagemLinha)
        atualizarProgresso("Hospedagens", i, len(content))

    def selecionarHospedagens():
        repositorio = hospesagemRepository()
        return repositorio.consultarTudo()