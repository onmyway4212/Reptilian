import json
from urllib.request import urlopen

def getCountry(ipAddress):
    response = urlopen('http://freegeoip.net/json/'+ipAddress).read().decode('utf-8')
    responsejson = json.loads(response)
    return responsejson.get('city')


print(getCountry('101.71.37.164'))