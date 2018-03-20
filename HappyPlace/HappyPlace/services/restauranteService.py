from pathlib import Path
from progressoService import *
from estabelecimentoAlimenticio import *
from restauranteRepository import *

class restauranteService(object):
    """description of class"""

    def processarArquivo(self, caminho):
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

                    restauranteLinha = estabelecimentosAlimenticios(x[0],x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17], x[18], x[19], x[20], x[21], x[22])
                    repositorio.inserir(restauranteLinha)
                    atualizarProgresso("Restaurantes", i, len(content))
                i = i + 1