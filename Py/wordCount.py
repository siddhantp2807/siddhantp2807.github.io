import urllib.request
import urllib.parse
import urllib.error
import ssl
from bs4 import BeautifulSoup
import re

#script that performs a wordcount of all words (case sensitive)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the url: ")

wordAsk = input("Enter the word: ")
html = urllib.request.urlopen(url, context=ctx)

bs = BeautifulSoup(html.read(), 'html.parser')

finalText = bs.get_text()

wordsRegex = re.compile(r'[A-Za-z]+')
grp = wordsRegex.findall(finalText)

wordCount = dict()

for word in grp :
        wordCount[word] = wordCount.get(word, 0) + 1

try :
    print(wordCount[wordAsk])

except :
    print("0")



