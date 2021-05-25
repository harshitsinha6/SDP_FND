

TOI_URLS = [
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

TH_URLS = [
        'https://www.thehindu.com/',
        'https://www.thehindu.com/news/'
        ]


HT_URLS = [
    'https://www.hindustantimes.com/',
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
        url = str(raw)
        d = raw.get_text()
        if len(d)>2 and 'href' in url and 'https:' in url:
            index = url.index('href')
            u = ''
            for i in url[index+5:]:
                if i==' ' or i==">":
                    break
                u+=i
            data.append((d, u))
    return data

data = []
'''for link in source_links:
    data.append(ScrapData(link, 'assam'))'''
    






'''
conn = sqdb.connect("testdb.db")

print("db open or created successfully")

#conn.execute("Create table test1(ID number, NEWS TEXT);")
#print("table creat'ed sucessfully")

def putdata(id1, data):
    st = "insert into test1(ID, NEWS) values(%s, '%s');"%(id1, data)
    print(st)
    conn.execute(st)
    conn.commit()
    

putdata(1, "hello")
putdata(2, "harshit")
putdata(3, "raj")
putdata(4, "sinha")
putdata(5, "12345")


#conn.execute("INSERT INTO TEST1(ID, NEWS) VALUES (1, 'HELLO');")

#print("data put successfully")

cursor = conn.execute("select * from test1;")
print(cursor)
for r in cursor:
    print(">>>> ", r)

print('printing done!')

#print(conn.execute("desc test;"))
'''


