##Para intalar pit install urllib.parse

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig="Ambato"
dest="Quito"
key="H0v9V4ZIBAKtFAwk0ZA4wPDspYCM1SrG"
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)