class municipio(object):
    """description of class"""
    uf = ""
    regiao = ""
    municipio = ""
    categoria = ""

    def __init__(self, uf, regiao, municipio, categoria):
      self.uf = uf
      self.regiao = regiao
      self.municipio = municipio
      self.categoria = categoria
      