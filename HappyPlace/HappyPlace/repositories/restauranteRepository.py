from databaseService import *

class restauranteRepository(object):
    """description of class"""
    def inserir(self, model):
        comando = "insert into restaurantes (razaosocial  ,nomefantasia  ,cnpj  ,naturezajuridica  ,datainicio  ,porte  ,situacao  ,tipoatividade  ,subtipo  ,cep  ,uf  ,localidade  ,bairro  ,logradouro  ,telefone  ,fax  ,email2  ,email3  ,site  ,codigocertificado  ,codigodescricaocnae  ,capacidade  , linguas ) " 
        comando = comando + " values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (model.razaosocial  ,model.nomefantasia  ,model.cnpj  ,model.naturezajuridica  ,model.datainicio  ,model.porte  ,model.situacao  ,model.tipoatividade  ,model.subtipo  ,model.cep  ,model.uf  ,model.localidade  ,model.bairro  ,model.logradouro  ,model.telefone  ,model.fax  ,model.email2  ,model.email3  ,model.site  ,model.codigocertificado  ,model.codigodescricaocnae  ,model.capacidade  , model.linguas )
        executarComando(comando)

