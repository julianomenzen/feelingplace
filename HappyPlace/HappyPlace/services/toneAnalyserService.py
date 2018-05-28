from instagramRepository import *
from instragram import *

class toneAnalyserService(object):
    """description of class"""
    def importarSentimentos(self):
       #Instanciar tags
       instaRepository = instagramRepository() 
       #carregar tags em uma lista
       listaTags = instaRepository.consultarTudo()
       for tagInsta in listaTags:
           #busca o sentimento
           tagInsta.sentimento = "felicidade"
           #atualizar a tag 
           instaRepository.atualizarSentimento(tagInsta)
       