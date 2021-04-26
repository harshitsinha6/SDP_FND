
import requests
from bs4 import BeautifulSoup as bs
import json 
import time
import FNDphase2BUFFUR_A as fa
prev = ''

conn = fa.conn
while True:
    t = time.asctime()
    t = str(t).split()
    t = t[3]
    t = t.split(':')
    t = t[0]
    if t != prev:
    
        url = "https://timesofindia.indiatimes.com/navjson/nav-48986328.cms?preload=1"
        
        src = requests.get(url)
        soup= bs(src.content, 'html.parser')
        text = soup.text
        
        jsonObject = json.loads(src.text)
        #print(jsonObject)
        
        myData = {}
        for d in jsonObject['stories']:
            myData[d['title']] = d['link']
            
        myDataNews = {}
        link = "https://timesofindia.indiatimes.com"
        for k, v in myData.items():
            link = link+v
            
            src1 = requests.get(link)
            soup1 = bs(src1.content, 'html.parser')
            text1 = soup1.text
            #idxlast = text1.index("Latest NewsQuick") if "Latest NewsQuick" in text1 else 100
            #text1 = text1[: idxlast-5]
            myDataNews[k] = text1
            text2 = ''
            for e in text1:
                if ord(e)!=34:
                    text2+=e
                    
            
            conn = fa.putDatainBuffer(conn, k, text2, 1)
        prev = t
        print(prev)
    else:
        break
        

    
        
    
        
