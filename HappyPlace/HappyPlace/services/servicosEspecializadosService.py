from pathlib import Path
from progressoService import *
from estabelecimentoEspecializado import *
from servicosEspecializadosRepository import *

class servicosEspecialiadosService(object):
    """description of class"""
    def processarArquivo(self, caminho):
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
                if (i == 0):
                    i = i + 1
                    continue
                x = str.split(linha,';')
                if (x[0] != ""):
                    estabelecimentoLinha = estabelecimentosEspecializados(x[0],x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17], x[18], x[19], x[20], x[21], x[22], x[22])
                    repositorio.inserir(estabelecimentoLinha)
                    atualizarProgresso("Estabelecimentos Especializados", i, len(content))
                i = i + 1