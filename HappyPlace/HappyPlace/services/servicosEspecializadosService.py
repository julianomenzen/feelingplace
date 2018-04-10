from pathlib import Path
from progressoService import *
from estabelecimentoEspecializado import *
from servicosEspecializadosRepository import *
from correiosWebService import *
from googleMapsWebService import * 
from funcoesString import *

class servicosEspecialiadosService(object):
    """description of class"""
    
    def buscarCidadeLatLong(self, service_correios, estabelecimentoLinha, tokens):
        cidade = service_correios.buscar_cidade_por_cep(funcoesString.somenteNumeros(estabelecimentoLinha.cep))
        if (cidade.strip() != ''):
            estabelecimentoLinha.localidade = cidade
                    
        local = googleMapsWebService.retornarLatitudeLongitude(estabelecimentoLinha.logradouro, estabelecimentoLinha.bairro, estabelecimentoLinha.localidade, estabelecimentoLinha.uf, tokens)
        if (local != ""):
            estabelecimentoLinha.latitude = local['lat']
            estabelecimentoLinha.longitude = local['lng']

    def processarArquivo(self, caminho, tokens):
        service_correios = correiosWebService()
        repositorio = servicosEspecializadosRepository()
        i = 0
        estabelecimentos = Path(caminho)
        #verifica se o arquivo existe
        if (not estabelecimentos.exists()):
            print("O arquivo " + caminho + " nao foi encontrado") 
        else:
            #identifica quantos registros o arquivo possuir
            with open(caminho) as f:
                content = f.read().splitlines()

            for linha in content:
                linha = str.replace(linha, "'", " ")
                if (i == 0):
                    i = i + 1
                    continue
                x = str.split(linha,';')
                if (x[0] != ""):
                    if (len(x) < 23):
                        j = len(x)
                        while j < 23:
                            j = j + 1
                            x.append("")
                                        
                    estabelecimentoLinha = estabelecimentosEspecializados(x[0],x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17], x[18], x[19], x[20], x[21], x[22], x[22])
                    self.buscarCidadeLatLong(service_correios, estabelecimentoLinha, tokens)

                    repositorio.inserir(estabelecimentoLinha)
                    atualizarProgresso("Estabelecimentos Especializados", i, len(content))
                i = i + 1

    def selecionarEstabelecimentosEspecializados():
        repositorio = servicosEspecializadosRepository()
        return repositorio.consultarTudo()

    
        
