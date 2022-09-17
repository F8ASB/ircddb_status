#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#GET Informations about your repeater on IRCDDB French Webpage
#
#F8ASB 2022 - F8ASB.COM
#

import requests

url="https://status.ircddb.net/repeater.php?n=51&ctry=FRA"
requete = requests.get(url)
page = requete.text

search_start = page.find('<a href="/cgi-bin/ircddb-log?30 0 F1ZBU    F1ZBU__B">')        >
search_stop = page.find('Epinal 88, JN38ee')      # And close it...

premier = page[search_start-49:search_start-18]
deuxieme = page[search_start+80:search_start+111]

print("Statut Relais:")
print(premier)

if "green" in premier:
    print("CONNECTED")
else:
    print("DISCONNECTED")

print("Statut Gateway:")
print(deuxieme)
if "green" in deuxieme:
    print("CONNECTED")
else:
    print("DISCONNECTED")
