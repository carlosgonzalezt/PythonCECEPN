##Para intalar pit install urllib.parse

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key="H0v9V4ZIBAKtFAwk0ZA4wPDspYCM1SrG"

while True:
    orig=input("Origen: ")
    dest=input("Destino: ")
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: "+(url))
    

