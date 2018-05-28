import requests
import json
class ibmWebService(object):   
    def retornarEmocaoTag(self, tag):
        session = requests.Session()
        session.auth = ("382f1638-ee10-4158-bf10-b78576181302", "6TFb5g07hCND")

        response = session.get("https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21&text={0}".format(str.replace(tag, "#", "")))  

        resp_json_payload = response.json()
        try:
            return resp_json_payload['document_tone']['tones'][0]['tone_name']
        except:
            return ""
    
    
        
 