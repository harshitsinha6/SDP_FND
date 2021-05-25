
# Phase 1

import requests
from bs4 import BeautifulSoup as bs
import urls
import json


DATA_SCRAPPED = []
    
def scrapTOI(url):
    src = requests.get(url)
    response = json.loads(src.content)    
    required_data = []         # data where we store data which is required (title and link to follow)
    #print(response['stories'])
    v = ''
    for k, v in response.items():
        v = k
        
    if v=='items':
        v1 = None
        for e in response[v]:
            for k, v1 in e.items():
                if k=='stories':
                    v1 = v1
                    break
        for data in v1:
            for k, v in data.items():
                if k=='title' or k=='link':
                    if k=='link':
                        v = "https://timesofindia.indiatimes.com"+v
                    required_data.append({
                        k: v
                        })
        return required_data
    else:
        for data in response[v]:
            for k, v in data.items():
                if k=='title' or k=='link':
                    required_data.append({
                        k: v
                        })
        #print(required_data)
        return required_data
    
    
'''TOI_SCRAPPED_DATA = []
# url = urls.TOI_URLS[0]
# print(url)

for url in urls.toi_urls:
    data = scrapTOI(url)
    for d in data:
        TOI_SCRAPPED_DATA.append(d)
        
# print(TOI_SCRAPPED_DATA)'''
    

HT_SCRAPPED_DATA=[]
def scrapHT(url):
    src = requests.get(url, headers=urls.headers)
    soup = bs(src.content, 'html.parser')
    data = soup.text
    data = data.split("\n")
    data = set(data)
    return list(data)


for url in urls.HT_URLS:
    HT_SCRAPPED_DATA.append(scrapHT(url))

# print(HT_SCRAPPED_DATA)
for data in HT_SCRAPPED_DATA:
    for e in data:
        #print(">> ", e)
        if len(e) > 20:
            DATA_SCRAPPED.append(e)



TH_SCRAPPED_DATA = []
def scrapTH(url):
    src = requests.get(url)
    soup = bs(src.content, 'html.parser')
    #print(soup.text)
    data = soup.text
    data = data.split("\n")
    data = set(data)
    return list(data)


for url in urls.TH_URLS:
    TH_SCRAPPED_DATA.append(scrapTH(url))

#print(TH_SCRAPPED_DATA)
for data in TH_SCRAPPED_DATA:
    for e in data:
        #print(" >>  ",e)
        if len(e) > 20:
            DATA_SCRAPPED.append(e)


"""for e in DATA_SCRAPPED:
    print(" ++++++>>>> ", e)"""
    
    
print(len(DATA_SCRAPPED))





