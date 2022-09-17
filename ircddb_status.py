#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#GET Informations about your repeater on IRCDDB Database
#
#F8ASB 2022 - F8ASB.COM
#

import requests
import json

url="https://status.ircddb.net/ircddbgw.json"
i = ""

r = requests.get(url)
data = json.loads(r.text)
info = data["ircddbgw"]

json_str = json.dumps(data, indent=4)

#info status 
#t = connected
#f = deconnected 

for i in info:
    #replace F1ZBU with your repeater callsign
    if i['zonerp_cs'] == "F1ZBU   ":
        print("*************************")
        print("*  INFORMATIONS: "+i['zonerp_cs'][:-3]+ "  *")
        print("*************************")
        print("")
        print("+----------------------+")
        print("Statut:")
        if (i['status'])=="t":
            print("CONNECTED")
        else:
            print("DECONNECTED")
        print("+----------------------+")
        print("Dernière connection:")
        print(i['lastin'][:-3])
        print("+----------------------+")
        print("Dernière deconnection::")
        print(i['lastout'][:-3])
        print("+----------------------+")
        print("Dernière activité:")
        print(i['last_act'][:-3])
        print("+----------------------+")
        print("Adresse IP:")
        print(i['zonerp_ipaddr'])
        print("+----------------------+")
        print("Pays:")
        print(i['country_code'])
        print("+----------------------+")
