import requests
class googleMapsWebService:   

    @staticmethod
    def retornarLatitudeLongitude(logradouro, bairro, cidade, uf):
        file = open('apigoogle.txt','r') 
        api = file.readline()
        file.close()
        response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address={0}-{1},{2}-{3}&key={4}".format(logradouro, bairro, cidade, uf, api))  
        resp_json_payload = response.json()
        if (resp_json_payload['status'] == 'OK'):
            return resp_json_payload['results'][0]['geometry']['location']
        elif (resp_json_payload['status'] == 'OVER_QUERY_LIMIT'):
            print(resp_json_payload)
            api = input("Digite uma nova API google Maps no endereco https://developers.google.com/maps/documentation/geocoding/start\n")
            file = open('apigoogle.txt','w') 
            file.write(api)
            file.close()
            googleMapsWebService.retornarLatitudeLongitude(logradouro, bairro, cidade, uf)
        else: 
            print(str(resp_json_payload) + "Log " + logradouro + " Bairro "+  bairro + " Cidade " + cidade + " UF " + uf)
            return ""
            



