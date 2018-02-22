# coding=utf-8
from bs4 import BeautifulSoup
import os, os.path
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

file= open("/Users/ebrarsahin/GitHub/Graduation-Project/file/rrh.html", "r")
story= file.read()
file.close()

#find number of files
num_files= len([name for name in os.listdir('.') if os.path.isfile(name)])
if num_files == 0:
    numfiles = 2
print num_files

#write to file
file_html = open("/Users/ebrarsahin/GitHub/Graduation-Project/file/story.txt", "w")
file_html.write(story)
file_html.close()
# #
# # #print (html)
# #
# #get rid of html tags

soup = BeautifulSoup(story, "html5lib")

text = soup.get_text(strip=True)
text=text.encode('utf-8').decode('ascii','ignore')
file_text = open("/Users/ebrarsahin/GitHub/Graduation-Project/file/text"+str((num_files/2))+".txt", "w")
file_text.write(text)
file_text.close()

#print(text)
file_tokens = open("/Users/ebrarsahin/GitHub/Graduation-Project/file/tokens"+str((num_files/2))+".txt", "w")

for t in text.split():
    print (t)
    file_tokens.write(t+'\n')
file_tokens.close()

tokens = [t for t in text.split()]
freq = nltk.FreqDist(tokens)

for key, val in freq.items():
    file_token_freq = open("/Users/ebrarsahin/GitHub/Graduation-Project/file/token_freq" + str((num_files / 2)) + ".txt", "w")
    file_token_freq.write(str(key) + ':' + str(val) + '\n')
    print (str(key) + ':' + str(val))
file_token_freq.close()

#clean tokens before plotting

clean_tokens = tokens[:]

for token in tokens:

    if token in stopwords.words('english'):
        clean_tokens.remove(token)

freq.plot(20, cumulative=False)