import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
# Se puede obtener el objeto JSON de dos formas distintas
data = json.loads(response.text)
data = response.json()# La mas recomendable es esta
print('Imprimir los datos traídos de la nube')
print("diccionario:",data)
print("JSON",json.dumps(data, indent=4))

response_2 = requests.get("https://jsonmock.hackerrank.com/api/transactions/search?txnType=debit&page=1")

data_2 = response_2.json()
print(json.dumps(data_2, indent=4))