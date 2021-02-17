import urllib.request, urllib.parse, urllib.error, ssl
from bs4 import BeautifulSoup


#Scrapes links from The Indian Express of the Top 5 news headlines
def getTopNews() :

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen('https://indianexpress.com/', context = ctx)

    bSoup = BeautifulSoup(html.read(), 'html.parser')
    #For Top news
    findArticles = bSoup.find('div', {'class' : 'top-news'}).find_all('a', recursive = True)

    s = ''
    for art in findArticles :
        s = s + art.attrs['href'] + '\n'
    return s

#Search news scraped from the Indian Express by keyword
def searchNews(word) :
    words = ''
    for i in word.split() :
        words = words + i + '+'
    url = 'https://indianexpress.com/?s=' + words
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE    

    html = urllib.request.urlopen(url, context = ctx)

    bSoup = BeautifulSoup(html.read(), 'html.parser')

    findArticles = bSoup.find('div', {'class' : 'search-result'}).find_all('div',  {'class' : 'details'}, limit = 2)

    s = ''
    for i in findArticles :
        s = s + i.a.attrs['href'] + '\n'
    return s

