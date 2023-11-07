import requests
body = {
   
    
    "Product":14860,
    "Type": 0,
    "AirTeperature": 298.1,
    "ProcessTeperature": 308.6,
    "Rotationa1speed": 1551,
    "Too1wear": 0,
    "ac2inefai1ure": 0,
    "TWF": 0,
    "DF": 0,
    "PWF": 0,
    "OSF": 0,
    "RNF": 0
    }
response = requests.post(url = 'http://127.0.0.1:8000/score',
              json = body)
print (response.json())
# output: {'score': 0.866490130600765]]
