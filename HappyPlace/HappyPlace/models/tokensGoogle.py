
class tokensGoogle(object):
    """description of class"""
    listaTokens = []
    linha = 0

    def __init__(self):
        self.listaTokens.append("AIzaSyCWhAnQ80OxbOCineGjTzaL0obPgswJKq8")
        self.listaTokens.append("AIzaSyB2mD3gR8vXSmWIgCQpkDAjF4ySJMMaH6U")
        self.listaTokens.append("AIzaSyDlNhU4Wjbxc_iJ8ipO9P6TGWCfPu4B-9c")
        self.linha = 0

    def getTokenAtual(self):
        return self.listaTokens[self.linha]

    def updateToken(self):
        self.linha = self.linha + 1


        




