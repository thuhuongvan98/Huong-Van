import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['c4e']

kpop_collection = db['kpop']

import requests
from bs4 import BeautifulSoup

kpop_data = requests.get('https://dbkpop.com/db/all-k-pop-idols?fbclid=IwAR0JY5BFzSalTz4C5SW4alf6vHtaOZct-f8N-XpSuGENlQEgyBgp4cvkQyY')

soup = BeautifulSoup(kpop_data.text, 'html.parser')

kpop_collection.delete_many({})

table_body = soup.find('tbody')

tr_content = table_body.find_all('tr')
kpop_all = []
for tr in tr_content:
    td_content = tr.find_all('td')
    info = []
    for td in td_content:
        info.append(td.string)
    kpop_all.append(info)

for i in kpop_all:
    kpop_collection.insert_one({
        'Stage name': i[1],
        'Korean name': i[3],
        'DOB': i[5],
        'Group': i[6],
    })