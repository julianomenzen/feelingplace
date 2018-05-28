from databaseService import *

class instagramRepository(object):
    """description of class"""
    def inserir(self, model):
        comando = "insert into tags (latitude, longitude, cnpj, tag ) " 
        comando = comando + " values('%s','%s','%s','%s');" % (model.latitude, model.longitude, model.cnpj, model.tag )
        executarComando(comando)

    def atualizarSentimento(self, model):
        comando = "update tags set sentimento = %s where id = %s"  % (model.emocao, model.id )
        executarComando(comando)

    def consultarTudo(self):
        linhas = SelecionarRegistros("select id, latitude, longitude, cnpj, tag, sentimento  from tags ")

        arr = []
        for linha in linhas:
            inst = instragram(linha[1], linha[2], linha[3], linha[4])
            inst.id = linha[0]
            inst.sentimento =  linha[5]
            arr.append(inst)

        return arr


