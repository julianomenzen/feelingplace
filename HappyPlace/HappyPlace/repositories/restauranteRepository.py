from databaseService import *
from estabelecimentoAlimenticio import *

class restauranteRepository(object):
    """description of class"""
    def inserir(self, model):
        if (not self.validaExistePorCNPJ(model.cnpj)):
            comando = "insert into restaurantes (razaosocial  ,nomefantasia  ,cnpj  ,naturezajuridica  ,datainicio  ,porte  ,situacao  ,tipoatividade  ,subtipo  ,cep  ,uf  ,localidade  ,bairro  ,logradouro  ,telefone  ,fax  ,email2  ,email3  ,site  ,codigocertificado  ,codigodescricaocnae  ,capacidade  , linguas, latitude, longitude ) " 
            comando = comando + " values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (model.razaosocial  ,model.nomefantasia  ,model.cnpj  ,model.naturezajuridica  ,model.datainicio  ,model.porte  ,model.situacao  ,model.tipoatividade  ,model.subtipo  ,model.cep  ,model.uf  ,model.localidade  ,model.bairro  ,model.logradouro  ,model.telefone  ,model.fax  ,model.email2  ,model.email3  ,model.site  ,model.codigocertificado  ,model.codigodescricaocnae  ,model.capacidade  , model.linguas, model.latitude, model.longitude )
            executarComando(comando)

    def validaExistePorCNPJ(self, cnpj):
        return RegistroExite("SELECT cnpj FROM restaurantes WHERE cnpj = '{0}'".format(cnpj))

    def consultarTudo(self):
        linhas = SelecionarRegistros("select * from restaurantes ")

        arr = []
        i = 0;
        for linha in linhas:
            arr.append(estabelecimentosAlimenticios(linhas[i][1], linhas[i][2], linhas[i][3], linhas[i][4], linhas[i][5], linhas[i][6], linhas[i][7], linhas[i][8], linhas[i][9], linhas[i][10], linhas[i][11], linhas[i][12], linhas[i][13], linhas[i][14], linhas[i][15], linhas[i][16], linhas[i][17], linhas[i][18], linhas[i][19], linhas[i][20], linhas[i][21], linhas[i][22], linhas[i][23], linhas[i][24], linhas[i][25], linhas[i][26], linhas[i][27], linhas[i][28], linhas[i][29], linhas[i][30], linhas[i][31], linhas[i][32]))
            i = i + 1

        return arr
