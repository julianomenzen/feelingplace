import requests
class googleMapsWebService:   

    @staticmethod
    def retornarLatitudeLongitude(logradouro, bairro, cidade, uf, tokens):
        response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address={0}-{1},{2}-{3}&key={4}".format(logradouro, bairro, cidade, uf, tokens.getTokenAtual()))  
        resp_json_payload = response.json()
        if (resp_json_payload['status'] == 'OK'):
            return resp_json_payload['results'][0]['geometry']['location']
        elif (resp_json_payload['status'] == 'OVER_QUERY_LIMIT'):
            tokens.updateToken();
            googleMapsWebService.retornarLatitudeLongitude(logradouro, bairro, cidade, uf, tokens)
        else: 
            print(str(resp_json_payload) + "Log " + logradouro + " Bairro "+  bairro + " Cidade " + cidade + " UF " + uf)
            return ""
            



