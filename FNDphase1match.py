

import FNDphase1webscrap as ws

# Compare two news

import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
def match_news(news1, news2):
      
    # tokenization
    news1_list = word_tokenize(news1) 
    news2_list = word_tokenize(news2)
      
    # sw contains the list of stopwords
    sw = stopwords.words('english') 
    lst1 =[]
    lst2 =[]
      
    # remove stop words from the string
    news1_set = {w for w in news1_list if not w in sw} 
    news2_set = {w for w in news2_list if not w in sw}
      
    # form a set containing keywords of both strings 
    rvector = news1_set.union(news2_set) 
    for w in rvector:
        if w in news1_set: 
            lst1.append(1) # create a vector
        else: 
            lst1.append(0)
        if w in news2_set:
            lst2.append(1)
        else:
            lst2.append(0)
            
            
    c = 0
    # cosine formula 
    for i in range(len(rvector)):
            c+= lst1[i]*lst2[i]
    cosine = c / float((sum(lst1)*sum(lst2))**0.5)
    #print("similarity: ", cosine)
    
    return cosine

# match_news("i love chinies food", 'i hate chinies food')
news1 = 'Tesla in Russia? Elon Musk says he is keen to open production hub for EVs'
news2 = "Elon Musk said at a Kremlin conference that Tesla could build a factory in Russia: 'I think we're close to establishing a Tesla presence'"

#match_news(news1, news2)

DATA_TO_COMPARE = []

DATA = ws.DATA_SCRAPPED
for e in DATA:
    # print(" >> >> ",  e)
    v = match_news(e, news1)
    if v > 0.15:
        # print(" >> >> ",  e, "\n\t\t >> ", v)
        DATA_TO_COMPARE.append(e)
        
        
#print(DATA_TO_COMPARE)









