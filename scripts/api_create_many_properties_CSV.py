#!/usr/bin/env python
import requests,csv

url = "https://api.hubapi.com/properties/v1/contacts/properties"
querystring = {"hapikey":API_KEY_HERE}

with open('data.csv',encoding='utf-8-sig')as f:
  data = csv.reader(f)
  for row in data:
    payload = "{\"name\":\""+row[0]+"\",\"label\":\""+row[1]+"\",\"type\":\""+row[2]+"\",\"fieldType\":\""+row[3]+"\",\"groupName\":\"contactinformation\",\"description\":\""+row[4]+"\",\"options\":[]}"
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
        }
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    print(response.text)
