
# Importing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

import re, pickle
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import Models
import DataPreprocessing

# Importing Datasets

def dataImporting():

    fake_news = pd.read_csv('Fake.csv')
    real_news = pd.read_csv('True.csv')
    
    fake_news['class'] = 0
    real_news['class'] = 1
    
    fake_manual_testing = fake_news.tail(10)
    for i in range(len(fake_news)-1, len(fake_news)-11, -1):
        fake_news.drop([i], axis=0, inplace=True)
        
        
    real_manual_testing = real_news.tail(10)
    for i in range(len(real_news)-1, len(real_news)-11, -1):
        real_news.drop([i], axis=0, inplace=True)
        
    manual_testing = pd.concat([fake_manual_testing, real_manual_testing], axis=0)
    manual_testing.to_csv("manual_testing.csv")
    
    merge_dataset = pd.concat([fake_news, real_news], axis = 0)
    
    dataset = merge_dataset.drop(["title", "subject", "date"], axis=1)

    dataset.isnull().sum()
    dataset = dataset.sample(frac=1)
    
    return dataset

dataset = dataImporting()

# make object and send with the constructor
DataPreprocessingObject = DataPreprocessing.Preprocessing(dataset)
X_train, X_test, Y_train, Y_test = DataPreprocessingObject.preprocess()

def models():
    '''from sklearn.linear_model import LogisticRegression
    LR_model = LogisticRegression()
    LR_model.fit(XV_train,Y_train)
    
    pred_LR_model=LR_model.predict(XV_test)
    
    print("Accuracy : ", LR_model.score(XV_test, Y_test))
    return LR_model'''

    model = Models.models()
    # print(model.model, model.LR_model, model.DT_model, model.GB_model, model.RF_model)
    model.feedData(X_train, Y_train, X_test, Y_test)
    model.fit()
    model.predict()
    model.selectModel()
    model = model.giveModel()
    return model

model = models()

# Manual testing

def manual_testing_news(news, model):
    testing_news = {"text": [news]}
    test_data = pd.DataFrame(testing_news)
    test_data["text"] = test_data["text"].apply(DataPreprocessingObject.Normalizer)
    X_data_test = test_data["text"]
    print(X_data_test)
    vectorization = TfidfVectorizer()
    vectorization.fit_transform(X_data_test)
    XV_data_test = vectorization.transform(X_data_test)
    pred_value = model.predict(XV_data_test)
    return pred_value


news = """BRUSSELS (Reuters) - NATO allies on Tuesday welcomed President Donald Trump s decision to commit more forces to Afghanistan,
 as part of a new U.S. strategy he said would require more troops and funding from America s partners. 
 Having run for the White House last year on a pledge to withdraw swiftly from Afghanistan, 
 Trump reversed course on Monday and promised a stepped-up military campaign against  Taliban insurgents, 
 saying:  Our troops will fight to win .  U.S. officials said he had signed off on plans to send about 4,000 
 more U.S. troops to add to the roughly 8,400 now deployed in Afghanistan. But his speech did not define benchmarks
 for successfully ending the war that began with the U.S.-led invasion of Afghanistan in 2001, and which he acknowledged 
 had required an   extraordinary sacrifice of blood and treasure .  We will ask our NATO allies and global partners to support
 our new strategy, with additional troops and funding increases in line with our own. We are confident they will,  Trump said. 
 That comment signaled he would further increase pressure on U.S. partners who have already been jolted by his repeated demands 
 to step up their contributions to NATO and his description of the alliance as  obsolete  - even though, since taking office, 
 he has said this is no longer the case. NATO Secretary General Jens Stoltenberg said in a statement: 
     NATO remains fully committed to Afghanistan and I am looking forward to discussing the way ahead with (Defense)
     Secretary (James) Mattis and our Allies and international partners.  NATO has 12,000 troops in Afghanistan, 
     and 15 countries have pledged more, Stoltenberg said. Britain, a leading NATO member, called the U.S. commitment  
     very welcome .  In my call with Secretary Mattis yesterday we agreed that despite the challenges, we have to stay the 
     course in Afghanistan to help build up its fragile democracy and reduce the terrorist threat to the West,  
     Defence Secretary Michael Fallon said. Germany, which has borne the brunt of Trump s criticism over  
     the scale of its defense spending, also welcomed the new U.S. plan.  Our continued commitment is necessary
     on the path to stabilizing the country,  a government spokeswoman said. In June, European allies had already pledged 
     more troops but had not given details on numbers, waiting for the Trump administration to outline its strategy for the 
     region.Nearly 16 years after the U.S.-led invasion - a response to the Sept. 11 attacks which were planned by al Qaeda leader
     Osama bin Laden from Afghanistan - the country is still struggling with weak central government and a Taliban insurgency. 
     Trump said he shared the frustration of the American people who were  weary of war without victory , but a hasty withdrawal
     would create a vacuum for groups like Islamic State and al Qaeda to fill."""
     
print(manual_testing_news(news, model))
