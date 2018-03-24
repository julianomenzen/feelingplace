import re
class funcoesString(object):
    @staticmethod
    def somenteNumeros(texto):
        return re.sub("[^0-9]", "", texto)
