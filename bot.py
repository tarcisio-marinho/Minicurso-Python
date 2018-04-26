import urllib.request, json

path = "https://api.blinktrade.com/api/v1/BRL/ticker"

req = urllib.request.urlopen(path)

texto = req.read()

dicionario = json.loads(texto)
print(dicionario["high"])








