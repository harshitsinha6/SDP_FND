

# Importing Libraries
from bs4 import BeautifulSoup as bs
import requests

'''
response = requests.get('https://timesofindia.indiatimes.com/navjson/nav-48986328.cms?preload=1')
print(response.status_code)
data = response.json()

for k, v in data.items():
    for value in v:
        for k, v in value.items():
            print('key: ', k)
            print('value: ', v)
            print("\n\n\n")
            
'''

url = [
       'https://timesofindia.indiatimes.com/navjson/nav-48986328.cms?preload=1',
       'https://timesofindia.indiatimes.com/navjson/nav-296589292.cms?preload=1',
       'https://timesofindia.indiatimes.com/navjson/nav-1898055.cms?preload=1',
       'https://timesofindia.indiatimes.com/navjson/nav-4719148.cms?preload=1',
       'https://timesofindia.indiatimes.com/navjson/nav-1081479906.cms?preload=1',
       'https://timesofindia.indiatimes.com/navjson/nav-17781976.cms?preload=1',
       'https://timesofindia.indiatimes.com/navjson/nav-2886704.cms?preload=1',
       'https://timesofindia.indiatimes.com/navjson/nav-2886704.cms?preload=1',
       'https://timesofindia.indiatimes.com/navjson/nav-9978101.cms?preload=1'
       ]

url1 = [
        'https://www.hindustantimes.com/static-content/10s/cricket-liupre.json',
        'https://content.jwplatform.com/v2/media/ruywLvZt?recommendations_playlist_id=ispf3NOE',
        ''
        ]


source_links = [
    'https://timesofindia.indiatimes.com/home/headlines',
    'https://www.thehindu.com/',
    'https://www.hindustantimes.com/latest-news'
    ]


headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    }

def ScrapData(source_link, target_word):
    src = requests.get(source_link, headers=headers)
    soup = bs(src.content, 'html.parser')
    raws = soup.find_all("a")
    data = []
    for raw in raws:
        data.append((raw.get_text(), str(raw)))
    return data

data = []
for link in source_links:
    data.append(ScrapData(link, 'assam'))
    








