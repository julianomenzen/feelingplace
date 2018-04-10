from instragram import *
from instagramWebService import instagramWebService
from hospedagemService import *
class instagramService(object):
    """description of class"""
    def importarTags(self):
        servicehospedagem = hospedagemService() 
        hospedagens = servicehospedagem.selecionarHospedagens()
        for h in hospedagens:
            self.importarPorCNPJLatitudeLongitude(h.cnpj, h.latitude, h.latitude)

    def importarPorCNPJLatitudeLongitude(self, cnpj, latitude, longitude):
        listInstragram = []
        tokens = instragram.tokensCadastrados()
        for token in tokens:
            tags = instagramWebService.retornarMidiasPorLatitudeLongitude(latitude, longitude, token);
            for t in tags:
                tag = instragram(latitude, longitude, cnpj, t)
                listInstragram.append(tag)

        return listInstragram

