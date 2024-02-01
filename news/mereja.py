from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import *

# GEtting news from  Mereja
mereja_news_r = requests.get('https://mereja.com/amharic/v2/') 
soup = BeautifulSoup(mereja_news_r.content, 'html.parser') 
headlines_m = soup.find_all('h1', class_='entry-title post-title')
headlines_m = headlines_m[:4]
m_news = []

for tag in headlines_m:
    text = tag.a.text.strip()
    image_src = tag.img['src']
    url = tag.a['href']

#Filling the Mereja list
for headline in headlines_m:

    #title = headline.text.strip()
    #url = 'None'
    #headline_obj = NewsArticle.objects.create(title=title)
    #headline_obj.save()


    max_length = 90  

    if len(headline.text) > max_length:
        truncated_text = headline.text[:max_length-3] + '...'
    else:
        truncated_text = headline.text


    m_news.append(truncated_text)
    print(truncated_text)