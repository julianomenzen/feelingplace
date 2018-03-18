from databaseService import *

class municipioRepository(object):
    """description of class"""

    def inserir(self, model):
        comando = "insert into municipio (uf, regiao, municipio, categoria) values('%s','%s','%s','%s');" % (model.uf, model.regiao, model.municipio, model.categoria)
        executarComando(comando)
