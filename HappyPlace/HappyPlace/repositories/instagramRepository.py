from databaseService import *

class instagramRepository(object):
    """description of class"""
    def inserir(self, model):
        comando = "insert into tags (latitude, longitude, cnpj, tag ) " 
        comando = comando + " values('%s','%s','%s','%s','%s');" % (model.latitude, model.longitude, model.cnpj, model.tag )
        executarComando(comando)


