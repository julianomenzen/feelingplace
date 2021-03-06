from pathlib import Path
from progressoService import *
from estabelecimentoAlimenticio import *
from restauranteRepository import *
from correiosWebService import *
from googleMapsWebService import * 
from funcoesString import *
class restauranteService(object):
    """description of class"""
    def buscarCidadeLatLong(self, service_correios, restauranteLinha, tokens):
        cidade = service_correios.buscar_cidade_por_cep(funcoesString.somenteNumeros(restauranteLinha.cep))
        if (cidade.strip() != ''):
            restauranteLinha.localidade = cidade
                    
        local = googleMapsWebService.retornarLatitudeLongitude(restauranteLinha.logradouro, restauranteLinha.bairro, restauranteLinha.localidade, restauranteLinha.uf, tokens)
        if (local != ""):
            restauranteLinha.latitude = local['lat']
            restauranteLinha.longitude = local['lng']

    def processarArquivo(self, caminho, tokens):
        service_correios = correiosWebService()
        repositorio = restauranteRepository()
        i = 0
        restaurantes = Path(caminho)
        #verifica se o arquivo existe
        if (not restaurantes.exists()):
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

                    restauranteLinha = estabelecimentosAlimenticios(x[0],x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17], x[18], x[19], x[20], x[21], x[22], 0, 0)
                    self.buscarCidadeLatLong(service_correios, restauranteLinha, tokens)
                    repositorio.inserir(restauranteLinha)
                    atualizarProgresso("Restaurantes", i, len(content))
                i = i + 1

    def selecionarRestaurantes(self):
        repositorio = restauranteRepository()
        return repositorio.consultarTudo()