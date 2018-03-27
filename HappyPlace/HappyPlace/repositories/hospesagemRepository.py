from databaseService import *

class hospesagemRepository(object):
    """description of class"""
    def inserir(self, model):        
        comando = "insert into hospedagens (razaosocial, nomefantasia, cnpj, naturezajuridica, datainicio, porte, situacao, tipoatividade, subtipo, cep, uf, localidade, bairro, logradouro, telefone, fax, email2, email3, site, codigocertificado, codigodescricaocnae, uh, uhacessiveis, uhscaoguia, uhstps, totalleitos, linguas, segmentos, servicos, equipamentos, latitude, longitude) " 
        comando = comando + " values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (model.razaosocial, model.nomefantasia, model.cnpj, model.naturezajuridica, model.datainicio, model.porte, model.situacao, model.tipoatividade, model.subtipo, model.cep, model.uf, model.localidade, model.bairro, model.logradouro, model.telefone, model.fax, model.email2, model.email3, model.site, model.codigocertificado, model.codigodescricaocnae, model.uh, model.uhacessiveis, model.uhscaoguia, model.uhstps, model.totalleitos, model.linguas, model.segmentos, model.servicos, model.equipamentos, model.latitude, model.longitude)
        executarComando(comando)

    def validaExistePorCNPJ(self, cnpj):
        return RegistroExite("SELECT cnpj FROM hospedagens WHERE cnpj = '{0}'".format(cnpj))

