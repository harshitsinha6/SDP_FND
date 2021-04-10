
import pandas as pd
import numpy as np
import re



def Normalizer(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text

dataset = dataImporting()

def NormalizeDataset(dataset):
    dataset["text"] = dataset["text"].apply(Normalizer)
    return dataset

dataset = NormalizeDataset(dataset)

def SplitDATA(dataset):
        
    X_data = dataset['text']
    Y_data = dataset['class']
    
    X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size = 0.20)
    return (X_train, X_test, Y_train, Y_test)

X_train, X_test, Y_train, Y_test = SplitDATA(dataset)

# Convert text to vectors
from sklearn.feature_extraction.text import TfidfVectorizer
vectorization = TfidfVectorizer()
def textTOvectorConvertor(X_train, X_test):
    XV_train = vectorization.fit_transform(X_train)
    XV_test = vectorization.transform(X_test)
    
    return XV_train, XV_test

XV_train, XV_test = textTOvectorConvertor(X_train, X_test)








