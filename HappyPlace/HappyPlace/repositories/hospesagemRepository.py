from databaseService import *
from estabelecimentoHospedagem import *

class hospesagemRepository(object):
    """description of class"""
    def inserir(self, model):        
        comando = "insert into hospedagens (razaosocial, nomefantasia, cnpj, naturezajuridica, datainicio, porte, situacao, tipoatividade, subtipo, cep, uf, localidade, bairro, logradouro, telefone, fax, email2, email3, site, codigocertificado, codigodescricaocnae, uh, uhacessiveis, uhscaoguia, uhstps, totalleitos, linguas, segmentos, servicos, equipamentos, latitude, longitude) " 
        comando = comando + " values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (model.razaosocial, model.nomefantasia, model.cnpj, model.naturezajuridica, model.datainicio, model.porte, model.situacao, model.tipoatividade, model.subtipo, model.cep, model.uf, model.localidade, model.bairro, model.logradouro, model.telefone, model.fax, model.email2, model.email3, model.site, model.codigocertificado, model.codigodescricaocnae, model.uh, model.uhacessiveis, model.uhscaoguia, model.uhstps, model.totalleitos, model.linguas, model.segmentos, model.servicos, model.equipamentos, model.latitude, model.longitude)
        executarComando(comando)

    def validaExistePorCNPJ(self, cnpj):
        return RegistroExite("SELECT cnpj FROM hospedagens WHERE cnpj = '{0}'".format(cnpj))

    def consultarTudo(self):
        linhas = SelecionarRegistros("select * from hospedagens ")

        arr = []
        for linha in linhas:
            arr.append(hospedagem(linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16], linha[17], linha[18], linha[19], linha[20], linha[21], linha[22], linha[23], linha[24], linha[25], linha[26], linha[27], linha[28], linha[29], linha[30], linha[31], linha[32]))

        return arr