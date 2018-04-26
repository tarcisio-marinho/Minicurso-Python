import urllib.request, json, time

def request(path):
    try:    
        req = urllib.request.urlopen(path)
    except:
        return None
        
    texto = req.read()

    dicionario = json.loads(texto)    

    return dicionario


if __name__ == "__main__":
    path = "https://api.blinktrade.com/api/v1/BRL/ticker"

    precos = []
    while(True):
        dicionario = request(path)
        if(dicionario):
            precos.append(dicionario["high"])
            print("Preço do bitcoin é: {}".format(dicionario["high"]))
            time.sleep(2)
        else:
            print("Sem conexão com a internet. ")
            exit(-1)







