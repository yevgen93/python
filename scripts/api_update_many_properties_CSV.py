#!/usr/bin/env python

import requests,csv, os
from io import open

querystring = {"hapikey":os.environ["apikey"]}

with open('data.csv',encoding='utf-8-sig')as f:
  data = csv.reader(f)
  for row in data:
    url = "https://api.hubapi.com/properties/v2/tickets/properties/named/{}".format(row[0])
    payload = "{\"name\":\""+row[0]+"\",\"label\":\""+row[1]+"\"}"
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
        }
    response = requests.request("PATCH", url, data=payload, headers=headers, params=querystring)
    print(response.text)
