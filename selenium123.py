
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 14:34:45 2021

@author: Harshit
"""

# Importing Libraries
from bs4 import BeautifulSoup
import requests
import selenium
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome("C:/Users/Pratyush/Downloads/chromedriver_win32/chromedriver.exe")

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
# driver.get("https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq")

driver.get('https://www.hindustantimes.com/latest-news')

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text) 
    
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')

news = 'narendra modi is prime minister'

def find_links():
    return 0


