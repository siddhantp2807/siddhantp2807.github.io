import urllib.request
import urllib.parse
import urllib.error
import ssl
from bs4 import BeautifulSoup
import re


#Ignore invalid urls

ctx = ssl.create_default_context()
ctx.check_hostname = False

ctx.verify_mode = ssl.CERT_NONE
beginSec = re.compile(r'^(https://)')
endCss = re.compile(r'(.css)$')
# print(endCss.findall('https://www.youtube.com/.css'))


url = input("Enter the webpage URL: ")
domain = 'https://' + url.split('//')[1].split('/')[0]
html = urllib.request.urlopen(url, context=ctx)

bs = BeautifulSoup(html.read(), 'html.parser')

cssCode = bs.find_all('link', {'rel' : 'stylesheet'})

c = 0
for code in cssCode :
    if beginSec.findall(code.attrs['href']) and endCss.findall(code.attrs['href']) :

        print("The CSS Code's link is: ", code.attrs['href'])
        c += 1
    elif (beginSec.findall(code.attrs['href']) == []) and endCss.findall(code.attrs['href']) :
        print("The CSS Code's link is: ", domain + code.attrs['href'])
        c += 1

if c == 0 :
    print('Could not find .css file extension.')
    for code in cssCode :

        if beginSec.findall(code.attrs['href']) :

            print("Link: ", code.attrs['href'])
            
        elif (beginSec.findall(code.attrs['href']) == []) :
            print("Link: ", domain + code.attrs['href'])
            
