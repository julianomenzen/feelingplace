from pathlib import Path
from progressoService import *
from municipio import *
from municipioRepository import *

class municipioService(object):
    """description of class"""

    def processarArquivo(self, caminho):
        repositorio = municipioRepository()
        i = 0
        municipios = Path(caminho)
        #verifica se o arquivo existe
        if (not municipios.exists()):
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
                    cidadeLinha = municipio(x[0],x[1], x[2], x[3])
                    repositorio.inserir(cidadeLinha)
                    atualizarProgresso("Cidades", i, len(content))
                i = i + 1
                

