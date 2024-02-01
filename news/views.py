from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import *


# GEtting news from  BBC Amharic
bbc_news_r = requests.get('https://www.bbc.com/amharic') 
soup = BeautifulSoup(bbc_news_r.content, 'html.parser') 
headlines_b = soup.find_all("li", class_="bbc-19fk8fk")
headlines_b = headlines_b[:4]
bbcam_news = []

#for tag in headlines_b:
 #   title = tag.find("h3", class_="bbc-8espq9 e47bds20").text.strip()
    #url = tag.find("a")["href"]

#    try:
 #       image_src = tag.find("img")["src"]
  #  except Exception as e:
   #     pass
#headline_obj = NewsArticle.objects.create(title=title, image_src=image_src)
#headline_obj.save()

# GEtting news from  VoA


#Filling the BBC list
for headline in headlines_b:

    max_length = 90  

    if len(headline.text) > max_length:
        truncated_text = headline.text[:max_length-3] + '...'
    else:
        truncated_text = headline.text


    bbcam_news.append(truncated_text)


#Filling the Mereja list




#Filling the VOA list




def index(req):
    return render(req, 'index.html', {'bbcam_news':bbcam_news})
