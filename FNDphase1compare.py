
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

STOP_WORDS = list(set(stopwords.words('english')))
# print(STOP_WORDS)

def toRoot(news):
    lemmatizer = WordNetLemmatizer()
    ps = PorterStemmer()
    sentence = nltk.sent_tokenize(news)
    sentence = [nltk.word_tokenize(data) for data in sentence]
    sentence = [[lemmatizer.lemmatize(w) for w in data] for data in sentence]
    sentence = [w for w in sentence if w not in STOP_WORDS]
    # sentence = [[ps.stem(w) for w in data] for data in sentence]
    sentence = [[lemmatizer.lemmatize(w) for w in data] for data in sentence]
    sentence = [nltk.pos_tag(word) for word in sentence]
    
    D={}
    for data in sentence:
        for word, tag in data:
            #print(word, tag)
            if D.get(tag, False):
                D[tag].append(word)
            else:
                D[tag]=[word]
    #for k, v in D.items():
    #    print(k, v)
    #print("<><><><><><><><><><><><><>")
    return D

def valueCompare(value1, value2, key):
    n1 = len(value1)
    n2 = len(value2)
    c=0.1
    for e in value1:
        if e in value2:
            c+=1*key
    v = c/n1
    #print(v, c)
    return v


def compare(news1, news2):
    news1_root = toRoot(news1)
    news2_root = toRoot(news2)
    
    weightage = {
        'NN': 1.0,
        'IN': 0.4,
        'VBP': 0.6,
        'VB': 0.7,
        'JJ': 0.8
        }
    
    
    negate_statement_check = False
    a, b = False, False
    if news1_root.get('RB', False) or (news1_root.get('VBZ', False) and news1_root['VBZ'] in ["n't", 'not', "doesnot", "havenot"]):
        a=True
    if news2_root.get('RB', False) or news2_root.get('VBZ', False):
        b=True
        
    #print(">>>>>>>>>>>>>>>>>         ", a, b)
        
    negate_statement_check = not a^b
    
    count = 0
    for_compare = 0
    for key, value in news1_root.items():
        if news2_root.get(key, False):
            value1 = news2_root[key]
            #v = valueCompare(value, value1)
            #print(value)
            #print(value1)
            #print(v)
                # todo
            for_compare+=1
            key_v=1
            if weightage.get(key, False):
                key_v = weightage[key]
            if valueCompare(value, value1, key_v)>.2:
                count+=1
                
    print("ITEMS get compared: ", for_compare)
    print("ITEMS matched: ", count)
    compare_percentage = count/for_compare
    
    print("compare percentage: ", compare_percentage)
    print("is find Negate: ", negate_statement_check)
    return compare_percentage
            
            


news1 = "Tesla in Russia? Elon Musk says he is keen to open production hub for EVs"
news2 = "Elon Musk said at a Kremlin conference that Tesla couldn't build a factory in Russia: 'I think we're close to establishing a Tesla presence'"
news2 = news2.lower()
news1 = news1.lower()
# toRoot(news1)
# toRoot(news2)

compare(news1, news2)




