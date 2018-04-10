import requests
class instagramWebService(object):
    def retornarMidiasPorLatitudeLongitude(latitude, longitude, token):
        #response = requests.get("https://api.instagram.com/v1/media/search?lat={0}&lng={1}&access_token={2}".format(-16.4512405,-39.0716458, token))
        response = requests.get("https://api.instagram.com/v1/media/search?lat={0}&lng={1}&access_token={2}".format(latitude, longitude, token))       
        resp_json_payload = response.json()
        tags = []
        if (resp_json_payload['meta']['code'] == 200):
            for attribution in resp_json_payload['data']:
                for tag in attribution['tags']:
                    tags.append(tag)

            return tags 
        else: 
            print(str(resp_json_payload))
            return ""



