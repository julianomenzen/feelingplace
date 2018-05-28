class instragram(object):
    """description of class"""
    id = 0
    latitude = 0.0
    longitude = 0.0
    cnpj = ""
    tag = ""
    sentimento = ""

    def __init__(self, latitude, longitude, cnpj, tag):
        self.latitude = latitude
        self.longitude = longitude
        self.cnpj = cnpj
        self.tag = tag

    @staticmethod 
    def tokensCadastrados():
        listTokens = []
        listTokens.append("4255763955.a56a369.89af9b5c9c2a4b7f99849f41c1145d9a");
        return listTokens
