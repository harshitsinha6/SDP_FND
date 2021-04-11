
import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import string
from sklearn.model_selection import train_test_split

class Preprocessing:
    def __init__(self, dataset):
        self.dataset = dataset
        self.X_train = None
        self.Y_train = None
        self.X_test = None
        self.Y_test = None
        self.vectorization = TfidfVectorizer()
        
    def Normalizer(self, text):
        text = text.lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub("\\W"," ",text) 
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)    
        return text
    
    def NormalizeDataset(self, dataset):
        dataset["text"] = dataset["text"].apply(self.Normalizer)
        return dataset

    
    def SplitDATA(self, dataset):
        
        X_data = dataset['text']
        Y_data = dataset['class']
        
        X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size = 0.20)
        return (X_train, X_test, Y_train, Y_test)
    
        
    # Convert text to vectors
    def textTOvectorConvertor(self, X_train, X_test):
        XV_train = self.vectorization.fit_transform(X_train)
        XV_test = self.vectorization.transform(X_test)
        
        return XV_train, XV_test
    
    def preprocess(self):
        self.dataset = self.NormalizeDataset(self.dataset)
        self.X_train, self.X_test, self.Y_train, self.Y_test = self.SplitDATA(self.dataset)
        self.X_train, self.X_test = self.textTOvectorConvertor(self.X_train, self.X_test)
        
        return(self.X_train, self.X_test, self.Y_train, self.Y_test)








