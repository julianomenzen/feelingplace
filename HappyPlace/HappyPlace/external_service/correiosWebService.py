from suds.client import Client
class correiosWebService:   
    
    def __init__(self):
        self.client = Client('https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl')
    
    def buscar_cidade_por_cep(self, cep):
        if (cep == "" or cep == 0):
            return ""
        try:
            return self.client.service.consultaCEP(cep).cidade
        except :
            return "" 
