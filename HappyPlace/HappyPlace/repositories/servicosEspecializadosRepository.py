from databaseService import *
from estabelecimentoEspecializado import *

class servicosEspecializadosRepository(object):
    """description of class"""
    def inserir(self, model):
        if (not self.validaExistePorCNPJ(model.cnpj)):
            comando = "insert into especializados (razaosocial , nomefantasia ,cnpj , natureza ,datainicio , porte , situacao , tipoatividade , subtipo , cep , uf , localidade , bairro , logradouro , telefone , fax , email2 , email3 , site , certificado , codigodescricaocnae , servicos , segmento ,linguas, latitude, longitude) " 
            comando = comando + " values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (model.razaosocial , model.nomefantasia ,model.cnpj , model.natureza ,model.datainicio , model.porte , model.situacao , model.tipoatividade , model.subtipo , model.cep , model.uf , model.localidade , model.bairro , model.logradouro , model.telefone , model.fax , model.email2 , model.email3 , model.site , model.certificado , model.codigodescricaocnae , model.servicos , model.segmento ,model.linguas, model.latitude, model.longitude)
            executarComando(comando)

    def validaExistePorCNPJ(self, cnpj):
        return RegistroExite("SELECT cnpj FROM especializados WHERE cnpj = '{0}'".format(cnpj))

    def consultarTudo(self):
        linhas = SelecionarRegistros("select * from especializados ")

        arr = []
        for linha in linhas:
            arr.append(estabelecimentosEspecializados(linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16], linha[17], linha[18], linha[19], linha[20], linha[21], linha[22], linha[23], linha[24], linha[25], linha[26]))

        return arr