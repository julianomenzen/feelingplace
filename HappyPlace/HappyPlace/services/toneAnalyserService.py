from instagramRepository import *
from instragram import *
from ibmWebService import *

class toneAnalyserService(object):
    """description of class"""
    def importarSentimentos(self):
       #Instanciar tags
       instaRepository = instagramRepository() 
       ibmTone = ibmWebService()
       #carregar tags em uma lista
       listaTags = instaRepository.consultarTudo()
       for tagInsta in listaTags:
           #busca o sentimento
           tagInsta.sentimento = ibmTone.retornarEmocaoTag(tagInsta.tag)
           #atualizar a tag 
           instaRepository.atualizarSentimento(tagInsta)
       