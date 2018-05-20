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
        print("Buscando hospedagens:")
        hospedagens = servicehospedagem.selecionarHospedagens()
        
        for h in hospedagens:
            print(hospedagens.index(h) + 1, len(hospedagens), sep="/", end=" - ")
            tags = self.importarPorCNPJLatitudeLongitude(h.cnpj, h.latitude, h.latitude)
            print(len(tags), "tags encontradas")
            for t in tags:
                self.salvarTags(t)

    def importarTagsRestaurante(self):
        serviceRestaurante = restauranteService() 
        print("Buscando restaurantes:")
        restaurantes = serviceRestaurante.selecionarRestaurantes()
        
        for r in restaurantes:
            print(restaurantes.index(r) + 1, len(restaurantes), sep="/", end=" - ")
            tags = self.importarPorCNPJLatitudeLongitude(r.cnpj, r.latitude, r.latitude)
            print(len(tags), "tags encontradas")
            for t in tags:
                self.salvarTags(t)

    def importarServicosEspecialiados(self):
        serviceServicosEspecialiados = servicosEspecialiadosService() 
        print("Buscando servicos especializados:")
        servicosEspecializados = serviceServicosEspecialiados.selecionarEstabelecimentosEspecializados()
        
        for s in servicosEspecializados:
            print(servicosEspecializados.index(s) + 1, len(servicosEspecializados), sep="/", end=" - ")
            tags = self.importarPorCNPJLatitudeLongitude(s.cnpj, s.latitude, s.latitude)
            print(len(tags), "tags encontradas")
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