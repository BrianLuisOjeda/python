import json
import re
import requests
import numpy


def fetch(page_number, location_id):
    url2 = "https://jsonmock.hackerrank.com/api/transactions/search?txnType=debit&page=1"
    url = f"https://jsonmock.hackerrank.com/api/transactions/search?txnType=debit&page={page_number}"
    response = requests.get(url2)
    data = response.json()
    dataset = []

    for i in data["data"]:
        key = i["userId"]
        amount = i["amount"]
        id = location_id
        if i["location"]["id"] == id:
            user = {}
            user["userId"] = key
            user["amount"] = amount
            dataset.append(user)
    return dataset
    

def transform(dataset):
    data = [
        
    ]
    lista = []
    users = {}
    
    for i in dataset:
        # amount_str es el valor en string con el $ tomado del dataset    
        amount_str = str(i["amount"])
        amount = float(re.sub(r'[^\d\-.]', '', amount_str)) 

        if len(lista) == 0:
            user = {}
            user["userId"] = i["userId"]
            user["amount"] = amount
            lista.append(user)
        
        for e in lista:
            if i["userId"] == e["userId"]:
                print(f"usuario repetido {i}")
                i[amount] + e[amount]
            else:
            #elif i["userId"] not in lista:
                user = {}
                user["userId"] = i["userId"]
                user["amount"] = amount
                lista.append(user)
            
            #suma = users[amount] + amount
        
    print(lista)

if __name__ == "__main__":

    dataset = fetch(2, 7)
    data = transform(dataset)
    #report(data)
