from instragram import *
from instagramRepository import *
from instagramWebService import instagramWebService
from hospedagemService import *
from restauranteService import *
from servicosEspecializadosService import *
class instagramService(object):
    """description of class"""
    def importarTags(self):
        self.importarTagsHospedagem()
        self.importarTagsRestaurante()
        self.importarServicosEspecialiados()
    
    def importarTagsHospedagem(self):
        servicehospedagem = hospedagemService() 
        hospedagens = servicehospedagem.selecionarHospedagens()
        
        for h in hospedagens:
            tags = self.importarPorCNPJLatitudeLongitude(h.cnpj, h.latitude, h.latitude)
            for t in tags:
                self.salvarTags(t)

    def importarTagsRestaurante(self):
        serviceRestaurante = restauranteService() 
        restaurantes = serviceRestaurante.selecionarRestaurantes()
        
        for r in restaurantes:
            tags = self.importarPorCNPJLatitudeLongitude(r.cnpj, r.latitude, r.latitude)
            for t in tags:
                self.salvarTags(t)

    def importarServicosEspecialiados(self):
        serviceServicosEspecialiados = servicosEspecialiadosService() 
        servicosEspecializados = serviceServicosEspecialiados.selecionarEstabelecimentosEspecializados()
        
        for s in servicosEspecializados:
            tags = self.importarPorCNPJLatitudeLongitude(s.cnpj, s.latitude, s.latitude)
            for t in tags:
                self.salvarTags(t)

    def importarPorCNPJLatitudeLongitude(self, cnpj, latitude, longitude):
        listInstragram = []
        tokens = instragram.tokensCadastrados()
        for token in tokens:
            tags = instagramWebService.retornarMidiasPorLatitudeLongitude(latitude, longitude, token);
            for t in tags:
                tag = instragram(latitude, longitude, cnpj, t)
                listInstragram.append(tag)

        return listInstragram

    def salvarTags(self, modelInstagram):
        repositorio = instagramRepository()
        return repositorio.inserir(modelInstagram)