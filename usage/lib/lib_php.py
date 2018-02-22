# coding=utf-8
from bs4 import BeautifulSoup
import os, os.path
import nltk
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

response = urlopen('http://php.net/')

html = response.read()

#find number of files
num_files= len([name for name in os.listdir('.') if os.path.isfile(name)])
if num_files == 0:
    numfiles = 2
print num_files

#write to file
file_html = open("/Users/ebrarsahin/GitHub/Graduation-Project/file/html"+str((num_files/2))+".txt", "a")
file_html.write(html)
file_html.close()

#print (html)

#get rid of html tags

soup = BeautifulSoup(html, "html5lib")

text = soup.get_text(strip=True)
text=text.encode('utf-8').decode('ascii','ignore')
file_text = open("/Users/ebrarsahin/GitHub/Graduation-Project/file/text"+str((num_files/2))+".txt", "a")
file_text.write(text)
file_text.close()

print len([name for name in os.listdir('.') if os.path.isfile(name)])

#print(text)
file_tokens = open("/Users/ebrarsahin/GitHub/Graduation-Project/file/tokens"+str((num_files/2))+".txt", "a")

for t in text.split():
    print (t)
    file_tokens.write(t+'\n')
file_tokens.close()

tokens = [t for t in text.split()]
freq = nltk.FreqDist(tokens)

for key, val in freq.items():
    file_token_freq = open("/Users/ebrarsahin/GitHub/Graduation-Project/file/token_freq" + str((num_files / 2)) + ".txt", "a")
    file_token_freq.write(str(key) + ':' + str(val) + '\n')
    print (str(key) + ':' + str(val))
file_token_freq.close()

freq.plot(20, cumulative=False)