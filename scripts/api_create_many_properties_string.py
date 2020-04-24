#!/usr/bin/env python
import requests
import ast


first='[["eugeneprop","Eugene Property Label","string","radio","Eugene Property Description"],["eugeneprop2","Eugene Property Label 2","string","text","Eugene PrOperty Description 2"]]'
master=ast.literal_eval(first)


url = "https://api.hubapi.com/properties/v1/contacts/properties"
querystring = {"hapikey":API_KEY_HERE}

for x in range(0, len(master)):
    payload = "{\"name\":\""+master[x][0]+"\",\"label\":\""+master[x][1]+"\",\"type\":\""+master[x][2]+"\",\"fieldType\":\""+master[x][3]+"\",\"groupName\":\"contactinformation\",\"description\":\""+master[x][4]+"\",\"options\":[]}"
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
        }
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    print(response.text)
