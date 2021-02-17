#Program to find out how two wikipedia pages are connected
import urllib.request, urllib.error, urllib.error
import ssl
import re
from bs4 import BeautifulSoup
import random
import sys

#Ignore invalid URLs

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE






def getLinks(url) :
   
    regexGen = re.compile(r'^https://en.wikipedia.org/wiki/')

    lst = []
    regResult = regexGen.findall(url)
    if (len(regResult) != 0) :
        html = urllib.request.urlopen(url, context=ctx)
        bs = BeautifulSoup(html.read(), 'html.parser')
        links = bs.find_all('a', href = re.compile('^(/wiki/)((?!:).)*$'))
        for link in links :
            lst.append('https://en.wikipedia.org' + link.attrs['href'])
        
    elif (len(regResult) == 0) :
        sys.exit(0)
    return lst



#returns a list of all wikipedia pages in between the url and found

def ultimateGetLinks(url, found) :
    response = "Y"
    urlList = list()
    while True :
        x = getLinks(url)
        # for link in x :
        #     print(link)
        if found in x :
            response = 'N'
            break
        else :
            print(url)
            url = x[random.randint(1, len(x)-1)]
        urlList.append(url)
        
    return urlList


url = input("Enter the URL- ")
finalUrl = input('Enter destination URL- ')

print(ultimateGetLinks(url, finalUrl))