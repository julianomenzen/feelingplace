from databaseService import *

class servicosEspecializadosRepository(object):
    """description of class"""
    def inserir(self, model):
        comando = "insert into especializados (razaosocial , nomefantasia ,cnpj , natureza ,datainicio , porte , situacao , tipoatividade , subtipo , cep , uf , localidade , bairro , logradouro , telefone , fax , email2 , email3 , site , certificado , codigodescricaocnae , servicos , segmento ,linguas) " 
        comando = comando + " values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (model.razaosocial , model.nomefantasia ,model.cnpj , model.natureza ,model.datainicio , model.porte , model.situacao , model.tipoatividade , model.subtipo , model.cep , model.uf , model.localidade , model.bairro , model.logradouro , model.telefone , model.fax , model.email2 , model.email3 , model.site , model.certificado , model.codigodescricaocnae , model.servicos , model.segmento ,model.linguas)
        executarComando(comando)